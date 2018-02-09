# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:30:09 2018

@author: matteo.caravati
"""
#https://github.com/danielcardeenas/PythonChat/blob/master/Multi/servermul.py

import socket
import sys
from threading import Thread
import select

clientslist = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 2943
s.bind((host, port))
s.listen(10)

clientslist.append(s)

def send(data):
    for socket in clientslist:
        client.send(data.encode())
        

while 1:
    lireSockets, ecrireSockets, erreursSockets = select.select(clientslist,[],[])
    for sock in lireSockets:
        if sock == s:
            client, infos = s.accept()
            clientslist.append(client)
            print("Client %s connected" % str(infos))
        
    else:
        try:
            data = client.recv(1024)
            data = data.decode()
            data = str(infos) + ": " + data
            if data == '':
                print("Client %s is offline" % str(infos))
                client.close()
                clientslist.remove(client)
                continue
            if data == "/quit":
                print("Client %s quit" % str(infos))
                client.close()
                clientslist.remove(client)
            else:
                send(data)
                pass
        except:
            pass
s.close()
            
            