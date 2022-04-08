import base64
import os
from click import password_option 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def privateKey(pas):

    password = pas.encode()

    salt=b'\x07\xc6.\x9eo\x8bK\xa5m\xf3\xebM\xa2$\xf7\t'

    kdf= PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()

    )

    key= base64.urlsafe_b64encode(kdf.derive(password)) # can only use kdf once
    

    return key





