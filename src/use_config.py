#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser

"""
Nombre: use_config
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Ernesto Crespo
Correo: ecrespo@gmail.com
Licencia: GPL Version 3
Copyright: Copyright (C) 2010 Distrito Socialista Tecnologico AIT PDVSA  Merida
Version: 0.1

"""

#Clase config
class config:

    def __init__(self, cnffile):
        self.__cnffile = cnffile
        self.__config = ConfigParser()
        self.__config.read(self.__cnffile)

#Se define la funcion que muestra los item de una seccion
    def ShowItemSection(self, section):
        return self.__config.items(section)

#Se muestra el valor de los item
    def ShowValueItem(self, section, option):
        return self.__config.get(section, option)

#Se cambia el valor de la opcion
    def change(self, section, option, value):
        self.__config.set(section, option, value)

#Se escribe al archivo de configuracion
    def write(self):
        self.__config.write(open(self.__cnffile,'w'))



