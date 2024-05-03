lista = list()

ismet = True
while ismet:
    szam = input("Kérek...")
    if szam == "":
        ismet =False
    else:
        lista.append(int(szam))

print(lista)


def nagy(li):
    m = li[0]
    for elem in li:
        if m < elem:
            m = elem
    return m
print(nagy(lista))

def kis(li):
    m = li[0]
    for elem in li:
        if m > elem:
            m = elem
    return m
print(kis(lista))

def harommal(li):
    db = 0
    for elem in li:
        if elem % 3 == 0:
            db +=1
    return db


