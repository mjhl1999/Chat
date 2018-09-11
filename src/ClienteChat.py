#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle
import codecs

class ClienteChat():

    def __init__ (self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def crea_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
        return socket

    def conecta(self, host, puerto):
        self.socket.connect( (host, puerto) )
        self.socket.send('El cliente', nombre, 'se ha conectado al servidor y esta', estado)


def main():
    try:
        print 'Ingresa tu nombre de usuario: '
        usuario = raw_input()
        if (usuario == None or usuario == ""):
            raise ValueError()
        print 'Elige tu estado (ACTIVE, AWAY, BUSY):'
        estado = raw_input()
        if (estado != "ACTIVE" or estado != "AWAY" or estado != "BUSY"):
            raise ValueError()
        cliente = ClienteChat(self, usuario, estado)
    except:
         print("Usuario no valido, intenta de nuevo.")
         sys.exit()

    try:
        print 'Ingresa el host:'
        host = raw_input()
        print 'Ingresa el puerto:'
        puerto = raw_input()
        cliente.crea_socket()
        cliente.conecta(host, puerto)
    except:
        print("Conexión rechazada, intente de nuevo,")

main()
