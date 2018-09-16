class ClienteParaLista(object):

    def __init__(self, socket, conexion):
        self.socket = socket
        self.conexion = conexion
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

    def get_conexion(self):
        return self.ip
