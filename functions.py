from os import system
from data import *
osszetevoneve = []
osszetevoara = []

filename = 'osszetevok.csv'


def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Új recept felvétele')
    print('2 - Új összetevő felvétele')
    print('3 - Receptek kiírása')
    print('4 - Összetevők kiírása')
    print('5 - Recept törlése')
    print('6 - Összetevő törlése')
    return input('Választás: ')

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


def Mentes():
    with open(filename, 'w', encoding='utf-8') as cel:
        cel.write(címsor)
        for i in range(len(osszetevoneve)):
            cel.write(f'{osszetevoneve[i]};{osszetevoara[i]}\n')
    osszetevoara.clear()
    osszetevoneve.clear()