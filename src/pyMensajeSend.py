#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pySMS_cliente: Servidor que envie sms conectadose al celular
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
        self._cliente = SOAPpy.SOAPProxy("http://localhost:8580/")

        self._validar = Validar()

    def __getattr__(self):
        return None
    

    def _ajustar_conf(self):
        """Permite ajustar la configuracion por medio de adb"""
        resultado = self._cliente.detectar_dispositivos()
        if resultado["estado"] == False: return {"estado":False}
        self._cliente.remover_forwarding()
        resultado = self._cliente.agregar_forwarding(self._port)
        return {"estado":resultado["estado"]}


    def info_cel(self):
        """
        Se verifica si el dispositivo existe.
        si no se levanta el dispositivo.
        """
        resultado = self._cliente.detectar_dispositivos()
        if resultado["estado"] == True:
            return resultado["dispositivo"]
        else:
            return {"dispositivos":[],"estado":False}





    def sms_send(self,port_android,numero,mensaje):
        
        """EnviarMensaje: Metodo que permite enviar un mensaje de texto
        pasando el numero y el mensaje
        Maneja ambos casos conexion USB o por red wifi.
        """
        if self._validar.num_cel(numero) == False:
            print(u"Numero no valido")
            return {"estado": False}
        resultado = self._ajustar_conf()
        if resultado["estado"] == False: return {"estado": False}
        droid = android.Android()
        #Enviando el mensaje de texto
        droid.smsSend(numero,mensaje)
        return {"estado":True}
    


    
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        port = sys.argv[1]
        numero = sys.argv[2]
        mensaje = sys.argv[3]
    else:
        print ("error enviando mensaje, se necesita pasar el puerto, numero y mensaje")
        sys.exit
    andr = sms()
    #print(andr.info_cel())
    resultado = andr.sms_send(port,numero,mensaje)
    if resultado["estado"] == False:
        print("No se pudo configurar el ambiente para el envio")
    else:
        print("Mensaje enviado")

    #except socket.error:
    #   print("Error de conexion con el celular")
