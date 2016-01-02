#!/usr/bin/env python3
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

class Validar(object):

    def __init__(self):
		pass

    @staticmethod
    def num_cel(num):
        if ((len(num) == 11) and (re.search("041[2|4|6]\d\d\d\d\d\d\d",num) or re.search("042[4|6]\d\d\d\d\d\d\d",num))):
            return True
        else:
            return False


    	

if __name__ == '__main__':
    validar = Validar()
    print(validar.num_cel("04265673018"))
    print(validar.num_cel("04277338282"))

