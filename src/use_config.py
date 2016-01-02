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
    """Clase Config: facilita el uso del modulo ConfigParser"""

    def __init__(self, cnffile):
        """Constructor toma el archivo de configuracion e inicializa ConfigParser"""
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)


#
    def ShowItemSection(self, section):
        """Se define la funcion que muestra los item de una seccion"""
        return self._config.items(section)

#
    def ShowValueItem(self, section, option):
        """Se muestra el valor de los item"""
        return self._config.get(section, option)

#
    def change(self, section, option, value):
        """Se cambia el valor de la opcion"""
        self._config.set(section, option, value)

#
    def write(self):
        """Se escribe al archivo de configuracion"""
        self._config.write(open(self._cnffile,'w'))



if __name__ == '__main__':
    configuracion = Config("./conf/androidsms.conf")
    print(configuracion.ShowItemSection("server"))
    print(configuracion.ShowValueItem("server","ip"))