#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle

class ServidorChat():

    def crea_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8800))
        self.socket.listen(10)
        self.sock.setblocking(False)
        return socket

    def conecta(self):
        while True:
            try:
                conexion, direccion = self.socket.accept()
                conexion.setblocking(False)
                self.clientes.append(conexion)
                print "Nueva conección establecida", direccion
            except:
                pass

    def procesar(self):
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        mensaje = c.recv(1024)
                        if data:
                            self.enviar_a_todos(datos,c)
                    except:
                        pass
        return mensaje

    def enviar_a_todos(self, mensaje, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(mensaje)
            except:
                self.clientes.remove(c)

    def desconecta(self):
        mensaje = input('->')
        if mensaje == 'salir':
            self.socket.close()
            sys.exit()
        else:
            pass
