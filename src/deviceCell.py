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
from string import find 
from SOAPpy import SOAPServer
from commands import getstatusoutput

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
        resultados = getstatusoutput("adb devices")
        lista_dispositivos = []
        if resultados == None: return {"estado": False}
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
                        estado = False
                    elif estado_dispositivo == u'device':
                        estado = True
                    else: 
                        estado = False
                    lista_dispositivos.append({"dispositivo":dispositivo,"estado":estado})
            self._estado = True
            return {"estado":self._estado,"elementos":lista_dispositivos}
        else:
            self._estado = False
            return {"estado":self._estado,"elementos":[]}









if __name__ == "__main__":
    try:
        cell = Cell()
        #print(cell.detectar_dispositivos())
        server = SOAPServer(("localhost",8580))
        server.registerFunction(cell.detectar_dispositivos)
        server.serve_forever()
        
    except KeyboardInterrupt:
        print(u"Finalizada la aplicación")
        sys.exit()
