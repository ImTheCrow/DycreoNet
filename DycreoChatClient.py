# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:20:55 2018

@author: matteo.caravati
"""

import socket
from threading import Thread

class recev(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        
        
        while 1:
            try:
                data = s.recv(1024)
                data = data.decode()
            except:
                print("La connexion a été éteinte err1")
                #implanter le retour au menu principal
                break
            if data != '':
                print(data)

class send(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        #Implanter la recherche du pseudo dans le client DycreoNet        
        while 1:
            dataToSend = input(">: ")
            if dataToSend == "/quit":
                s.send(dataToSend.encode())
                #implanter le retour au menu principal
                break
            else:
                #dataToSend = pseudo + ": " + dataToSend                
                s.send(dataToSend.encode())

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 2943
    s.connect((host, port))
except:
    print("Erreur lors de la connexion au serveur")
    
send = send()
recv = recev()

send.start()
recv.start()
            