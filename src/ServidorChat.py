#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle
from Comportamiento import Comportamiento

class ServidorChat():

    #(self, host = sys.argv[1], port = sys.argv[2])
    def __init__(self):
        #crea nuevo socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #establece conexión
        self.socket.bind(('localhost', 8761))
        #establece cantidad de peticiones en cola que maneja el socket
        self.socket.listen(10)
        #lista que almacenara a los clientes
        clientes = []

    def crea_hilo(self):
        while True:
            try:
                #acceptando peticiones
                conexion, direccion = self.socket.accept()
                print "Nueva conexion establecida"
                hilo = threading.Thread(self.envia_mensaje()).start()
            except:
                sys.exit()

    def desconecta(self):
        mensaje = input('->')
        if mensaje == 'salir':
            for cliente in self.clientes:
                cliente.close()
            self.socket.close()
            sys.exit()
        else:
            pass

servidor = ServidorChat()
servidor.crea_hilo()
servidor.desconecta()

"""
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
"""
# main()
