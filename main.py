agree = True

def dis_agree(word):
    if word == 'Выйти':
        return False
    elif word == 'Продолжить':
        return True
    else:
        return 'Введена некорректная команда'


while agree:
    print("start")
    print("- " * 10)
    word = input()
    agree = dis_agree(word)
    if agree == True:
        print('Продолжение')
        continue
    elif agree == False:
        print('Конец')
    else:
        continue
