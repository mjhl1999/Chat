#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle

class ServidorChat():

    def crea_servidor(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8800))
        self.socket.listen(10)
        self.socket.setblocking(False)
        self.clientes = []
        return socket

    def conecta(self):
        while True:
            try:
                conexion, direccion = self.socket.accept()
                conexion.setblocking(False)
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
                c.send(bytearray(self.usuario, "utf8"))
                c.send(bytearray(self.mensaje, "utf8"))
            except:
                self.clientes.remove(c)

    def recibe(self):
        try:
            for c in self.clientes:
                self.usuario = cliente.recv(1024).decode('utf-8')
                self.mensaje = cliente.recv(1024).decode('utf-8')
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
        servidor.crea_servidor()
        try:
            aceptar = threading.Thread(target=self.aceptarCon)
            procesar = threading.Thread(target=self.procesarCon)
        except:
            print 'Algo salio mal'
            servidor.desconecta()
            sys.exit()

main()
