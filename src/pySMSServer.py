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
from commands import getstatusoutput
from deviceCell import Cell
import android




class AndroidSMS:
    def __init__(self,conexion,puerto,host="127.0.0.1"):
        #asignacion de los valores a los datos del objeto.
        #conexion: usb|wifi
        self.__conexion = conexion
        #Puerto es el numero de puerto asignado al servicio sl4a en el celular
        self.__puerto = puerto
        #Host: es la IP asignada en la red wifi al celular
        self.__host = host
        #Se define la ruta del programa adb, esta ruta se encuentra en
        #el archivo de configuracion config-sms.conf.
        #crear instancia cel con el tipo de celular, archivo de conf y tipo
        #de conexion
        self.__cel = Cel("android","./config-sms.conf",self.__conexion)
        self.__adb = self.__cel.InformacionDispositivo()[2]
        
    
    def __VerificarCel__(self):
        """
        Se verifica si el dispositivo existe.
        si no se levanta el dispositivo.
        """
        if self.__cel.DispositivoNoExiste() == 0 :
            return 1
        else:
            resultado = self.__cel.LevantarDispositivo()
            if resultado == 0:
                return 0
            else:
                return 1
    
    def __confAmbienteCel__(self):
        #Se apaga el servidor adb en el Linux
        getstatusoutput("%s kill-server" %self.__adb)
        #Se borra las variables de entorno AP_PORT y AP_HOST
        getstatusoutput("export AP_PORT=\"\"")
        getstatusoutput("export AP_HOST=\"\"")
        #Se inicia el servidor adb y se verifica que funciona correctamente
        r = getstatusoutput("%s devices" %self.__adb)
        if r[0] <> 0:
            print "Problemas con la configuracion del celular"
            return 0 
        else:
            if self.__conexion == "usb":
                #Se verifica que el dispositivo aparece identificado
                if r[1].split("\n")[1] == "":
                    print "NO hay un celular conectado"
                    return 0 
        #En este punto se tiene el dispositivo funcionando
        #Tanto por wifi como por usb.
        getstatusoutput("%s  forward tcp:9999 tcp:%s" %(self.__adb,self.__puerto))
        if self.__conexion == "wifi":
            #Se crean las variables de entorno AP_PORT y AP_HOST
            #para el caso de wifi
            getstatusoutput("export AP_PORT=%s" %self.__puerto)
            getstatusoutput("export AP_HOST=%s" %self.__host)
        elif self.__conexion == "usb":
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
                

class CellSMS:
    def __init__(self,tipoCell,conexion="",puerto="",host="",dispositivo="",baudios=""):
        self.__tipoCell = tipoCell
        self.__conexion = conexion
        self.__puerto = puerto
        self.__host = host
        self.__dispositivo = dispositivo
        self.__baudios = baudios
        if self.__tipoCell == "v9":
            self.__celV9 = V9SMS(self.__dispositivo,self.__baudios)
        elif self.__tipoCell == "android":
            self.__celAndroid = AndroidSMS(self.__conexion,self.__puerto,self.__host)
    
    def SendSMS(mensaje="",numero=""):
        if self.__tipoCell == "v9":
            self.__celV9.SendSMS(mensaje,numero)
        elif self.__tipoCell == "android":
            self.__celAndroid.SendSMS(mensaje,numero)
            
    
if __name__ == "__main__":
    #sms = Sms("/dev/ttyUSB0",19200)
    #sms.SendMensaje("numero","esta es una prueba")
    Android = AndroidSms("usb","42917")
    Android.EnvioSMS("04265673018","Hola Doris, es ernesto, avisame si te llega este sms.")
