#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: privilegios
Description: Modulo que permite la ejecución de comandos como root
Version:0.3
License: GPLv3
Copyright: Copyright (C) 2011 Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com

"""


import os 
import gobject
import getpass
from commands import getstatusoutput


def ask_pass_func(context, prompt):
    try:
        return getpass.getpass("Escriba la clave de administrador (root): ")
    except KeyboardInterrupt:
        print
        err = gobject.GError("keyboard interrupt")
        
        raise err

def ejecutar(comando):
    resultado = os.popen("sudo %s" %comando).readlines()
    return resultado


def AgregarUsuarioSudo(usuario):
    ejecutar("echo \"%s ALL=(ALL) ALL\" >>  /etc/sudoers " %usuario)
    

    
    
if __name__ == "__main__":
    print ejecutar("adb devices")
