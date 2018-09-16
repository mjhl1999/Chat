#!/usr/bin/python
# -*- coding: utf-8 -*-

class Eventos():

    IDENTIFY = "IDENTIFY"
    STATUS = "STATUS"
    USERS = "USERS"
    MESSAGE = "MESSAGE"
    PUBLICMESSAGE = "PUBLICMESSAGE"
    CREATEROOM = "CREATEROOM"
    INVITE = "INVITE"
    JOINROOM = "JOINROOM"
    ROOMESSAGE = "ROOMESSAGE"
    DISCONECT = "DISCONECT"

    def evento(self,msg):
        try:
            if msg == "IDENTIFY":
                return self.IDENTIFY
            if msg == "STATUS":
                return self.STATUS
            if msg == "MESSAGE":
                return self.MESSAGE
            if msg == "PUBLICMESSAGE":
                return self.PUBLICMESSAGE
            if msg == "CREATEROOM":
                return self.CREATEROOM
            if msg == "INVITE":
                return self.INVITE
            if msg == "JOINROOM":
                return self.JOINROOM
            if msg == "ROOMESSAGE":
                return self.ROOMESSAGE
            if msg == "DISCONECT":
                return self.DISCONECT
            else:
                raise ValueError
        except:
            print("Evento no valido.")
