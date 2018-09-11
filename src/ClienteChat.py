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

    def conecta(self):
        self.socket.connect( ('localhost', 8010) )
        self.socket.send('El cliente', nombre, 'se ha conectado al servidor y esta', estado)

    def recibe(self):
    	while True:
			try:
				msg = self.sock.recv(1024)
				if msg:
					print(pickle.loads(msg))
			except:
				pass

    def envia(self, msg):
        self.sock.send(pickle.dumps(msg))

    def desconecta(self):
        while True:
			mensaje = input('->')
			if mensaje != 'salir':
				self.send_mensaje(mensaje)
			else:
				self.socket.close()
				sys.exit()

    def cambia_estado(self, estado):
        self.estado = estado

    def ver_usuarios(self):
        pass

    def main():
        try:
            print 'Ingresa tu nombre de usuario: '
            usuario = raw_input()
            if (usuario == None or usuario == ""):
                raise ValueError()
            print 'Elige tu estado (ACTIVE, AWAY, BUSY)'
            estado = raw_input()
            if (estado != 'ACTIVE' or estado != 'AWAY' or estado != 'BUSY'):
                raise ValueError()
            cliente = ClienteChat(self, usuario, estado)
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
