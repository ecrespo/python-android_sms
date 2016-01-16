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
    def __init__(self):
        """Asignacion de valores a los atributos de la clase"""
        #self._port = port
        #self._server = SOAPpy.SOAPProxy("http://localhost:8580/")
        self._validar = Validar()

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


    def sms_send(self,numero,mensaje):
        
        """EnviarMensaje: Metodo que permite enviar un mensaje de texto
        pasando el numero y el mensaje
        Maneja ambos casos conexion USB o por red wifi.
        """
        if self._validar.num_cel(numero) == False:
            print(u"Numero no valido")
            return {"estado": False}
        #Se crea la instancia del objeto Android dependiendo si es conexion
        #wifi se le pasa el host y el puerto
        #Si es conexion USB simplemente se crea la instancia
        droid = android.Android()
        #Enviando el mensaje de texto
        droid.smsSend(numero,mensaje)
        return {"estado":True}
    


    
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        numero = sys.argv[1]
        mensaje = sys.argv[2]
    else:
        print ("error enviando mensaje, se necesita pasar el numero y mensaje")
        sys.exit
    andr = sms()
    #print(andr.info_cel())
    resultado = andr.sms_send("04265746477","Epale Dhionel, es ernesto, avisa si llega es otro script 1")
    if resultado["estado"] == False:
        print("No se pudo configurar el ambiente para el envio")
    else:
        print("Mensaje enviado")

    #except socket.error:
    #   print("Error de conexion con el celular")
