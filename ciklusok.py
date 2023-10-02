'''
szamok = [1,2,33,6,9]
# pl java script:
# for (i=0;i<5;i++) {...ciklus mag ....}
for szam in szamok:
    print(szam,end=", ")
    szam += 1
    print(szam)
print(szam)

#elemek = {12,"Alam",23,"cica",2,23,4,{1,2}}    halmazban halmaz
#elemek = {12,"Alam",23,"cica",2,23,4,[1,2]}    halmazban lista
elemek = {12,"Alam",23,"cica",2,23,4,(1,2)}
for e in elemek:
    print(e,end=", ")
print()
print("-"*10)

elemek = [12,"Alam",23,"cica",2,23,4,(1,2)]
elemek = [12,"Alam",23,"cica",2,23,4,[1,2]]
elemek = [12,"Alam",23,"cica",2,23,4,{1,2}]
elemek = (12,"Alam",23,"cica",2,23,4,{1,2})
for e in elemek:
    print(e,end=", ")
print()
print("+"*10)

szamok = [1,2,3,4]
szamok = range(1,11)
print(szamok,type(szamok))
for i in szamok:
    print(i)

for i in range(1,101):
    print(i,i**2,sep="^2 = ") # i*i = i ** 2

for i in range(1,101,3):
    print(i,i**3,sep="^3 = ") # i*i*i = i ** 3
'''
for i in range(10,-10,-2):
    print(i)

#for i in range(10.5,-10,-2):  csak egész lehet !!
#    print(i)

for x in ["a","b"]:
    print(x)
    x *=10          # működik, de KERÜLD
    print(x)

elemek = [12,"Alam",23,"cica",2,23,4,(1,2)]

db = 1
for elem in elemek:
    print(db,elem)
    db = db + 1     # += 1
print("*"*10)
print(elemek[2])
print(elemek[0])

for i in range(8):
    print(elemek[i],end=", ")
print()