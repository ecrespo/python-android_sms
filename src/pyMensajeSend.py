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


class AndroidSms(object):
    """Clase que permite el envio de SMS solo por conexion USB"""
    def __init__(self,port,host="127.0.0.1"):
        
        """asignacion de los valores a los datos del objeto"""
        
        #Puerto es el numero de puerto asignado al servicio sl4a en el celular
        self._port = port
        #Host: es la IP asignada en la red wifi al celular
        self._host = host
        self._server = SOAPpy.SOAPProxy("http://localhost:8580/")
        self._privilegio = Privilegio()


        

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


    def __conf_ambiente_cel__(self):
        #Se apaga el servidor adb en el Linux
        self._privilegio.ejecutar_comando("adb kill-server")
        #Se borra las variables de entorno AP_PORT y AP_HOST
        self._privilegio.ejecutar_comando("export AP_PORT=\"\"")
        self._privilegio.ejecutar_comando("export AP_HOST=\"\"")
        self._privilegio.ejecutar_comando("adb devices")
        #Se inicia el servidor adb y se verifica que funciona correctamente
        r = self.__info_cel()
        if r["estado"] == False:
            print "Problemas con la configuracion del celular"
            return 0 
        elif r["estado"] == True:
            #El dispositivo esta activo
            #En este punto se tiene el dispositivo funcionando
            #Tanto por wifi como por usb.
            self._privilegio.ejecutar_comando("{0} forward tcp:9999 tcp:{1}")
            getstatusoutput("%s  forward tcp:9999 tcp:%s" %(self.__adb,self.__puerto))
        
        #Se crea la variable de entorno AP_PORT
        #para el caso conexion usb
        getstatusoutput("export AP_PORT=\"9999\"")
        return 1

    def SendSMS(self,numero,mensaje):
        
        """EnviarMensaje: Metodo que permite enviar un mensaje de texto
        pasando el numero y el mensaje
        Maneja ambos casos conexion USB o por red wifi.
        """
        if self.__ValidarNumero__(numero) == 0:
            print "Numero invalido"
            return 0 
        #Creando la instancia droid del objeto Android
        self.__ConfigAndroid__()
        #Se crea la instancia del objeto Android dependiendo si es conexion
        #wifi se le pasa el host y el puerto
        #Si es conexion USB simplemente se crea la instancia
        droid = android.Android((self.__host,self.__puerto))
        #Enviando el mensaje de texto
        droid.smsSend(numero,mensaje)
                

    
if __name__ == "__main__":
    #sms = Sms("/dev/ttyUSB0",19200)
    #sms.SendMensaje("numero","esta es una prueba")
    Android = AndroidSms("usb","42917")
    Android.EnvioSMS("04265673018","Hola Doris, es ernesto, avisame si te llega este sms.")
