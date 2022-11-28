from data import cim,szerzö,megtalalhato
from os import system

def menu():
    system('cls')
    print("---------MENÜ---------")
    print('0 - Kilépés')
    print('1 - összes könyv listázása')
    print('2 - új könyv hozzáadása a listához')
    print('3 - könyv kikölcsönzése')
    print('4 - könyv visszahozása a könyvtárba')
    print('5 - könyv törlése a listából')
    return input('Választás: ')