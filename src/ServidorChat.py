#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle

class ServidorChat(object):

    def __init__(self, host, port):
        #lista que almacenara a los clientes
        self.clientes = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #creando socket que establece conexión hasta para 10000 clientes
        self.socket.bind((str(host), int(port)))
        self.socket.listen(10000)
        self.socket.setblocking(False)
        #hilos tipo daemon para el servidor
        aceptar = threading.Thread(target=self.aceptar)
        procesar = threading.Thread(target=self.procesar)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()
        # DISCONNECT
        print 'Teclee "DISCONNECT" para cerrar el servidor.'
        while True:
			mensaje = raw_input()
			if mensaje == 'DISCONNECT':
				self.socket.close()
				sys.exit()
			else:
				pass

    def lista_de_clientes(self, cliente):
        cliente.send(self.clientes)
        '''
        m = len(clientes)
        for i in range(1,m):
            cliente.send([self.clientes[i][0], self.clientes[i][1]])
        '''

    def mensaje_privado(self, user, mensaje, cliente):
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
                conexion.send('Te has conectado al servidor')
                print ('Nueva conexión establecida')
                cliente = conexion.recv(1024)
                cliente = pickle.loads(cliente)
                cliente.append(conexion)
                conexion.setblocking(False)
                self.clientes.append(cliente)
                print self.clientes
            except:
                pass

    def procesar(self):
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						datos = c.recv(1024)
						if datos:
							self.mensaje_publico(datos,c)
					except:
						pass


def main():
    #try:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    servidor = ServidorChat(host, port)
    #except:
    print ('Algo salio mal, intente de nuevo')
    sys.exit()

main()
