'''
1.
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. 
Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! 
Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!

2.
Írj egy programot ami (Akasztófa játék alapja):
Egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót.
A felhasználónak többször is legyen lehetősége újabb tippet megadnia. 
A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt vagy az összes betűt kitalálta!

3.
A program kérjen be egy szöveget!

Határozza meg és írja ki a képernyőre, hogy
- az adott szövegben volt-e,
- ha igen akkor hány darab,
- és hányadik helyen / helyeken (a legelső hely az egyes számú)
”a”, ”e”, ”i” , ”o” vagy ”u” magánhangzó!

Mindegyik magánhangzóra külön-külön adja meg az információkat!

4.
A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van az alábbi listában 
A képernyőre írja is ki a feltételnek megfelelő szavakat!

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

'''
import random
szamok = list()
for i in range(5):
    szamok.append(random.randint(1,7))
be = int(input("Kérek egy számot: "))
if szamok.count(be) > 0:
    print("A",be,"szám a listában előfordul.")
    print("A lista:",szamok)

# 2
szavak = ["ajtó","ablak","szék","asztal","ceruza"]
szo = szavak[random.randint(0,4)]
print(szo)
ismetel = True
while ismetel:
    betu = input("Kérek egy betűt: ")
    if betu == "":
        ismetel=False
    else:
        if szo.count(betu) >0 :
            print(betu, "a szóban van")
        else:
            print(betu, "nincs a szóban van")
# 3
szoveg = input("Kérek egy szöveget: ")
# 3.a
if szoveg.count("e"):
    print(szoveg.count("e"),"darab e betű volt")
    print(szoveg.index("e")+1,"helyen volt")
else:
    print("Nincs e betű")

if szoveg.count("a"):
    print(szoveg.count("a"),"darab a betű volt")
    print(szoveg.index("a")+1,"helyen volt")
else:
    print("Nincs a betű")
# .......

# 3b
magan = ["a", "e", "i" , "o" ,"u"]
for c in magan:
    if szoveg.count(c):
        print(szoveg.count(c),"darab",c,"betű volt")
        print(szoveg.index(c)+1,"helyen volt")
    else:
        print("Nincs",c,"betű")

#4
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
db = 0
for szo in szavak:
    if szo.upper().startswith("A"):
        db +=1
print(db)