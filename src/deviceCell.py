#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: privilegios
Description: Modulo que permite detectar que el dispositivo este conectado y si no se reconfigura, adicionalmente pasa la informacion
del dispositivo (sólo para dispositivos android por medio de adb)

Version:0.5
License: GPLv3
Copyright: Copyright (C) Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
"""

#import config
from os import path,environ
from privilegios import Privilegio
from SOAPpy import SOAPServer
import sys 
from string import find 
class Cell(object):
    def __init__(self):
        """
        Se capturan los valores del archivo de configuracion y se asigna los valores a
        los datos del objeto Cell
        """
        
        self._estado = False
        self._usuario = environ["USERNAME"]
        self._privilegio = Privilegio(self._usuario) 
        
    def __getattr__(self):
        """Devuelve None de atributos que no existen"""
        return None 

    @property
    def usuario(self):
        """getter del usuario que esta ejecutando la aplicacion"""
        return self._usuario
    
    @usuario.setter
    def usuario(self,usuario):
        """se asigna un nuevo usuario"""
        self._usuario = usuario
        self._privilegio = Privilegio(self._usuario)


    def detectar_dispositivos(self):
        """Detecta los dispositivos android conectados al computador por medio de adb"""
        resultados = self._privilegio.ejecutar_comando("adb devices")
        lista_dispositivos = []
        if len(resultados[1].split("\n")) == 2:
            self._estado = False
            return {"estado":self._estado,"elementos":[]}
        elif len(resultados[1].split("\n")) > 2:
            for dispositivos in resultados[1].split("\n")[:-1]:
                if (find(dispositivos,"List")) <> -1:
                    pass
                else:
                    linea = dispositivos.split("\t")
                    estado_dispositivo = linea[-1]
                    dispositivo = linea[0]
                    if estado_dispositivo == u'offline':
                        estado = u"inactivo"
                    elif estado_dispositivo == u'device':
                        estado = u"activo"
                    else: 
                        estado = u"inactivo"
                    lista_dispositivos.append({"dispositivo":dispositivo,"estado":estado})
            self._estado = True
            return {"estado":self._estado,"elementos":lista_dispositivos}
        else:
            self._estado = False
            return {"estado":self._estado,"elementos":[]}





class Servicio(object):
    """Servicio soap para publicar si hay dispositivos o no conectados"""
    def __init__(self,host="localhost",port=8580):
        self._host = host
        self._port = port
        self._cell = Cell()
        self._server = SOAPServer((self._host, self._port))
        self._server.registerFunction(self._cell.detectar_dispositivos)

    def __getattr__(self):
        """devuelve none si se intenta acceder a un atributo que no existe"""
        return None


    @property
    def host(self):
        """getter del host"""
        return self._host
    
    @host.setter
    def host(self,host="localhost"):
        """setter del host"""
        self._host = host 

    @property
    def port(self):
        """getter del port"""
        return self._port
    
    @port.setter
    def post(self,port):
        """setter del puerto """
        self._port = port

    def iniciar(self):
        """Se inicia el servicio soap"""
        self._server.serve_forever()






if __name__ == "__main__":
    try:
        servicio = Servicio()
        servicio.iniciar()
    except KeyboardInterrupt:
        print(u"Finalizada la aplicación")
        sys.exit()
    
    #cell = Cell()
    #cell.detectar_dispositivos()
    #print("{0}".format(cell.detectar_dispositivos()))
