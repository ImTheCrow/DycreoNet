import socket
from threading import Thread

clientsList = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 3118
s.bind((host, port))
s.listen(10)

clientsList.append(s)

class main(Thread, client):

    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def connexion(self):
        username = self.client.recv(1024)
        username = username.decode()
        #Checker dans la base de données
        if 

    def run(self):
        data = self.client.recv(1024)
        data = data.decode()
        if data == "connexion":
            connexion()
        if data == "inscription":
            inscription()
        else:
            self.client.close()





while 1:
    lireSockets, ecrireSockets, erreursSockets = select.select(clientslist, [], [])
    for sock in lireSockets:
        if sock == s:
            client, infos = s.accept()
            #Créer thread
            clientslist.append(client)
            print("%s est connecté" % str(infos))



