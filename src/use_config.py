#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser

"""
Nombre: use_config
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Ernesto Crespo
Correo: ecrespo@gmail.com
Licencia: GPL Version 3
Copyright: Copyright (C) 2016 Cenditel Merida
Version: 0.2

"""

#Clase config
class Config(object):

    def __init__(self, cnffile):
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)


#Se define la funcion que muestra los item de una seccion
    def ShowItemSection(self, section):
        return self._config.items(section)

#Se muestra el valor de los item
    def ShowValueItem(self, section, option):
        return self._config.get(section, option)

#Se cambia el valor de la opcion
    def change(self, section, option, value):
        self._config.set(section, option, value)

#Se escribe al archivo de configuracion
    def write(self):
        self._config.write(open(self._cnffile,'w'))



if __name__ == '__main__':
    configuracion = Config("./conf/androidsms.conf")
    print(configuracion.ShowItemSection("server"))
    print(configuracion.ShowValueItem("server","ip"))