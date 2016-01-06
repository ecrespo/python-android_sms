#!/usr/bin/env python
# -*- coding: utf-8 -*-
#libreria estándar loggin y time


import logging
import time

#de python-daemon import runner
import daemon

from daemon import runner
from pywrapper_config import Config
from deviceCell import Cell
from SOAPpy import SOAPServer
import sys 



from sys import exit

configfile = "./conf/devicecelldaemon.conf"


class AppDemonio(object):
    """clase que inicia el demonio de la aplicacion"""
    def __init__(self,config_file):
        """se define unos path estándar en linux."""
        self._config_file = config_file
        self._configuracion = Config(self._config_file)
        self.stdin_path = self._configuracion.show_value_item("paths","null")
        self.stdout_path = self._configuracion.show_value_item("paths","stdout")
        self.stderr_path = self._configuracion.show_value_item("paths","stderr")
        #Se define la ruta del archivo pid del demonio.
        self.pidfile_path = self._configuracion.show_value_item("paths","pidfile")
        self.pidfile_timeout = int(self._configuracion.show_value_item("time","timeout"))
        self.logfile = self._configuracion.show_value_item("paths","logfile")

    @property
    def config_file(self):
        """getter de config_file"""
        return self._config_file
    
    @config_file.setter
    def config_file(self,config_file):
        """Setter de config_file"""
        self._config_file = config_file
        self._configuracion = Config(self._config_file)
        self._stdin_path = self._configuracion.show_value_item("paths","null")
        self._stdout_path = self._configuracion.show_value_item("paths","stdout")
        self._stderr_path = self._configuracion.show_value_item("paths","stderr")
        #Se define la ruta del archivo pid del demonio.
        self._pidfile_path = self._configuracion.show_value_item("paths","pidfile")
        self._pidfile_timeout = int(self._configuracion.show_value_item("time","timeout"))
        self._logfile = self._configuracion.show_value_item("paths","logfile")


    def __getattr__(self):
        """Si se intenta acceder a un atributo inexistente se devuelve None"""
        return None


    def run(self):
        """Ejecucion del demonio"""
        cell = Cell()
        server = SOAPServer(("localhost",8580))
        server.registerFunction(cell.detectar_dispositivos)
        while True:
            try:
                cell.config_file = configfile         
                server.serve_forever()
                logger.info("deviceCelldaemond started")
            except KeyboardInterrupt:
                logger.info("deviceCelldaemond ended")
                exit()
            time.sleep(self._pidfile_timeout)



if __name__ == "__main__":
    app = AppDemonio(configfile)
    #define la instancia de la clase logging para generar la bitacora
    logger = logging.getLogger("devicecelldaemon log")
    logger.setLevel(logging.INFO)
    #Se define el forma del log
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(app.config_file)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    #Se ejecuta el demonio llamando al objeto app

    daemon_runner = runner.DaemonRunner(app)
    #Esto evita que el archivo log no se cierre durante la ejecución del demonio
    daemon_runner.daemon_context.files_preserve=[handler.stream]
    #Ejecuta el método run del objeto app
    daemon_runner.do_action()
