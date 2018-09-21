#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random
import threading
import sys

class ClienteChat(object):

    def __init__ (self,host, puerto):
        self.nombre = ''
        self.estado = ''
        #creando y estableciendo conexion con el cliente
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((str(host), int(puerto)))
        #recibe un mensaje desde el sevidor que nos dice si nos hemos conectado
        respuesta = self.socket.recv(1024)
        print (respuesta)
        mensaje = threading.Thread(target=self.mensaje_recibido)
        mensaje.daemon = True
        mensaje.start()
        while True:
			mensaje = raw_input()
			if mensaje != 'DISCONNECT':
				self.envia_mensaje(mensaje)
			else:
				self.socket.close()
				sys.exit()

    def mensaje_recibido(self):
		while True:
			try:
				data = self.socket.recv(1024).encode('UTF-8')
				if data:
					print(data)
			except:
				pass

    def envia_mensaje(self, mensaje):
		self.socket.send(mensaje.encode('UTF-8'))

def main():
    #try:
    """print ('Ingresa tu nombre de usuario: ')
    usuario = raw_input()
    if (usuario == None or usuario == ""):
        raise ValueError()
        print 'Usuario Invalido'
    print ('Elige tu estado (ACTIVE, AWAY, BUSY):')
    estado = raw_input()
    if (estado != 'ACTIVE' and estado != "AWAY" and estado != "BUSY"):
        raise ValueError()
        print 'Estado Invalido' """
    #print 'Ingresa el host:'
    #host = raw_input()
    print 'Ingresa el puerto:'
    port = input()
        #identificador = str(random.randint(1, 10000))
        #tripleta = (usuario, estado, identificador)
    cliente = ClienteChat('localhost', port)
    #except:
     #  print ('Algo salio mal, intente de nuevo')
      # sys.exit()

main()
