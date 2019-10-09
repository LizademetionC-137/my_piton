x = input('Введите число:')

summa = 0

for i in x:
    if int(i)%2 == 1:
        summa += int(i)**2
print(summa)

