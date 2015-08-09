#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

#Importar zmq
import zmq


class ServZmq:

    def __init__(self,ip,puerto):
        self.__ip = ip
        self.__puerto = puerto
        self.__context = zmq.Contest()
        self.__socket = self.__context.socket(zmq.PAIR)
        self.__socket.bind("tcp://%s:%s" %(self.__ip,self.__puerto))

    def run(self):
        try:
            while True:
                mensaje = self.__socket.recv()
                print mensaje
                self.__socket.send("Recibido")


