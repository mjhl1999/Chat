#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

class ServidorChat(object):

    def conecta(self, host, port):
        #crea nuevo socket
        self.socket = socket.socket()
        #establece conexión
        self.socket.bind( (host, port) )
        #establece cantidad de peticiones en cola que maneja el socket
        self.socket.listen(10)
        #lista que almacenara a los clientes
        clientes = []
        while True:
            #acceptando peticiones
            conexion, direccion = self.socket.accept()
            print "Nueva conexion establecida"
            conexion.send("Te has conectado al servidor")

        def desconecta():
            

def main():
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    servidor = ServidorChat()
    servidor.conecta(host, port)

main()
