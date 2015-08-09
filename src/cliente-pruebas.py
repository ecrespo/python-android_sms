#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importan los modulos haslib,json y SOAPpy
import hashlib
import json
import SOAPpy


#Se crea la instancia del proxy SOAP
#a el servidor SOAP
server = SOAPpy.SOAPProxy("http://localhost:8080/")

#Se define un diccionario con la informacion del mensaje.
dato = {"mensaje" : "Esta es una prueba de envio de sms",
        "numeros":('04125672538','04165273538','04262673538','04145273538','04245273538'),
        "cantnumeros" :5,
        "evento":8
        }

#Se codifica en json
codificado = json.dumps(dato)

#Se instancia md5
m = hashlib.md5()

#Se codifica con sha224
hash = hashlib.sha224(codificado).hexdigest()
#Se envia los datos
print "El resultado es: ", server.recepcion(codificado,hash)



