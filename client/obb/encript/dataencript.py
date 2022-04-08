
from cryptography.fernet import Fernet
from pathlib import Path
import os

from .import keymake







BASE = Path(__file__).resolve().parent.parent


pasw_path= os.path.join(BASE,"files\_login2.txt")

fil= open(pasw_path,'r') 
pawlist= fil.readlines()
paw=pawlist[2] # get the password form the file 
fil.close()

key= keymake.privateKey(paw) # use that passrod in to encripted key code 

filenc = Fernet(key)

def encr(data):
    
    encrypted = filenc.encrypt(data)

    return encrypted

def decr(data):
    
    decrypted = filenc.decrypt(data)

    return decrypted
