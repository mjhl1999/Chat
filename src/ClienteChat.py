#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle

def crea_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
        return socket

def conecta(self):
    self.socket.connect( ('localhost', 8800) )
    socket.send('Me he conectado al servidor')

def recibe(self):
    respuesta = treading.Thread(target=self.respuesta)
    respuesta.deamon = True
    respuesta.start()
    while True:
        try:
            datos = self.respuesta(1024)
            if datos:
                print(pickle.loads(datos))
        except:
            pass

def envia(self):
    self.socket.send(pickle.dumps(mensaje))

def desconecta(self):
    while True:
			mensaje = input('->')
			if mensaje != 'salir':
				self.send_mensaje(mensaje)
			else:
				self.socket.close()
				sys.exit()
