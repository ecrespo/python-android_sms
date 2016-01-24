#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pySMScli: Cliente de linea de comandos para envio de SMS desde Linux con celular Android
License: GPLv3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
version: 0.1
"""



class app_cli(object):
    """Clase que genera la interaccion con el servidor de SMS"""

    def __init__(self):
        """COnstrucctor"""
        pass

    def multi_send(self,texto):
        numeros = texto.split(":")
        print(numeros)


def multi_send(texto):
    print (texto.split(":"))



if __name__ == "__main__":
    import argparse
    appcli = app_cli()
    parser = argparse.ArgumentParser(description=u'Procesa envío de sms')
    #envio = parser.add_mutually_exclusive_group(required=True)
    envio = parser.add_argument_group('envio')
    info = parser.add_argument_group('info')
    envio.add_argument('-m','--multi', type=str, dest="multi_nums", help=u'Envío de sms a multiples números celulares')
    envio.add_argument('-s','--single', type=str,dest="single_num",help=u'Envío de sms a un número celular')
    info.add_argument('-i','--info', action='store_false', help=u'Consulta información del celular')
    envio.add_argument('-e','--enviar',action='store_false', help=u'Envío del mensaje al número o números celulares')
    args = parser.parse_args()
    if args.multi_nums != None:
        print("~multi: {0}".format(args.multi_nums))
    else:
        print("~single: {0}".format(args.single_num))


