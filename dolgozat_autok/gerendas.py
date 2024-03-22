#1
'''
szamok = list()
while True:
    be = input("Kérek egy számot: ")
    if be == "":
        break
    else:
        szamok.append(float(be))
print(szamok)

szamok = list()
ismeteld = True
while ismeteld:
    be = input("Kérek egy számot: ")
    if be == "":
        ismeteld = False
    else:
        szamok.append(float(be))
print(szamok)

szamok = list()
be = 0
while not be == "":
    be = input("Kérek egy számot: ")
    if be != "":
        szamok.append(float(be))
print(szamok)

print("------------- 1. feladat -------------")
print(f"A listában {min(szamok)} a legkisebb.")
print(f"A listában {max(szamok)} a legnagyobb.")

mini = szamok[0]
for szam in szamok:
    if szam < mini:
        mini = szam

maxi = szamok[0]
for szam in szamok:
    if szam > maxi:
        maxi = szam
print("------------- 1. feladat -------------")
print(f"A listában {mini} a legkisebb.")
print(f"A listában {maxi} a legnagyobb.")

'''
def harommal_oszthatok(lista):
    db = 0
    for elem in lista:
        if elem % 3 == 0:
            db += 1
    return db
#print(harommal_oszthatok([1,2,3,6]))
#2.b
import random
szamok = list()
for _ in range(20):
    szamok.append(random.randint(1,100))
#print(szamok)
print("------------- 2.c feladat -------------")
print(f"A listában {harommal_oszthatok(szamok)} darab hárommal osztható szám szerepelt.")

db = sum(1 for szam in szamok if szam % 3 == 0)
print(db)




