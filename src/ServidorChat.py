#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class ServidorChat(object):

    host = 'localhost'
    port = 8753
    #crea nuevo socket
    socket = socket.socket()
    #establece conexión
    socket.bind((host, port))
    #establece cantidad de peticiones en cola que maneja el socket
    socket.listen(10)
    #lista que almacenara a los clientes
    clientes = []
    while True:
        #acceptando peticiones
        conexion, direccion = socket.accept()
        print "Nueva conexion establecida"
        conexion.send("Te has conectado al servidor")
