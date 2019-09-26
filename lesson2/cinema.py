film = input('Пятница, Чемпионы, Пернатая банда: ')
data = input('дата: ')
time = int(input('время: '))
tickets = int(input('количество билетов:'))
def price(f,t):
    if f == 'Пятница':
        if t == 12:
            cost = 250
        elif t == 16:
            cost = 350
        elif t == 20:
            cost = 450
    elif f == 'Чемпионы':
        if t == 10:
            cost = 10
        elif t == 12:
            cost = 13
        elif t == 16:
            cost = 350
    elif f == 'Пернатая банда':
        if t == 10:
            cost = 350
        elif t == 14:
            cost = 450
        elif t == 18:
            cost = 450
    return cost

def cost_t(x):
    if x <= 20:
        return x
    else:
        return x*0.8
        

def data_s(d):
    if d == 'завтра':
        return 0.95
    else :
        return  1

cost = price(film,time)
cost = float(cost * cost_t(tickets))
cost = float(cost * data_s(data))
print("Ваша стоимость", cost)


         
                
        
    
