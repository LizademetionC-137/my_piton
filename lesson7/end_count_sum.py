suma = 0
while True:
    x = input('Введите число или стоп для входа:')
    if x == 'стоп':
        break
    elif x.isalpha() == True :
        print('Ошибка ввода')
    else:
        suma += int(x)
print(suma)
