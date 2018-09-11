#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle
from Comportamiento import Comportamiento

class ServidorChat():

    def __init__(self, host=sys.argv[1], port=sys.argv[2]):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(10)
        clientes = []

    def crea_hilo(self):
        while True:
            try:
                conexion, direccion = self.socket.accept()
                hilo = threading.Thread(self.envia_mensaje()).start()
            except:
                sys.exit()

def main():
    servidor = ServidorChat()
    while True:
        try:
            conectar = threading.Thread(target=servidor.conectar()).start()
            Comportamiento.procesar = threading.Thread(target=servidor.procesar()).start()

            conectar.daemon = True
            conectar.start()

            Comportamiento.procesar.daemon = True
            Comportamiento.procesar.start()
        except:
            print 'Algo salio mal'
            servidor.desconecta()
            sys.exit()

main()
