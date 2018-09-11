#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import pickle

class Comportamiento():

    def conecta_cliente(self):
        self.clientes.append(conexion)
        print ("Nueva conección establecida con ", usuario)

    def procesa_mensaje(self):
        while True:
            if len(clientes) > 0:
                for c in clientes:
                    try:
                        mensaje = c.recv(1024)
                        if data:
                            self.enviar_a_todos(datos,c)
                    except:
                        pass

    def enviar_a_todos(self):
        for c in self.clientes:
            try:
                if c != cliente:
    				c.send(msg)
            except:
                self.clientes.remove(c)

    def recibe(self):
        try:
            self.mensaje = cliente.recv(1024)
        except:
            print("Error en el mensaje recibido")

    def envia_especifico(self, mensaje, cliente):
            if cliente in self.clientes:
                try:
        			c.send(msg)
                except:
                    print ("El usuario al que quieres enviar el mensjae no existe")

    def desconecta(self):
        mensaje = input('->')
        if mensaje == 'salir':
            for cliente in self.clientes:
                cliente.close()
            self.socket.close()
            sys.exit()
        else:
            pass
