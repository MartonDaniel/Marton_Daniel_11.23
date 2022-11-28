from functions import *
from os import system
valasztas=""
while valasztas!='0':
    valasztas=menu()
    if valasztas=="1":
        fajlbeolvasása()
    elif valasztas=='2':
        system('cls')
        konyveklistaja()
    elif valasztas=='3':
        system('cls')
        pass
    elif valasztas=='4':
        system('cls')
        pass
    elif valasztas=='5':
        system('cls')
        pass