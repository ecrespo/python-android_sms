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


class Privilegio(object):
    """Clase privilegio que permite ejecutar comandos como root y permite agregar un usuario al sudo"""
    
    def __init__(self,usuario):
        """Constructor que toma un usuario a usar los privilegios"""
        self._usuario = usuario

    def __getattr__(self):
        """__getattr__ devuelve none"""
        return None

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self,usuario):
        self._usuario = usuario
    


    @staticmethod
    def ejecutar_comando(comando):
        """ejecuta un comando con privilegios usando sudo"""
	resultado = os.popen("sudo {0}".format(comando)).readlines()
    	return resultado

    def agregar_usuario_sudo(self):
        """Agrega el usuario a los sudoers"""
    	ejecutar("echo \"{0} ALL=(ALL) ALL\" >>  /etc/sudoers ".format(self._usuario))


    
    
if __name__ == "__main__":
    privilegio = Privilegio("ernesto")
    print (privilegio.ejecutar_comando("adb devices"))
    print(privilegio.usuario)
    privilegio.usuario = "dayana"
    print(privilegio.usuario)
