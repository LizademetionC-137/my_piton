line = 'Мой дядя самых честных правил, \nКогда не в шутку занемог, \nОн уважать себя заставил, \nИ лучше выдумать не мог'
line = line.split()
for i in range(len(line)):
    if line[i][0] == 'м':
        del line[i]
print(' '.join(line))
