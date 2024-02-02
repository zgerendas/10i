'''
v = {}
print(type(v))
halmaz = set()
print(type(halmaz))
halmaz.add(1)
halmaz.add(2)
halmaz.add(2)
print(halmaz)

lista = list()
lista.append(1)
lista.append(2)
lista.append(2)
print(lista)


szotar = dict()
print(type(szotar))

t = tuple()
print(type(t))
'''
'''
szemely = { "nev": "Zalán", "kor": 18}
print(szemely)

print(szemely["nev"])
print(szemely["kor"])
szemely["nev2"]="Pista"
print(szemely)
szemely["kor"]=34
print(szemely)

print(len(szemely))

szoveg = "In exercitation amet qui fugiat sint eu aliqua incididunt consectetur laboris velit exercitation do incididunt."


s = szoveg.replace('.','')
print(s)

lista = s.split(" ")
print(lista)

szotar = dict()
i = 1
for elem in lista:
    szotar[i] = elem
    i +=1
print(szotar)

szotar.update({1:"Alma"}) # szotar[1] = "Alma"
print(szotar)

szotar.update({0:"Körte"})
print(szotar)


print(szotar.fromkeys(range(2,5)))
print(szotar.fromkeys(range(2,5),"p"))

print(szotar.get(10))
print(szotar.get(101))
print(szotar[10])
# print(szotar[101])

for elem in szotar:
    print(elem,end=", ")
print()

for elem in szotar:
    print(elem,szotar[elem],end=", ")
print()

for elem in szotar.values():
    print(elem,end=", ")
print()

for elem,ertek in szotar.items():
    print(elem,ertek,end=", ")
print()

print(szotar.values())
print(szotar.items())
'''

tanulok = list()

szemely ={"név":"Pista","kor":14}
tanulok.append(szemely)

# print(szemely)
szemely ={"név":"Ági","kor":15}
tanulok.append(szemely)

szemely ={"név":"Ákos","kor":14}
tanulok.append(szemely)

print(tanulok)

for t in tanulok:
    print(t["név"])

kor = int(input("Kérek egy életkort: "))
for t in tanulok:
    if t["kor"] == kor:
        print(t["név"])

for t in tanulok:
    t["kor"] +=1
print(tanulok)

osszeg = 0
db = 0
for t in tanulok:
    osszeg += t["kor"]
    db += 1
print(osszeg/db)
print(osszeg/len(tanulok))


