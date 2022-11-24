from functions import *

choice = ''
while choice != '0':
    loadOsszetevok()
    loadReceptek()
    choice = menu()
    if choice == '0':
        Kilepes()
    if choice == '1':
        Osszetevok()
    elif choice =='2':
        Ujrecept()
    elif choice =='3':
        pass
    elif choice == '4':
        pass
    else:
        system('cls')
        print('hibás válasz')
        time.sleep(1.5)
    MentesOsszetevok()
    MentesReceptek()