#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random
import threading
import pickle
import sys

class ClienteChat(object):

    def __init__ (self, nombre, estado, host, port):
        self.nombre = nombre
        self.estado = estado
        #creando socket
        self.socket = socket.socket()
        #estableciendo conexion
        self.socket.connect( (host, port) )
        #recibe un mensaje desde el sevidor que nos dice si nos hemos conectado
        respuesta = self.socket.recv(1024)
        print (respuesta)
        #envia la informacion del cliente al servidor
        #self.socket.send(str(tripleta))
        self.socket.close()
        #hilo tipo daemon para el cliente
        #mensaje = threading.Thread(target=self.recibe)
        #mensaje.daemon = True
        #mensaje.start()
        #hilo principal y DISCONNECT
        """
        while True:
            mensaje = raw_input('-> ')
            if (mensaje != 'DISCONNECT'):
                self.envia_publico(str(mensaje))
            else:
                self.socket.close()
                sys.exit()
        """
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
