L = ['самовар', 'весна','лето']
import random 

word = random.choice(L)
lst = list(word)
letter = random.choice(lst)
myl = lst.index(letter)

lst[myl] = '?'

word = ''.join(lst)

print("Попробуй угадавать букву!",word)

let = input()
if let == letter:
    print('Победа!')
else:
    print("Неть")


