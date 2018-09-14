#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class ClienteChat(object):

    def __init__ (self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def magia(self):
        #creando socket
        self.my_socket = socket.socket()
        #estableciendo conexion
        self.my_socket.connect( ('localhost', 8754) )
        self.my_socket.send("El cliente se a conectado")
        respuesta = self.my_socket.recv(1024)
        print (respuesta)
        self.my_socket.close()


def main():
    print ('Ingresa tu nombre de usuario: ')
    usuario = input()
    #if (usuario == " " or usuario == ):
    print ('Elige tu estado (ACTIVE, AWAY, BUSY):')
    estado = input()
    cliente = ClienteChat(usuario, estado)
    cliente.magia()

main()

"""
    try:
        print 'Ingresa el host:'
        host = raw_input()
        print 'Ingresa el puerto:'
        puerto = raw_input()
        cliente.crea_socket()
        cliente.conecta(host, puerto)
    except:
        print("Conexión rechazada, intente de nuevo,")
"""
