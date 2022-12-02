from data import cim,szerzö,megtalalhato
from os import system

def menu():
    system('cls')
    print("---------MENÜ---------")
    print('0 - Kilépés')
    print('1 - Könyveklistája')
    print('2 - új könyv hozzáadása a listához')
    print('3 - könyv kikölcsönzése')
    print('4 - könyv visszahozása a könyvtárba')
    print('5 - könyv törlése a listából')
    return input('Választás: ')

def fajlbeolvasása():
    file=open('Books.csv','r',encoding="utf-8")
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(',')
        cim.append(darabolt[0])
        szerzö.append((darabolt[1]))
        megtalalhato.append((darabolt[2]))
    file.close

def kiír():
    system("cls")
    print("Könyvek listája")
    for i in range(0,len(cim)):
        print(f"\t {i+1}.{(cim[i])}, {(szerzö[i])}, {(megtalalhato[i])}")
    input()


def Újkönyv():
    system("cls")
    print("Új könyv felvétele")
    ujkonyv=input("Kérem adja meg az új könyv címét!")
    cim.append(ujkonyv)
    ujszerzo=input("Kérem adja meg az új könyv szerzőjét!")
    szerzö.append(ujszerzo)
    megtalalhato=1
    end(ujkonyv,ujszerzo,megtalalhato)
    input("A könyv sikeresen fel lett véve az adatbázisba")

def end(cim,szerzö,megtalalhato):
    file=open("Books.csv","a", encoding="utf-8")
    file.write(f'\n{cim},{szerzö},{megtalalhato}')
    file.close()

def kikölcsönzes():
    system("cls")
    kiír()
    sSz=int(input("Válassza ki a kívánt könyv sorszámát "))
    cim(sSz-1)
    szerzö(sSz-1)
    if megtalalhato==1:
        megtalalhato=0
        print ("A könyv kikölcsönzése sikeres volt ")
    elif megtalalhato==0:
        print("A könyv jelenleg kikölcsönzés alatt van")
    input()    
     



def konyvTorlese():
    system('cls')
    print('----KÖNYV TÖRLÉSE---\n')
    kiír()
    sSz=int(input('Melyik könyvet töröljünk a listából? Adja meg a sorszámát: '))
    cim.pop(sSz-1)
    szerzö.pop(sSz-1)
    megtalalhato.pop(sSz-1)
    mentesFajlba()
    input('Sikeres törlés.')

def mentesFajlba():
    file=open('jumps.csv','w',encoding='utf-8')
    for i in range(len(cim)):
        file.write(f'{cim[i]};{szerzö[i]};{megtalalhato[i]} ')
        if i<len(cim)-1:
            file.write('\n')
    file.close()