import random 
random_num = random.randint(1,4) 
a=int(input("Угадай число!: ")) 

if a == random_num : 
    print("Победа! Ты угадал!") 
else : 
    print("Не угадал!Я загадал {0}".format(random.choice([random_num+1,random_num-1])))
