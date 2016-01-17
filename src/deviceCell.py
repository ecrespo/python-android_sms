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
from string import find,join 
from SOAPpy import SOAPServer
from commands import getstatusoutput



class Cell(object):
    def __init__(self,port):
        """
        Se capturan los valores del archivo de configuracion y se asigna los valores a
        los datos del objeto Cell
        """
        self._port = port

    @property
    def port(self):
        """getter del puerto"""
        return self._port
    
    @port.setter
    def port(self,port):
        """Setter del puerto"""
        self._port = port
        
    def __getattr__(self):
        """Devuelve None de atributos que no existen"""
        return None 

    def detener_servicio(self):
        """Detiene el servicio de adb"""
        resultado = getstatusoutput("adb kill-server")
        if resultado[0] == 0:
            return {"estado":True}
        else:
            return {"estado": False}

    def iniciar_servicio(self):
        """Inicia el servicio de adb"""
        resultado = getstatusoutput("adb start-server")
        if resultado[0] == 0:
            return {"estado":True}
        else:
            return {"estado": False}



    def listar_forwarding(self):
        """listar el port forwarding de adb"""
        detectar = self.detectar_dispositivos()
        if detectar["estado"] == False: return {"estado":False}
        resultados = getstatusoutput("adb forward --list")
        if resultados[0] == 0:
            return {"estado": True, "resultado": resultados[1]}
        else:
            return {"estado":False}

    def remover_forwarding(self):
        """Remover el port forwarding de adb"""
        detectar = self.detectar_dispositivos()
        if detectar["estado"] == False: return {"estado":False}
        resultado = getstatusoutput("adb forward --remove-all")
        if resultado[0] == 0:
            return {"estado": True}
        else:
            return {"estado": False}

    def agregar_forwarding(self,puerto):
        self._port= puerto
        """Agregar puerto para port forwarding"""
        detectar = self.detectar_dispositivos()
        if detectar["estado"] == False: return {"estado":False}
        resultado = getstatusoutput("adb forward tcp:9999 tcp:{0}".format(self._port))
        if resultado[0] == 0:
            return {"estado": True}
        else:
            return {"estado": False}


    def detectar_dispositivos(self):
        """Detecta los dispositivos android conectados al computador por medio de adb"""
        resultado = getstatusoutput("adb get-state")
        if resultado[1] == "unknown": return {"estado": False}
        resultados = getstatusoutput("adb devices -l")
        lista = resultados[1].split("\n")[1].split(" ")
        lista_dispositivos = []
        datos = {}
        datos["id"] = lista[0]
        datos["device"] = lista[7]
        datos["producto"] = lista[9].split(":")[-1]
        arreglo = lista[10].split(":")[-1].split("_")
        texto =  join(arreglo," ")
        datos["modelo"] = texto
        return {"estado": True, "dispositivo":datos}
        








if __name__ == "__main__":
    try:
        cell = Cell()
        #print(cell.detectar_dispositivos())
        #print(cell.agregar_forwarding(3390))
        #print(cell.listar_forwarding())
        #print(cell.remover_forwarding())
        #print(cell.listar_forwarding())
        server = SOAPServer(("localhost",8580))
        server.registerFunction(cell.detectar_dispositivos)
        server.registerFunction(cell.listar_forwarding)
        server.registerFunction(cell.remover_forwarding)
        server.registerFunction(cell.agregar_forwarding)
        server.registerFunction(cell.detener_servicio)
        server.registerFunction(cell.iniciar_servicio)
        server.serve_forever()
        
    except KeyboardInterrupt:
        print(u"Finalizada la aplicación")
        sys.exit()
