#!/usr/bin/env python
# -*- coding: utf-8 -*-
#libreria estándar loggin y time


import logging
import time

#de python-daemon import runner
from daemon import runner
from pywrapper_config import Config
from deviceCell import Servicio





class App(object):
    def __init__(self,config_file):
        """se define unos path estándar en linux."""
        self._config_file = config_file
        self._configuracion = Config(self._config_file)
        self._stdin_path = self._configuracion.show_value_item("paths","null")
        self._stdout_path = self._configuracion.show_value_item("paths","stdout")
        self._stderr_path = self._configuracion.show_value_item("paths","stderr")
        #Se define la ruta del archivo pid del demonio.
        self._pidfile_path = self._configuracion.show_value_item("paths","pidfile")
        self._pidfile_timeout = int(self._configuracion.show_value_item("time","timeout"))


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


    def __getattr__(self):
        """Si se intenta acceder a un atributo inexistente se devuelve None"""
        return None


    def run(self):
        """Ejecucion del demonio"""
        i = 0
        while True:
            #El código principal va acá
            i += 1
            #Diferentes niveles de registro de bitacora
            logger.debug("Debug message %s" %i)
            logger.info("Info message %s" %i)
            logger.warn("Warning message %s" %i)
            logger.error("Error message %s" %i)
            time.sleep(1)




if __name__ == '__main__':
    #Se crea la instancia de la clase
    app = App()
    #define la instancia de la clase logging para generar la bitacora
    logger = logging.getLogger("demonioprueba log")
    logger.setLevel(logging.INFO)
    #Se define el forma del log
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler("/var/log/demonioprueba/demoniopruebas.log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    #Se ejecuta el demonio llamando al objeto app
    daemon_runner = runner.DaemonRunner(app)
    #Esto evita que el archivo log no se cierre durante la ejecución del demonio
    daemon_runner.daemon_context.files_preserve=[handler.stream]
    #Ejecuta el método run del objeto app
    daemon_runner.do_action()

