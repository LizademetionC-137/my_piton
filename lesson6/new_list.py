lst = [2,4,9,16,25]

new_lst = []
for x in lst:
    new_lst.append(x**2)
print(new_lst) 

print(list(map((lambda x: x**2),lst)))

print([x**2 for x in lst])
