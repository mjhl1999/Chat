#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle
import codecs

class ClienteChat():

    def __init__ (self, nombre):
        self.nombre = nombre

    def crea_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
        return socket

    def conecta(self):
        self.socket.connect( ('localhost', 8810) )
        self.socket.send('El cliente', nombre, 'se ha conectado al servidor')

    def recibe(self):
        while True:
             msg = self.sock.recv(1024).decode('utf-8')
             print msg

    def envia(self, mensaje):
            try:
                msg = bytearray(mensaje,"utf8")
            except:
                print("El mensaje no es valido")
            self.socket.send(pickle.dumps(msg))

    def desconecta(self):
        while True:
			mensaje = input('->')
			if mensaje != 'salir':
				self.send_mensaje(mensaje)
			else:
				self.socket.close()
				sys.exit()

    def main():
        try:
            print 'Ingresa tu nombre de usuario: '
            usuario = raw_input()
            if (usuario == None or usuario == ""):
                raise ValueError()
            cliente = ClienteChat(usuario)
        except:
             print("Usuario no valido, intenta de nuevo.")
             sys.exit()
        try:
            cliente.crea_socket()
            cliente.conecta()
        except:
            print("Conexión rechazada, intente de nuevo,")
        while True:
            msg = raw_input
            hilo_envia = threading.Thread(cliente.envia_mensaje(mensaje)).start()
            hilo_recibe = threading.Thread(cliente.recibe_mensaje()).start()

    main()
