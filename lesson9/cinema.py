cinema = {
            'Пятница': {'time_price': { 12:250,16:350,20:450}},
            'Чемпионы':{'time_price': { 10:250,13:350,16:350}},
            'Пернатая банда':{'time_price': { 10:350, 14:450, 18:450}}
          }

for i in cinema:
    print(i)
movie = input('Выбирите фильм: ')

for i in cinema[movie]['time_price']:
    print(i)
    
time = int(input('Выбирите время: '))

data = input('Выбирите дату:\nзавтра\nпослезавтра\n')
tickets = int(input('Сколько вас?: '))


price = cinema[movie]['time_price'][time]*tickets

if data == 'завтра ' and tickets >= 20:
    price *= 0.75
if data != 'завтра' and tickets >= 20:
    price *= 0.8
if data == 'завтра' and tickets < 20:
    price *= 0.95

print(price)
