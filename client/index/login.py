from pathlib import Path
import os
import re
import typer
import getpass
app = typer.Typer()
BASE = Path(__file__).resolve().parent.parent # to get the path

# to get the login username and password

def get_login():
    pathl= os.path.join(BASE,"obb\_login2.txt")
    logc= open(pathl,'r')
    username=logc.read()
    logc.close()
    return username

# to create the username and password for the login
@app.command()
def login():
    user=input('Username : ')
    room=input("Room : ")
    pas = getpass.getpass('Password : ')
    pas2 = getpass.getpass('Re-Password : ')
    if pas==pas2:
        pathl= os.path.join(BASE,"obb\_login2.txt")
        regc=open(pathl,'w')
        regc.write(f'{user}\n{room}\n{pas}')
        regc.close()
        print(f"""{user} your login created for room :{room} 
        now you cam use the chat and chtabox etc. 
        to connect the server ...""")
    else:
        print("error: the password is not match ")

# it will cleaar the login page for logout
@app.command()
def logout():
    pathl= os.path.join(BASE,"obb\_login2.txt")
    regc=open(pathl,'w')
    regc.write('None')
    regc.close()
    print("""

    [logout account ] your acoount was logout
    now dont try to connect the server..
    it will give you the connecton error !!""")


if __name__== '__main__':
    app()



