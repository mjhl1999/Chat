#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class ClienteChat(object):

    def __init__ (self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def magia(self, host, port):
        #creando socket
        self.my_socket = socket.socket()
        #estableciendo conexion
        self.my_socket.connect( (host, port) )
        self.my_socket.send("El cliente se a conectado")
        respuesta = self.my_socket.recv(1024)
        print (respuesta)
        self.my_socket.close()




def main():
    print ('Ingresa tu nombre de usuario: ')
    usuario = raw_input()
    if (usuario == None or usuario == ""):
            raise ValueError()
    print ('Elige tu estado (ACTIVE, AWAY, BUSY):')
    estado = raw_input()
    if (estado == 'ACTIVE' or estado == "AWAY" or estado == "BUSY"):
        cliente = ClienteChat(usuario, estado)
    else:
        raise ValueError()
    print 'Ingresa el host:'
    host = raw_input()
    print 'Ingresa el puerto:'
    port = input()
    cliente.magia(host, port)

main()

"""
        cliente.crea_socket()
        cliente.conecta(host, puerto)
    except:
        print("Conexión rechazada, intente de nuevo,")
"""
