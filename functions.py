from os import system
import time

osszetevoneve = []
osszetevoara = []
címsor = ''
címsor2 = ''

etelek = []
osszetevok = []
mennyisegek = []
receptek = []

filename = 'osszetevok.csv'
filename2 = 'receptek.csv'


def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Összetevők kezelése')
    print('2 - Új recept felvétele')
    print('3 - Recept keresés')
    print('4 - Recept törlés')
    return input('Választás: ')

def Osszetevok():
    choice = ''
    while not choice.lower == '0':
        system('cls')
        print(choice)
        print('0 - Kilépés\n1 - Összetevők kilistázása\n2 - Összetevő hozzáadása\n3 - Összetevő törlése')
        choice = input('\nVálasz: ').lower()
        if choice == '0':
            Kilepes()
        elif choice == '1':
            system('cls')
            print('NÉV\t\tÁR')
            for i,item in enumerate(osszetevoneve):
                print(f'{item.capitalize()}\t\t{osszetevoara[i]} Ft')
                input('\nA továbblépéshez nyomja meg az ENTER-t!')
        elif choice == '2':
            system('cls')
            bekertosszetevo = input('Adja meg az összetevőt: ')
            bekertar = input('Adja meg az összetevő egységárát: ')
            system('cls')
            print(f'Biztosan szeretné menteni ezt az összetevőt? ({bekertosszetevo.capitalize()} - {bekertar} Ft)')
            valasz = False
            while valasz != True:
                valasztas = input('\nVálasz (i/n)').capitalize()
                if valasztas == 'i':
                    osszetevoneve.append(bekertosszetevo)
                    osszetevoara.append(bekertar)
                    system('cls')
                    print('Az összetevőd elmentettük')
                    time.sleep(1.5)
                    valasz = True
                elif valasztas == 'n':
                    Kilepes()
                    valasz = True
                else:
                    system('cls')
                    print('Hibás válasz!')
                    time.sleep(1.5)
        elif choice == '3':
            system('cls')
            bekertosszetevo = input('Adja meg a törölni kívánt összetevőt: ')
            for i,item in enumerate(osszetevoneve):
                if bekertosszetevo.lower() in osszetevoneve:
                    system('cls')
                    print('A megadott összetevő nem található')
                    time.sleep(1.5)
                elif bekertosszetevo == item:
                    valasz = False
                    while valasz != True:
                        system('cls')
                        print(f'Biztosan törölni kívánja ezt az összetevőt? ({bekertosszetevo.capitalize()})')
                        valasztas = input('Válasz (i/n) : ').lower()
                        if valasztas == 'i':
                            valasz = True
                            osszetevoneve.pop(i)
                            osszetevoara.pop(i)
                        elif valasztas == 'n':
                            valasz = True
                            Kilepes()
                        else:
                            system('cls')
                            print('Helytelen válasz!')
                            time.sleep(1.5)
        else:
            system('cls')
            print('Hibás válasz!')
            time.sleep(1.5)

def Ujrecept():
    bekertmennyiseg2 = []
    osszetevoneve2 = []
    osszetevoara2 = []
    
    system('cls')
    bekertetel = input('Adja meg az étel nevét:').lower()
    bekertosszetevok = input('Adja meg az összetevők listáját vesszővel elválasztva:').lower()
    bekertosszetevok2 = bekertosszetevok.split(',')

    for i in range(len(bekertosszetevok2)):
        bekertmennyiseg = input(f'Adja meg ennek az öszetevőnek ({bekertosszetevok2[i]}) a mennyiségét (gramm/db/liter): ')
        if not bekertosszetevok2[i].lower() in osszetevoneve:
            ar = input(f'Adja meg ennek az összetevőnek ({bekertosszetevok2[i]}) az egységárát: ')
            osszetevoneve2.append(bekertosszetevok2[i])
            osszetevoara2.append(ar)
        bekertmennyiseg2.append(bekertmennyiseg)

    bekertrecept = input(f'Adja meg a(z) {bekertetel.capitalize()} étel elkészítési módját: ')

    system('cls')
    print(f'Az étel neve: {bekertetel.capitalize()}')
    print(f'Az étel hozzávalói:')
    for item in bekertosszetevok2:
        print(f'\t{bekertosszetevok2[i].capitalize()}  -  {bekertmennyiseg2[i]}')
    print(f'Recept:')
    print(bekertrecept)

    valasztas = input('\nMenti a receptet? (i/n): ')
    if valasztas.upper() == 'I':
        for i in range(len(osszetevoneve2)):
            osszetevoneve.append(osszetevoneve2[i])
            osszetevoara.append(osszetevoara2[i])
        etelek.append(bekertetel)
        osszetevokvegleges = ''
        for osszetevo in bekertosszetevok2:
            osszetevokvegleges += f'{osszetevo},'
        osszetevok.append(osszetevokvegleges[:-1])
        mennyisegekvegleges = ''
        for mennyiseg in bekertmennyiseg2:
            mennyisegekvegleges += f'{mennyiseg},'
        mennyisegek.append(mennyisegekvegleges[:-1])
        receptek.append(bekertrecept)
        system('cls')
        print('A recept mentve')
        time.sleep(1.5)
    elif valasztas.upper() == 'N':
        Kilepes()

    else:
        print('Helytelen válasz')
        time.sleep(1.5)
        Kilepes()


def loadReceptek():
    global címsor2
    with open(filename2,'r', encoding='utf-8') as forras:
        címsor2 = forras.readline()
        for row in forras:
            splitted = row.strip().split(';')
            etelek.append(splitted[0])
            osszetevok.append(splitted[1])
            mennyisegek.append(splitted[2])
            receptek.append(splitted[3])


def loadOsszetevok():
    file = open(filename, 'r', encoding='utf-8')
    global címsor
    címsor = file.readline()
    for row in file:
        splitted = row.strip().split(';')
        osszetevoneve.append(splitted[0])
        osszetevoara.append(splitted[1])
    file.close
    input()

def osszesOsszetevo():
    system('cls')
    print('Összetevők listája:')
    for nev in osszetevoneve:
        print(f'\t{nev}')


def MentesOsszetevok():
    with open(filename, 'w', encoding='utf-8') as cel:
        cel.write(címsor)
        for i in range(len(osszetevoneve)):
            cel.write(f'{osszetevoneve[i]};{osszetevoara[i]}\n')
    osszetevoara.clear()
    osszetevoneve.clear()

def MentesReceptek():
    with open(filename2, 'w', encoding='utf-8') as cel:
        cel.write(címsor2)
        for i in range(len(etelek)):
            cel.write(f'{etelek[i]};{osszetevok[i]};{mennyisegek[i]};{receptek[i]}\n')
    etelek.clear()
    osszetevok.clear()
    mennyisegek.clear()
    receptek.clear

def Kilepes():
    system('cls')
    print('Kilépés.')
    time.sleep(0.5)
    system('cls')
    print('Kilépés..')
    time.sleep(0.5)
    system('cls')
    print('Kilépés...')
    time.sleep(0.5)
    system('cls')
