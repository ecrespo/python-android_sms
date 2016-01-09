#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: privilegios
Description: Modulo que permite la ejecución de comandos como root
Version:0.4
Licencia: GPLv3
Copyright: Copyright (C) 2011 Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com

"""


import os 
from os import popen
from commands import getstatusoutput


class Privilegio(object):
    """Clase privilegio que permite ejecutar comandos como root y permite agregar un usuario al sudo"""
    
    def __init__(self,usuario=None):
        """Constructor que toma un usuario a usar los privilegios"""
        self._usuario = usuario
        
    def __getattr__(self):
        """__getattr__ devuelve none"""
        return None

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self,usuario=None):
        self._usuario = usuario
    
    @staticmethod
    def ejecutar_comando_sudo(comando):
        """ejecuta un comando con privilegios usando sudo"""
	resultado = os.popen("sudo {0}".format(comando)).readlines()
    	return resultado

    @staticmethod
    def ejecutar_comando_root(comando):
        """Ejecutar comando en modo root"""
        resultado = getstatusoutput("{0}".format(comando))
        return resultado

    def ejecutar_comando(self,comando):
        """Ejecutar comando dependiendo si es su o sudo"""
        if self._usuario == None:
            self.ejecutar_comando_root(comando)
        else:
            self.ejecutar_comando_sudo(comando)

    



    def agregar_usuario_sudo(self):
        """Agrega el usuario a los sudoers"""
    	ejecutar("echo \"{0} ALL=(ALL) ALL\" >>  /etc/sudoers ".format(self._usuario))


    
    
if __name__ == "__main__":
    privilegio = Privilegio()
    print("{0}".format(privilegio.ejecutar_comando("adb devices")))
    