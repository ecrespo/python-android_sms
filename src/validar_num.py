#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Nombre: validar_num.py
Descripcion: Validar números de telefonos celulares de Venezuela.
Version: 0.2
Licencia: GPLv3
Copyright: Cenditel - Ernesto Crespo <ecrespo@gmail.com>
Autor: Ernesto Nadir Crespo Avila 
email: ecrespo@gmail.com

"""

import re, sys 

class validar(object):
	def __init__(self):
		pass


	def NumCel(self,numero):
		 if len(numero) == 11 and \
                ((re.search("041[2|4|6]\d\d\d\d\d\d\d",numero)) or \
                    (re.search("042[4|6]\d\d\d\d\d\d\d",numero))) :
            return True
        else:
            return False


    def NumFijo(self,numero):
    	pass

    	



