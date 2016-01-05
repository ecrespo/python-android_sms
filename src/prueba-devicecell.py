#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: prueba-devicecell.py
Description: Script de prueba para el script de devicecell.py

Version:0.1
License: GPLv3
Copyright: Copyright (C) Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
"""

#!/usr/bin/env python

#Se importa el modulo SOAPpy
import SOAPpy

#Se crea la instancia del proxy SOAP 
#a el servidor SOAP 
server = SOAPpy.SOAPProxy("http://localhost:8580/")

#Se llama las funciones registradas en el servidor SOAP
resultado = server.detectar_dispositivos()
if resultado["estado"] == True:
	print ("dispositivo: {0}, estado: {1}".format(resultado["elementos"][0]["dispositivo"],resultado["elementos"][0]["estado"]))
else:
	print("Sin resultado")