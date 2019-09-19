x = int(input("Введите число "))

def fun_P(x):
    if x % 2 == 0:
        return "четное"
    else :
        return "нечетное"

print("Ваше число", fun_P(x))
