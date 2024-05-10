'''
lista = list()
ismet = True
while ismet:
    be = input("Kérek.. :")
    if be == "":
        ismet = False
    else:
        lista.append(int(be))
print(lista)



db = 0
for elem in lista:
    if elem % 3 == 0:
        db += 1

print(db)

def parosok(lisa):
    plista = list()
    for elem in lisa:
        if elem % 2 == 0:
            plista.append(elem)
    return plista

print(parosok(lista))
print(lista)

x = 10
def teszt(a):
    a = a*a
    return a
print(teszt(x))
print(x)

def teszt2(x):
    x = x*x
    return x
print(teszt2(x))
print(x)


def minimum(li):
    m = li[0]
    for elem in li:
        if elem < m:
            m = elem
    return m
print(minimum(lista))

def mmaximum(li):
    m = li[0]
    for elem in li:
        if elem > m:
            m = elem
    return m
print(mmaximum(lista))
'''

lista =[1,2,33,-6,7]


def osszeg(li):
    ossz = 0
    for elem in li:
        ossz += elem
    return ossz
print(osszeg(lista))


def kicsi(li,db):  # db.-ik legkisebb vissza
    return sorted(lista)[db-1]

print(sorted(lista))
print(sorted(lista,reverse=True))
print(lista)

print(kicsi(lista,3))


def nagy(li,db):  # 
    return sorted(lista,reverse=True)[db-1]
print(nagy(lista,2))

'''
lista.remove(-6)
print(lista)
'''

def kicsi2(li,db):
  
    mi = min(li)
    print(li,db,mi)
    if db == 1:
        return mi
    else:
        li.remove(mi)
        db += -1
        kicsi2(li,db)
print(kicsi2(lista,3))
print(lista)
#print(kicsi2(lista,2))






