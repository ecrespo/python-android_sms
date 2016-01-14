#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
pySMS_server: Servidor que envie sms conectadose al celular
License: GPLv3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
version: 0.5
"""
from deviceCell import Cell
import android

import SOAPpy
from privilegios import Privilegio
from validar_num import Validar 
from commands import getstatusoutput
import os 
import socket

class sms(object):
    """Clase que permite el envio de sms por conexion USB a celular Android"""
    def __init__(self,port):
        """Asignacion de valores a los atributos de la clase"""
        self._port = port
        self._server = SOAPpy.SOAPProxy("http://localhost:8580/")
        self._validar = Validar()

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self,port):
        self._port = port 

    def __getattr__(self):
        return None
    
    def info_cel(self):
        """
        Se verifica si el dispositivo existe.
        si no se levanta el dispositivo.
        """
        resultado = self._server.detectar_dispositivos()
        if resultado["estado"] == True:
            return {"dispositivos":resultado["elementos"][0]["dispositivo"],"estado":resultado["elementos"][0]["estado"]}
        else:
            return {"dispositivos":[],"estado":False}


    def conf_ambiente_cel(self):
        """Iniciando configuracion de ambiente"""
        #Se apaga el servidor adb en el Linux
        print(getstatusoutput("sudo adb kill-server"))
        #Se borra las variables de entorno AP_PORT y AP_HOST
        os.environ["AP_PORT"] = ""
        #Se inicia el servidor adb y se verifica que funciona correctamente
        r = self.info_cel()
        print(r)
        if r["estado"] == False:
            return {"estado":False,"mensaje":"Problemas con la configuracion del celular"}
        elif r["estado"] == True:
            #El dispositivo esta activo
            #En este punto se tiene el dispositivo funcionando
            print(getstatusoutput("sudo adb devices"))
            print(getstatusoutput("sudo adb forward tcp:9999 tcp:{0}".format(self._port)))
            #Se crea la variable de entorno AP_PORT
            #para el caso conexion usb
            os.environ["AP_PORT"] = "9999"
            print(os.environ["AP_PORT"])
            return {"estado":True}
        


    def sms_send(self,numero,mensaje):
        
        """EnviarMensaje: Metodo que permite enviar un mensaje de texto
        pasando el numero y el mensaje
        Maneja ambos casos conexion USB o por red wifi.
        """
        print("envio")
        if self._validar.num_cel(numero) == False:
            print("Celular no conectado")
            return {"estado": False}
        resultado = self.conf_ambiente_cel()
        #Se crea la instancia del objeto Android dependiendo si es conexion
        #wifi se le pasa el host y el puerto
        #Si es conexion USB simplemente se crea la instancia
        if resultado["estado"] == False:
            return {"estado":"False"}
        else:
            droid = android.Android()
            #Enviando el mensaje de texto
            droid.smsSend(numero,mensaje)
            return {"estado":True}
                

    
if __name__ == "__main__":
    andr = sms("50097")
    #print(andr.info_cel())
    resultado = andr.sms_send("04140447060","Epale Hector, es ernesto, avisa si llega es otro script 1")
    if resultado["estado"] == False:
        print("No se pudo configurar el ambiente para el envio")
    else:
        print("Mensaje enviado")

    #except socket.error:
    #   print("Error de conexion con el celular")