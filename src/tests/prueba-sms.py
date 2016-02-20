#!/usr/bin/env python
# -*- coding: utf-8 -*-

import android

#Importando el módulo android,sys y re
import android,sys,re


#Función de envio de mensajes
def Enviomensaje():
    #Se averigua si se le pasa al script el número celular y el mensaje, y que el número sea válido para venezuela.
    if len(sys.argv) == 3:
        numero = sys.argv[1]
        mensaje = sys.argv[2]
    else:
        print ("error enviando mensaje, se necesita pasar el número y mensaje")
        sys.exit
    if Validar(numero) == 0:
        print (u"Número invalido")
        sys.exit
    #Creando la instancia droid del objeto Android
    droid = android.Android()
    #Enviando el mensaje de texto
    droid.smsSend(numero,mensaje)
    #Se presenta un mensaje de notificación en el celular.
    droid.makeToast('Mensaje enviado')


#Función que válida si el número es de movilnet, digitel o movistar.
def Validar(numero):
    #Valida si los numeros tienen 11 digitos y que sean de los proveedores movilnet, digitel y movistar
    if len(numero) == 11 and ((re.search("041[2|4|6]\d\d\d\d\d\d\d",numero)) or (re.search("042[4|6]\d\d\d\d\d\d\d",numero))) :
        return 1
    else:
        return 0
#Ejecución del programa.
if __name__ == "__main__":
    Enviomensaje()
