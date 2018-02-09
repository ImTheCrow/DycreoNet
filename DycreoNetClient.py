# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:19:37 2018

@author: matteo.caravati
"""
from os import system
import socket
from getpass import getpass
import sys
import sqlite3
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 3118
s.connect((host, port))
    
def banniere():
    system("cls")
    print("DycreoNet v1.0\n")
    
def menu():
    system("cls")
    print("DycreoNet v1.0\n")
    print("MENU")
    print("1-Se connecter au réseau chat du DycreoNet")
    print("2-Se connecter au réseau Web du DycreoNet")
    choix_main_menu = input("\nChoix: ")
    if choix_main_menu == 1:
        DycreoChat()
    if choix_main_menu == 2:
        DycreoNetWeb()
    else:
        print("Erreur, le choix sélectionné n'existe pas")
        menu()

def menuDemarrage():
    system("cls")
    print("DycreoNet v1.0\n")
    print("MENU")
    print("1-J'ai déjà un compte DycreoNet")
    print("2-Je n'ai pas de compte DycreoNet")
    choix_menu = int(input("\nChoix: "))
    if choix_menu == 1:
        connexion()
    if choix_menu == 2:
        inscription()
    else:
        print("Erreur, le choix sélectionné n'existe pas")
        menuDemarrage()

def inscription():
    print("yo")

def connexion():
    global s    
    s.send("connexion".encode())
    banniere()
    username = input("Username : ")
    s.send(username.encode())
    print("\n")
    response = s.recv(1024)
    response = response.decode()
    if response == "ok":
        password = input("Password : ")
        s.send(password.encode())
        resp = s.recv(1024)
        resp = resp.decode()
        if resp == "True":
            print("Authentification réussie")
            time.sleep(3)
            print("Redirection...")
            time.sleep(3)
            menu()
        if resp == "False":
            print("Erreur lors de l'authentification")
            time.sleep(3)
            connexion()
    if response == "error":
        print("Erreur, cet utilisateur n'existe pas")
        connexion()
        
    
    
def main():
    socketInit()    
    menuDemarrage()
    
main()
    
    