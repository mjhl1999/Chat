#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import threading
import pickle

class ServidorChat(object):

    def conecta(self, host, port):
        #lista que almacenara a los clientes
        self.clientes = []
        #crea nuevo socket
        self.socket = socket.socket()
        #establece conexión con el cliente
        self.socket.bind( (host, port) )
        #establece cantidad de peticiones en cola que maneja el socket
        self.socket.listen(10000)
        #hilo tipo daemon para el servidor
        aceptar = threading.Thread(target=self.aceptar)
        aceptar.daemon = True
        aceptar.start()
        procesar = threading.Thread(target=self.procesar)
        procesar.daemon = True
        procesar.start()
        print 'Teclee "DISCONNECT" para cerrar el servidor.'
        while True:
            mensaje = raw_input('-> ')
            if mensaje == 'DISCONNECT':
                self.socket.close()
                sys.exit()
            else:
                pass


    def aceptar(self):
        #acceptando peticiones de clientes
        while True:
            conexion, direccion = self.socket.accept()
            print ("Nueva conexion establecida")
            conexion.send("Te has conectado al servidor")
            #tripleta =  conexion.recv(1024)
            #self.clientes.append(str(tripleta))
            self.clientes.append(conexion)

    def procesar(self):
        while True:
            if(len(self.clientes) > 0):
                for i in self.clientes:
                    try:
                        mensaje = i.recv(1024)
                        if mensaje:
                            mensaje = str(mensaje)
                            self.envia_publico(mensaje,i)
                            print mensaje
                    except:
                        pass

        def ver_usuarios(self):
            peticion = conexion.recv(1024)
            if (peticion == 'IDENTIFY'):
                conexion.send(clientes)

        def status(self, estado):
            pass

        def ussers(self):
            pass

        def envia_publico(self, mensaje):
            for i in self.clientes:
                try:
                    if c != cliente: #evita que te autoenvies un mensaje
                        c.send(pickle.dumps(mensaje))
                except:
                    self.clientes.remove(i)


def main():
    #try:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    servidor = ServidorChat()
    servidor.conecta(host, port)
    #except:
    print ('Algo salio mal, intente de nuevo')
    sys.exit()

main()
