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




if __name__ == "__main__":
    import argparse
    appcli = app_cli()
    parser = argparse.ArgumentParser(description=u'Procesa envío de sms')
    parser.add_argument('-m','--multi', type=str, help=u'Envío de sms a multiples números celulares')
    parser.add_argument('-s','--single', type=int,help=u'Envío de sms a un número celular')
    parser.add_argument('-i','--info', default=" ",type=str, help=u'Consulta información del celular')
    parser.add_argument('-e','--enviar', help=u'Envío del mensaje al número o números celulares')
    args = parser.parse_args()
    print(args.accumulate(args.integers))


