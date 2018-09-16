#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random
import threading
import pickle
import sys

class ClienteChat(object):

    def __init__ (self, nombre, estado, host, port):
        	self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		self.socket.connect((str(host), int(port)))

    		recibe = threading.Thread(target=self.recibe)

    		recibe.daemon = True
    		recibe.start()

    		while True:
    			mensaje = raw_input('->')
    			if mensaje != "DISCONNECT":
    				self.envia(mensaje)
    			else:
    				self.socket.close()
    				sys.exit()
    def recibe(self):
		while True:
			try:
				data = self.socket.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

    def envia(self, mensaje):
		self.socket.send(pickle.dumps(mensaje))


def main():
    #try:
    print ('Ingresa tu nombre de usuario: ')
    usuario = raw_input()
    if (usuario == None or usuario == ""):
        raise ValueError()
        print 'Usuario Invalido'
    print ('Elige tu estado (ACTIVE, AWAY, BUSY):')
    estado = raw_input()
    if (estado != 'ACTIVE' and estado != "AWAY" and estado != "BUSY"):
        raise ValueError()
        print 'Estado Invalido'
    print 'Ingresa el host:'
    host = raw_input()
    print 'Ingresa el puerto:'
    port = input()
    cliente = ClienteChat(usuario, estado, host, port)
    #except:
        #print ('Algo salio mal, intente de nuevo')
        #sys.exit()

main()
