import socket               # Import socket module
from threading import Thread
import _thread

###### check ussername or password valid #####
from pathlib import Path
import os
import re

BASE = Path(__file__).resolve().parent.parent


def check(pas):
    pathl= os.path.join(BASE,"room1\Auther.txt")
    logc= open(pathl,'r')
    user=logc.readlines()
    
    logc.close()
   
    if f'{pas}\n' in user:
        return True
    else:
        return False    


def recode(msg,nam):
    path1= os.path.join(BASE,"room1\cound1.txt")
    #path2= os.path.join(BASE,"room1\cound2.txt")
    pathbox= os.path.join(BASE,"room1\chatbox.txt")
    
    ## open files
    data= re.findall('&.*>>',nam)
    data2=str(data[0])
    
    ####
    f1=open(path1,'r')
    num1=int(f1.read())
    f1.close()

    box= open(pathbox,'a')
    box.write(f'{data2[1:]} {msg}\n')
    box.close()
    

    #print(f'{data2[1:]} {msg}')
    num1+=1

    #cound the chage
    f1=open(path1,'w')
    f1.write(str(num1))
    f1.close()

###########################################################################

def on_chat_box(clientsocket,cout1):
    
    cout_path= os.path.join(BASE,"room1\cound1.txt")
    path_file= open(cout_path,'r')
    cout2= path_file.read()
    path_file.close()
    
    clientsocket.send(bytes(cout2,'utf-8'))# give the client count value
    if cout1 != int(cout2):    
        ### open chat##
        chat_path=os.path.join(BASE,"room1\chatbox.txt")
        chat_file= open(chat_path,'r')
        chat_data=chat_file.readlines()
        num=0
        send_data=''
        for data in chat_data:
            num+=1
            if num<cout1:
                continue
            send_data+=data
            
        clientsocket.send(bytes(send_data,'utf-8'))
        clientsocket.close()
    else:
        clientsocket.close()







def on_new_client2(clientsocket,addr,nam):
    
    while True:
        msg = clientsocket.recv(1024).decode()
        if msg=='stop':
            break
        #do some checks and if msg == someWeirdSignal: break:
        recode(msg,nam)
        
        
        msg = input()
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host='127.0.0.1'
port = 5000               # Reserve a port for your service.

print ('Server started!')
print ('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(8)                 # Now wait for client connection.

print ()
print ("The server was runnig .....\n")
print ("Use Ctrl_C to stop server ")
try:
    while True:
        c, addr = s.accept()
        che = c.recv(1024).decode()
        if check(che):
            c.send(bytes('true##::','utf-8'))
            typ=c.recv(1024).decode()
            if typ=="text###::chat":
            
                _thread.start_new_thread(on_new_client2,(c,addr,che))
            elif typ=="text###::chatbox":
                cout=c.recv(1024).decode()
                _thread.start_new_thread(on_chat_box,(c,int(cout)))

            
        else:
            c.send(bytes('false##::','utf-8)'))
            
            
            

            #Note it's (addr,) not (addr) because second parameter is a tuple
            #Edit: (c,addr)
            #that's how you pass arguments to functions when creating new threads using thread module.
    s.close()
except KeyboardInterrupt:
    print("the server was close ")


                                                                             