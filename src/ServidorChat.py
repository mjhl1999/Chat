#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

def crea_socket(self):
        socket = socket.socket()
        socket.bind(('localhost',5000))
        socket.listen(10)
        return socket

def conecta(self):
    while True:
        (conexion, direccion) = socket.accept()
        print "Nueva conección establecida", direccion

def recibe(self):
    while True:
        mensaje = self.crea_socket().recv(1024)
        self.conecta().send("Te has conectado al servidor")
        return mensaje

def desconecta(self):
    socket.close()
