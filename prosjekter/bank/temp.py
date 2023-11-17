a = b'3871230262S'
b = str(a)

liste = []
c = ''
for x in b:
    
    if x in ['1','2','3','4','5','6','7','8','9','0']:
        c += x

liste.append(int(c))
print(liste)
        