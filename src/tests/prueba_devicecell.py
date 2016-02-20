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


class pDeviceCell:
	"""Clase que prueba el webservice SOAP"""
	def __init__(self):
		self._server = SOAPpy.SOAPProxy("http://localhost:8580/")

	def run(self):
		"""Ejecucion de la prueba"""
		self._resultado = self._server.detectar_dispositivos()
		if self._resultado["estado"] == True:
			print (self._resultado["dispositivo"])
	        print(self._server.agregar_forwarding(3390))
	        print(self._server.listar_forwarding())
	        print(self._server.remover_forwarding())
	        print(self._server.listar_forwarding())
	    else:
	    	print("Sin resultado")


if __name__ == '__main__':
	prueba = pDeviceCell()
	prueba.run()
	