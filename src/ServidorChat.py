#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle

class ServidorChat(object):

    def __init__(self, host, port):
        #estructura para almacenar clientes
    	self.clientes = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((str(host), int(port)))
        self.socket.listen(10)
        self.socket.setblocking(False)
        aceptar = threading.Thread(target=self.aceptar)
        procesar = threading.Thread(target=self.procesar)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()
        while True:
            mensaje = raw_input('->')
            if mensaje == "DISCONNECT":
                self.socket.close()
                sys.exit()
            else:
                pass

    def mensaje_publico(self, mensaje, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(mensaje)
			except:
				self.clientes.remove(c)

    def aceptar(self):
		while True:
			try:
				conexion, direccion = self.socket.accept()
				conexion.setblocking(False)
				self.clientes.append(conexion)
			except:
				pass

    def procesar(self):
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.mensaje_publico(data,c)
					except:
						pass

def main():
    #try:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    servidor = ServidorChat(host, port)
    servidor.conecta(host, port)
    #except:
    print ('Algo salio mal, intente de nuevo')
    sys.exit()

main()
