fajl = open("ub2017egyeni.txt")

#print(fajl.read())

#print(fajl.readline())
#print(fajl.readline())

#print(fajl.readlines())
#print("*"*10)
#print(fajl.readline())

versenyzok = list()
fejlec = fajl.readline()
for sor in fajl:
    #print(sor.replace("\n","").split(";"))
    listaSor = sor.replace("\n","").split(";")
    #print(listaSor[0])
    versenyzo = {"nev":listaSor[0],"Rajtszam":listaSor[1],"Kategoria":listaSor[2],"Versenyido":listaSor[3],"TavSzazalek":int(listaSor[4])}
    #print(versenyzo)
    versenyzok.append(versenyzo)
fajl.close()
# print(fajl.readline()) !!!! Hiba

#print(versenyzok)

f = open("versenyzok.txt","w")

for v in versenyzok:
    #print(v["nev"])
    f.write(v["nev"])
    f.write("\n")
f.close()

ferfi = 0
for v in versenyzok:
    if v["Kategoria"] == "Ferfi":
        ferfi += 1
print(ferfi)
print(len(versenyzok)-ferfi)

teljes = 0
for v in versenyzok:
    if v["TavSzazalek"] == 100:
        teljes += 1
print(teljes)

minimum = 100
rovid =""
for v in versenyzok:
    if v["TavSzazalek"] < minimum :
        minimum = v["TavSzazalek"]
        rovid = v["nev"]
print(rovid,minimum)
