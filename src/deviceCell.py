#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: privilegios
Description: Modulo que permite detectar que el dispositivo este conectado y si no se reconfigura, adicionalmente pasa la informacion
del dispositivo (sólo para dispositivos android por medio de adb)

Version:0.3
License: GPLv3
Copyright: Copyright (C) Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
"""

#import config
from os import path
from privilegios import ejecutar, AgregarUsuarioSudo
from commands import getstatusoutput
from bson import BSON
import bson

class Cell(object):
    def __init__(self,celular,configuracion,conexion):
        """
        Se capturan los valores del archivo de configuracion y se asigna los valores a
        los datos del objeto Cell
        """
        self.__celular = celular
        #self.__configparser = config.config(configuracion)
        #self.__conexionAndroid = conexion
        #if self.__celular == "android":
        #    self.__adb = self.__configparser.ShowValueItem("android","ruta_adb")
        #elif celular == "v9":
        #    self.__dispositivo = self.__configparser.ShowValueItem("dispositivo","dispositivo")
        #    self.__baudios = self.__configparser.ShowValueItem("dispositivo","baudios")
        self.__estado = False
        
        
    def DispositivoNoExiste(self):
        """Si el dispositivo no existe devuelve 1
        si existe devuelve 0
        """
        if self.__celular == "v9":
            if not (path.isfile(self.__dispositivo)):
                return 1
            else:
                return 0
        elif self.__celular == "android" and self.__conexionAndroid == "usb":
            from commands import getstatusoutput
            r = getstatusoutput("%s devices" %self.__adb)
            if r[0] == 0:
                #Se inicio el dispositivo sin problemas
                l = r[1].split("\n")
                if l[1] <> '':
                    return 0
                else:
                    return 1
            else:
                return 1
        elif self.__celular == "android" and self.__conexionAndroid == "wifi":
            return 1
        
    
            
    def guardarDispositivo(self,archivobson):
        """
        Se guarda el estado de los dispositivos android en una tabla
        """
        if self.__estado == False: return False
        listaDispositivos = self.detectarDispositivos()
        f = open(archivobson, 'a+')
        try:
            for dispositivo in listaDispositivos:
                f.write(BSON.encode(dispositivo))
        finally:
            f.close()

    def leerDispositivos(self,archivobson):
        if self.__estado == False: return False
        f = open(archivobson, 'rb')
        result = bson.decode_all(f.read())
        print result


        
        
    
    def detectarDispositivos(self):
        resultados = ejecutar("adb devices")
        self.listaDispositivos = []
        if len(resultados) == 2:
            self.__estado = False
            return False
        elif len(resultados) > 2:
            for dispositivos in resultados[1:-1]:
                dispositivo = dispositivos[:-1].split("\t")[0]
                estadoDispositivo = dispositivos[:-1].split("\t")[1]
                if estadoDispositivo == u'device':
                    estadoDispositivo = u'activo'
                else:
                    estadoDispositivo = u'inactivo'
                self.listaDispositivos.append({"dispositivo": dispositivo,"estado": estadoDispositivo})
            self.__estado = True
            return self.listaDispositivos
        else:
            self.__estado = False
            return False

        print resultados
            

if __name__ == "__main__":
    
    cel = Cell("android","./config-sms.conf","usb")
    print "Deteccion de dispositivo",cel.detectarDispositivos()
    cel.guardarDispositivo("dispositivos.bson")
    cel.leerDispositivos("dispositivos.bson")
    """
    print "iniciando la deteccion"
    if cel.DispositivoNoExiste() == 0 :
        print "El dispositivo existe:",cel.InformacionDispositivo()
    else:
        print "levantando el dispositivo"
        resultado = cel.LevantarDispositivo()
        if resultado == 0:
            print "no se pudo detectar el dispositivo android"
        else:
            print "El dispositivo existe:",cel.InformacionDispositivo()
    """
