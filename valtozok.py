"""
egy=1
print(egy)
print(type(egy))

'''
Kerülendő típus csere
egy="egy"
print(egy)
print(type(egy))
'''
egy=2 # nem szerencsés - beszélő változó név
print(egy)

szám=123    # kerülendő az ékezet!!!
print(szám)

szam = 123
print(type(szam))
szam = szam/2
print(szam)
print(type(szam))

szam = 12
szam = szam +1
print(szam)
print(type(szam))

szam += 1
print(szam)

szam += 10
print(szam)

szam -= 10
print(szam)

szam *= 10
print(szam)

szam /= 2
print(szam)

szam **= 2  # szam = szam ** 2
print(szam)

szam2=1.2
print(szam*szam2)

print(szam == szam2)

l = szam == szam2
print(l,type(l))

l = 12 == 12
print(l,type(l))

s1='Alma'
s2='alma'
print(s1 == s2)
'''
S2=s1 # nem szerencsés
print(s1 == S2)
'''

l = (12,23,11,"körte")
print(l)
print(type(l))

l = {12,23,11,"körte"}
print(l)
print(type(l))

l = [12,23,11,"körte"]
print(l)
print(type(l))

l = {12,23,11,"körte",11}
print(l,type(l))

l = [12,23,11,"körte",11]
print(l,type(l))
"""
szoveg = "Piros pipacs"
print(szoveg,type(szoveg))
#szoveg +=1

szoveg *=2
print(szoveg,type(szoveg))

#szoveg *=2,5

x,y,z = (12,13,"szia")
print(x,y)

x,y = (12,[13,"szia"])
print(x,y,type(y))

szoveg2="kutya"
sz = szoveg+"\n"+szoveg2
print(sz)

egy = 1
print(egy,end="\t")
egy += 1
print(egy,end="\t")
egy += 1
print(egy)

egy += 1
print(egy,end="\t")
egy += 1
print(egy,end="\t")
egy += 1
print(egy)

egy += 1
print(egy,end="\t")
egy += 1
print(egy,end="\t")
egy += 1
print(egy)
print("*"*10)
print("1\t2\t3")
print("4\t5\t6")