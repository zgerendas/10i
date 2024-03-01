'''
#1
knev = input("Kérem a keresztneved: ")
vnev = input("Kérem a vezeték neved: ")
teljes_nev = vnev+" "+knev
print("Üdvözöllek",teljes_nev)
print(f"Üdvözöllek {teljes_nev}")


#2
import random
szamok = list()
for _ in range (10):
    szamok.append(random.randint(1,10))

szamok = [random.randint(1,10) for i in range(10) ]

beSzam = int(input("Kérek egy egész számot 1 és 7 között: "))
if beSzam in szamok:
    print("A szám a listában volt.")
else:
    print("A szám nincs a listában.")

print("A lista: ",end="")
for sz in szamok:
    print(sz,end=", ")
print()

#3
f = open("szamok.txt","w")
for sz in szamok:
#    f.write(str(sz)+"\n")
    f.write(str(sz))
    f.write("\n")
f.close()


#4
def addSzor(a,b):
    return (a+b)*2

print(f"Eremeny: 2,3 -> {addSzor(2,3)}")
print("Eremeny: 2,3 -> "+str(addSzor(2,3)))
'''

#5
versenyzok = list()
fajl = open("snooker.txt")
fej = fajl.readline()
for sor in fajl:
#    print(sor.replace("\n","").split(";"))
    bontott = sor.replace("\n","").split(";")
    szotar = {
        "Helyezes":int(bontott[0]),
        "Nev":bontott[1],
        "Orszag":bontott[2],
        "Nyeremeny":int(bontott[3])
    }
    #print(szotar)
    versenyzok.append(szotar)
fajl.close()

#print(versenyzok)

print(f"5.2. feladat: A világranglistán {len(versenyzok)} versenyző szerepel")

osszeg = 0
for versenyzo in versenyzok:
    osszeg += versenyzo["Nyeremeny"]
print(f"5.3. feladat: A versenyzők átlagosan {osszeg/len(versenyzok)} fontot kerestek")

db = 0
for versenyzo in versenyzok:
    if versenyzo["Orszag"] == "Anglia":
        db += 1
print(f"5.4. feladta: {db}-en indultak Angliábol")

for versenyzo in versenyzok:
    if versenyzo["Helyezes"] == 1:
        print(versenyzo["Nev"])
        break
ismeteld = True
index = 0
while ismeteld:
    v = versenyzok[index] 
    if v["Helyezes"] == 1:
        ismeteld = False
    index +=1
print(v)

index = 0
while versenyzok[index]["Helyezes"] != 1:
    index += 1
print(v)





