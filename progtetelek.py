import random

def listaGen(darab,tol=1,ig=100):
    lista = list()
    for i in range(darab):
        lista.append(random.randint(tol,ig))
    return lista

lista = listaGen(10,1,45)
print(lista)
lista = listaGen(10,50,200)
print(lista)

lista = listaGen(10,60)
print(lista)

# megszamolás
def megszamol(listam):
    db = 0
    for elem in listam:
        if elem > 50:
            db += 1
    return db

print(f"{megszamol(lista)} volt 50-nél nagyobb")

# eldöntés
volt = False
for elem in lista:
    if elem > 90:
        volt = True
if volt:
    print("Volt")
else:
    print("Nem volt 90-nél nagyobb")

# eldötés v2
volt = False
for elem in lista:
    #print(elem)
    if elem > 90:
        volt = True
        break
if volt:
    print("Volt")
else:
    print("Nem volt 90-nél nagyobb")

# eldötés v3
volt = False
i = 0
while not volt and i < len(lista):
    # print(lista[i])
    if lista[i] > 90:
        volt =True
    i += 1

if volt:
    print("Volt")
else:
    print("Nem volt 90-nél nagyobb")









