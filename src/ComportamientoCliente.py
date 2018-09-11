#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle

class ComportamientoCliente():

    def conecta(self, host, puerto):
        self.socket.connect( (host, puerto) )
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

    while True:
        msg = raw_input()
        hilo_envia = threading.Thread(cliente.envia_mensaje(mensaje)).start()
        hilo_recibe = threading.Thread(cliente.recibe_mensaje()).start()

main()
