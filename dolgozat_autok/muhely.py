'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

#print(autok)

oreg = autok[0]
for au in autok:
    if oreg['kor'] < au['kor']:
        oreg = au   
print('------------- 3.a feladat -------------')
print(f" A legöregebb autó: {oreg['rendszam']}, {oreg['marka']} {oreg['tipus']}, {oreg['kor']} éves.")

osszeg = 0
db = 0
for auto in autok:
    osszeg += auto['koltseg']
    db += 1

print('------------- 3.b feladat -------------')
print(f'Az egy autóra jutó átlagos javítási költség: {osszeg/db} Ft.')
print(f'Az egy autóra jutó átlagos javítási költség: {osszeg/len(autok)} Ft.')

print('------------- 3.c feladat -------------')
rendszam = input('Adjon meg egy rendszámot (pl. ABC-123)! ')
'''
van = False
for auto in autok:
    if rendszam == auto['rendszam']:
        van = True

van = False
for auto in autok:
    if rendszam == auto['rendszam']:
        van = True
        break
'''
van = False
index = 0
while not van and index < len(autok):
    if autok[index]['rendszam'] != rendszam:
        index += 1
    else:
        van = True

if van:
    print('A megadott rendszámú autó a műhelyben van.')




