s = str(input("Введите строку: "))
x = int(input('Введите число: '))

def fun(s , x):
    if len(s) > x:
        return(s.upper())
    else:
        return s

print(fun(s,x))
