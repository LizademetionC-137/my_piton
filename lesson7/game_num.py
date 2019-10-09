import random
x = random.randint(0,10)
print("Компьютер загадал число.\nУ вас есть три попытки.Удачи?\nПопробуйте угадать!")
count = 0
while count < 3:
    a = input()
    if a == 'Выход':
        break
    if int(a) == x:
        print("Победа")
        break
    else:
        if int(a) > x:
            print("Попробуйте число меньше!")
        else:
            print("Попробуйте число больше!")
        count += 1
print('Игра окончена\nЧисло:',x)
