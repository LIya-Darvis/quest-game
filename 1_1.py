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
    while True:
        print("Если хотите продолжить игру - введите 'Продолжить', если хотите закончить - введите 'Выйти'.")
        agree = dis_agree(input())
