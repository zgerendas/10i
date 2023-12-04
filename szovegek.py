mondat = "Ea esse eiusmod qui ea proident reprehenderit."
print(len(mondat)) 
print(mondat.count(" ")+1)

lista = mondat.split(" ")
print(lista)
print(len(lista))

mondat = "    Ea     esse    eiusmod qui ea proident reprehenderit.    "
lista = mondat.split(" ")
print(lista)
print(len(lista))

db = 0
for szo in lista:
    if szo != '':
        db += 1
print(db)


#print(mondat)
#print(mondat.replace("  "," "))

while len(mondat) > len(mondat.replace("  "," ")):
   # print(mondat)
    mondat = mondat.replace("  "," ")

print(mondat)

print(mondat.startswith(" "))
print(mondat.endswith("."))

if mondat.startswith(" "):
    #print("--"+mondat.replace(" ","",1)+"--")
    mondat = mondat.replace(" ","",1)

#print("--"+mondat.replace(" ","",2)+"--")
#print(mondat[1])
#print(mondat[-2])

print("--"+mondat.replace(mondat[-2]+" ",".")+"--")



print(lista)
lista2 = lista.copy()

hossz = 0
oldHossz = len(lista)
while oldHossz > hossz:
    oldHossz = len(lista)
    if lista.count('') > 0:
        lista.remove('')
    hossz = len(lista)
print(lista)
print(lista2)

a = 12
b = a
a = 23
print(b)
