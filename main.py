from functions import *
from os import system

fajlbeolvasása()

valasztas=""
while valasztas!='0':
    valasztas=menu()
    if valasztas=="1":
        
        kiír()
    elif valasztas=='2':
        Újkönyv()
    elif valasztas=='3':
        system('cls')
        kikölcsönzes()
    elif valasztas=='4':
        system('cls')
        könyvvisszahozása()
    elif valasztas=='5':
        system('cls')
        konyvTorlese()