s = str("У лукоморья 123 дуб зеленый 456")

print(s.find('я'))
print(s.count('у'))

if s.isalpha() == False :
    print(s.upper())
else:
    print("True")

if len(s) > 4:
    print(s.lower())
print(s.replace(s[0],'O'))

