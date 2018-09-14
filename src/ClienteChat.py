#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class ClienteChat():

    #creando socket
    socket = socket.socket()
    #estableciendo conexion
    socket.connect( ('localhost', 8754) )
    socket.send("El cliente se a conectado")
    respuesta = socket.recv(1024)
    print respuesta
    socket.close()
