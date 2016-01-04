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
from os import path
from privilegios import ejecutar, AgregarUsuarioSudo
from commands import getstatusoutput


class Cell(object):
    def __init__(self,archivo_conf):
        """
        Se capturan los valores del archivo de configuracion y se asigna los valores a
        los datos del objeto Cell
        """
        self.__archivo_conf = archivo_conf
        self.__estado = False
        
    def __getattr__(self):
        """Devuelve None de atributos que no existen"""
        return None 

    @property
    def archivo_conf(self):
        """property de gettter"""
        return self._archivo_conf

    @archivo_conf.setter
    def archivo_conf(self,archivo_conf):
        """property de setter"""
        self.__archivo_conf = archivo_conf
        self.__estado = False

        
    
    def detectar_dispositivos(self):
        """Detecta los dispositivos android conectados al computador por medio de adb"""
        resultados = ejecutar("adb devices")
        self.__lista_dispositivos = []
        if len(resultados) == 2:
            self.__estado = False
            return False
        elif len(resultados) > 2:
            for dispositivos in resultados[1:-1]:
                dispositivo = dispositivos[:-1].split("\t")[0]
                estado_dispositivo = dispositivos[:-1].split("\t")[1]
                if estado_dispositivo == u'device':
                    estado_dispositivo = u'activo'
                else:
                    estado_dispositivo = u'inactivo'
                self.__lista_dispositivos.append({"dispositivo": dispositivo,"estado": estado_dispositivo})
            self.__estado = True
            return self.__lista_dispositivos
        else:
            self.__estado = False
            return False

            

if __name__ == "__main__":
    
    cel = Cell(".../conf/config-sms.conf")
    print "Deteccion de dispositivo",cel.detectarDispositivos()
    cel.guardar_dispositivo()
    cel.leer_dispositivos()
    