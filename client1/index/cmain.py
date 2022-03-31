from ast import While
import socket
from time import sleep
from pathlib import Path
import os
import re
import typer
app = typer.Typer()

                                            ######################################
####################################################### authtecation creation ################################################################
                                            ######################################



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
    regc.write(f'login:!&[ {user} ]::>> ::{pas}]')
    regc.close()

# it will cleaar the login page for logout
@app.command()
def logout():
    pathl= os.path.join(BASE,"obb\_login.txt")
    regc=open(pathl,'w')
    regc.write('None')
    regc.close()


                                            ######################################
####################################################### chat creation ################################################################
                                            ######################################
@app.command()
def chat():
    while True:
        c = socket.socket()
        try:
            data=input('[send]:>> ')
            if data == 'stop':
                break
            c.connect(('127.0.0.1',5000))
            val=get_login()
            c.sendall(bytes(val,'utf-8'))
            msg1=c.recv(1024).decode()
            if msg1=='true##::':
                c.send(bytes("text###::chat",'utf-8'))
                
                c.sendall(bytes(data,'utf-8'))
                c.close()
            else:
                
                print(" pleases login for send data ")
                break

        except:
            print (' error to communictuion')


                                            ######################################
####################################################### chat Box creation ################################################################
                                            ######################################

@app.command()
def chatbox():
    try:
        while True:
            sleep(1)
            c = socket.socket()
            try:
                ###chta count file open ####
                cout_path= os.path.join(BASE,"obb\chtcount.txt")
                cout_file=open(cout_path,'r')
                cout=cout_file.read()
                cout_file.close()
                c.connect(('127.0.0.1',5000))
                val=get_login()
                c.sendall(bytes(val,'utf-8'))
                msg1=c.recv(1024).decode()
                
                if msg1=='true##::':
                    c.send(bytes("text###::chatbox",'utf-8'))
                    c.send(bytes(cout,'utf-8'))
                    msco=c.recv(2045).decode()
                    cout_file=open(cout_path,'w')
                    cout_file.write(msco)
                    cout_file.close()
                    msgg=c.recv(2045).decode()
                    if msgg:
                        print(msgg)
                    c.close()
                else:
                    print(" pleases login for send data ")
                    break
            except:
                print (' error to communictuion')
    except KeyboardInterrupt:
        print("server stop")
        pass



if __name__=='__main__':
    app()









