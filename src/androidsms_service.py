#!/usr/bin/env python
# -*- coding: utf-8 -*-

#libreria estándar loggin y time
import logging
from time import sleep
from daemon import runner
from use_config import config
import SOAPpy
import hashlib
import json
from server_zmq import ServZmq
def suma(a,b):
    suma = a+b
    logger.info("Suma %s" %suma)
    return suma


def recepcion(datos,verificacion):
    m = hashlib.md5()
    if hashlib.sha224(datos).hexdigest() != verificacion:
        logger.warn("Datos no son correctos %s,%s" %(datos,verificacion))
        return -1
    else:
        logger.info("Datos recibidos correctamente %s" %datos)
    diccionario = json.loads(datos)
    mensaje = diccionario['mensaje']
    numeros = diccionario['numeros']
    cantnumeros = int(diccionario['cantnumeros'])
    evento = diccionario['evento']
    if cantnumeros != len(numeros):
        logger.warn("Cantidad de numeros incorrecta %s" %cantnumeros)
        return -1
    else:
        logger.info(u"Cantidad de números correcta. %s" %cantnumeros)




class App():
    def __init__(self,fileconf):
        configuracion = config(fileconf)
        self.stdin_path =  configuracion.ShowValueItem("paths","stdin_path")
        self.stdout_path = configuracion.ShowValueItem("paths","stdout_path")
        self.stderr_path = configuracion.ShowValueItem("paths","stderr_path")
        #Se define la ruta del archivo pid del demonio.
        self.pidfile_path =  configuracion.ShowValueItem("paths","pidfile_path")
        self.pidfile_timeout = int(configuracion.ShowValueItem("time","pidfile_timeout"))



    def run(self):
        self.__serversoap = SOAPpy.SOAPServer(("localhost", 8080))
        self.__serversoap.registerFunction(suma)
        self.__serversoap.registerFunction(recepcion)
        self.__serversoap.serve_forever()
        self.__zmq = ServZmq("127.0.0.1", 5050)
        self.__zmq.run()
        """"
            #Diferentes niveles de registro de bitacora
            logger.debug("Debug message %s" %i)
            logger.info("Info message %s" %i)
            logger.warn("Warning message %s" %i)
            logger.error("Error message %s" %i)

"""




#Se crea la instancia de la clase
fileconfig = "/home/ernesto/proyectos/python-androidsms/python-android_sms/conf/androidsms.conf"
app = App(fileconfig)
#define la instancia de la clase logging para generar la bitacora
logger = logging.getLogger("androidsms log")
logger.setLevel(logging.INFO)
#Se define el forma del log
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(config(fileconfig).ShowValueItem("paths","log_path"))
handler.setFormatter(formatter)
logger.addHandler(handler)





#Se ejecuta el demonio llamando al objeto app
daemon_runner = runner.DaemonRunner(app)
#Esto evita que el archivo log no se cierre durante la ejecución del demonio
daemon_runner.daemon_context.files_preserve=[handler.stream]
#Ejecuta el método run del objeto app
daemon_runner.do_action()