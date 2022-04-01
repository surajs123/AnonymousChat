from ast import While
import socket


import typer
app = typer.Typer()

###########################################

from pathlib import Path
import os
import re

BASE = Path(__file__).resolve().parent.parent # to get the path





# to get the login username and password

def get_login():
    pathl= os.path.join(BASE,"obb\_login.txt")
    logc= open(pathl,'r')
    username=logc.read()
    logc.close()
    
    return username

# to create the username and passwor for the login
@app.command()
def login(user,pas):
    #user=input('Username : ')
    #pas =input('Password : ')
    pathl= os.path.join(BASE,"obb\_login.txt")
    regc=open(pathl,'w')
    regc.write(f'login[{user}::##::{pas}]')
    regc.close()

# it will cleaar the login page for logout
@app.command()
def logout():
    pathl= os.path.join(BASE,"obb\_login.txt")
    regc=open(pathl,'w')
    regc.write('')
    regc.close()


############################################




@app.command()
def chatbox():
    while True:
        c = socket.socket()
        try:
            c.connect(('127.0.0.1',5000))
            val=get_login()
            c.sendall(bytes(val,'utf-8'))
            msg1=c.recv(1024).decode()
            if msg1=='true##::':
                c.send(bytes("text###::box",'utf-8'))
                while True:
                    data = c.recv(1024)
                    if not data:
                        break
                c.close()
            else:
                print(" pleases login for send data ")

        except:
            print (' error to communictuion')


if __name__=='__main__':
    app()