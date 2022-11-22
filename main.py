from functions import *

choice = ''
while choice != '0':
    loadOsszetevok()
    choice = menu()
    if choice == '1':
        pass
    elif choice == '4':
        osszesOsszetevo()
    else:
        print('hibás válasz')
    Mentes()
       