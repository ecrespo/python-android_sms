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
from privilegios import Privilegios
from commands import getstatusoutput


class Cell(object):
    def __init__(self):
        """
        Se capturan los valores del archivo de configuracion y se asigna los valores a
        los datos del objeto Cell
        """
        
        self._estado = False
        self._usuario = environ["USERNAME"]
        self._privilegio = Privilegios(self._usuario) 
        
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
        self._privilegio = Privilegios(self._usuario)


    def detectar_dispositivos(self):
        """Detecta los dispositivos android conectados al computador por medio de adb"""
        resultados = self._privilegio.ejecutar("adb devices")
        self._lista_dispositivos = []
        if len(resultados) == 2:
            self._estado = False
            return {"estado":self._estado,"elementos":[]}
        elif len(resultados) > 2:
            for dispositivos in resultados[1:-1]:
                dispositivo = dispositivos[:-1].split("\t")[0]
                estado_dispositivo = dispositivos[:-1].split("\t")[1]
                if estado_dispositivo == u'device':
                    estado_dispositivo = u'activo'
                else:
                    estado_dispositivo = u'inactivo'
                self._lista_dispositivos.append({"dispositivo": dispositivo,"estado": estado_dispositivo})
            self._estado = True
            return {"estado":self._estado,"elementos":self.__lista_dispositivos}
        else:
            self._estado = False
            return {"estado":self._estado,"elementos":[]}

    

if __name__ == "__main__":
    
    cel = Cell()
    print "Deteccion de dispositivo",cel.detectarDispositivos()
    cel.guardar_dispositivo()
    cel.leer_dispositivos()
    