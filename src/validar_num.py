#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Validar números de telefonos"

import re, sys 

class validar:
	def __init__(self):
		pass


	def NumCel(self,numero):
		 if len(numero) == 11 and ((re.search("041[2|4|6]\d\d\d\d\d\d\d",numero)) or (re.search("042[4|6]\d\d\d\d\d\d\d",numero))) :
            return True
        else:
            return False


    def NumFijo(self,numero):
    	pass

    	



