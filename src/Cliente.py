#!/usr/bin/python
# -*- coding: utf-8 -*-

class Cliente(object):

    def __init__(self, socket):
        self.socket = socket
        self.nombre = ""
        self.estado = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_estado(self, estado):
        self.estado = estado

    def get_socket(self):
        return self.socket

    def get_nombre(self):
        return self.nombre

    def get_estado(self):
        return self.estado
