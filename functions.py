from os import system
from data import *

osszetevok = 'osszetevok.csv'


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

def addNewRecept():
    f = open('')


    f.close()

def osszesOsszetevo():
    file = open(osszetevok, 'r', encoding='utf-8')
    global címsor 
    címsor = file.readline()
    file.close()

    