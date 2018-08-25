#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

def crea_socket(self):
        socket = socket.socket()
        return socket

def conecta(self):
    socket.connect( ('localhost', 8800) )
    socket.send('Me he conectado al servidor')

def recibe(self):
    respuesta = socket.recv(1024)
    print respuesta

def desconecta(self):
    socket.close()
