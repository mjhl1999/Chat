#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random
import threading
import pickle
import sys

class ClienteChat(object):

    def __init__ (self, nombre, estado, host, puerto):
        self.nombre = nombre
        self.estado = estado
        self.cliente = [nombre, estado]
        #creando y estableciendo conexion con el cliente
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((str(host), int(puerto)))
        #recibe un mensaje desde el sevidor que nos dice si nos hemos conectado
        respuesta = self.socket.recv(1024)
        print (respuesta)
        print self.cliente
        self.envia_mensaje(self.cliente)
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
				datos = self.socket.recv(1024)
				if data:
					print(pickle.loads(datos))
			except:
				pass

    def envia_mensaje(self, mensaje):
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
    #identificador = str(random.randint(1, 10000))
    #tripleta = (usuario, estado, identificador)
    cliente = ClienteChat(usuario, estado, host, port)
    #except:
    #    print ('Algo salio mal, intente de nuevo')
    #    sys.exit()

main()
