#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
from Cliente import Cliente
reload(sys)
sys.setdefaultencoding('utf-8')

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


    def identificar(self, nombre, cliente):
         set_nombre(nombre)

    def asigna_estado(self, estado, cliente):
        pass
        #self.estado = estado

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
                conexion.setblocking(False)
                cliente = Cliente(conexion)
                self.clientes.append(cliente)
                print clientes
            except:
                pass

    def procesar(self):
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    #try:
                    d = c.get_socket(recv(1024))
                    dat = d.encode('UTF-8')
                    datos = dat.rstrip()
                    datoss = datos.split(' ', 1)
                    if datoss[0] == "PUBLICMESSAGE":
                        self.mensaje_publico(datoss.pop(),c)
                    #except:
                        #pass


def main():
    #try:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    servidor = ServidorChat(host, port)
    #except:
    print ('Algo salio mal, intente de nuevo')
    sys.exit()

main()
