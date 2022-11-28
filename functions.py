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

def konyveklistaja():
    file=open('Books.csv','r',encoding="utf-8")
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(',')
    cim.append(darabolt[0])
    szerzö.append(float(darabolt[1]))
    megtalalhato.append(float(darabolt[2]))
    file.close()