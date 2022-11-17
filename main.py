from functions import *

choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        addNewRecept()
    elif choice == '4':
        osszesOsszetevo()
       