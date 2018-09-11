#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle

class ServidorChat():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('localhost', 8014))
        self.socket.listen(10)
        self.socket.setblocking(False)
        self.clientes = []

    def conectar(self):
        while True:
            try:
                conexion, direccion = self.socket.accept()
                self.clientes.append(conexion)
                print "Nueva conección establecida", usuario
                hilo_envia = threading.Thread(self.envia_mensaje()).start()
                hilo_recibe = threading.Thread(self.recibe_mensaje()).start()
                hilo_envia.join()
                hilo_recibe.join()
            except:
                sys.exit()

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

    def enviar(self):
        for c in self.clientes:
            try:
                if c != cliente:
    				c.send(msg)
            except:
                self.clientes.remove(c)

    def recibe(self):
        try:
            self.usuario = cliente.recv(1024)
            self.mensaje = cliente.recv(1024)
        except:
            print("Error en el mensaje recibido")

    def envia_especifico(self, mensaje, cliente):
        pass

    def desconecta(self):
        mensaje = input('->')
        if mensaje == 'salir':
            for cliente in self.clientes:
                cliente.close()
            self.socket.close()
            sys.exit()
        else:
            pass


def main():
    servidor = ServidorChat()
    servidor.__init__()
    while True:
        try:
            conectar = threading.Thread(target=servidor.conectar()).start()
            procesar = threading.Thread(target=servidor.procesar()).start()

            conectar.daemon = True
            conectar.start()

            procesar.daemon = True
            procesar.start()
        except:
            print 'Algo salio mal'
            servidor.desconecta()
            sys.exit()

main()
