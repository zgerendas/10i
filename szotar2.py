mondat = "Voluptate consectetur nisi qui officia voluptate eiusmod eiusmod amet."

betuk = dict()
#mondat = mondat.lower()
#mondat = mondat.replace(".","")
mondat = mondat.lower().replace(".","").replace(" ","")
print(mondat)

for k in mondat:
    #print(k)
    #print(betuk.get(k))
    if betuk.get(k) == None:
        betuk.update({k:1})   
    else:
        betuk.update({k:betuk.get(k)+1})   
print(betuk)
'''
betuk.clear()
for k in mondat:
    db = betuk.get(k)
    if db == None:
        betuk.update({k:1})   
    else:
        betuk.update({k:db + 1})   
print(betuk)

print(betuk.items())
for kulcs,elem in betuk.items():
    print(kulcs,elem,end="; ")
print()
#betuk.pop('v')
#print(betuk)
    
#print(betuk.popitem())
#print(betuk.popitem())
#print(betuk)

#betuk.setdefault('zz','nincs')
#print(betuk)

karakter = input("Kérek egy betűt: ")
if betuk.get(karakter) == None:
    print("A "+karakter+" nem szerepel a mondatban.")
else:
    print("A "+karakter+" "+str(betuk.get(karakter))+" alaklommal szerepel a mondatban.")

#print('v' in betuk.keys())
#print('V' in betuk.keys())
if karakter in betuk.keys():
    print("A "+karakter+" nem szerepel a mondatban.")
else:
    print("A "+karakter+" "+str(betuk.get(karakter))+" alaklommal szerepel a mondatban.")

valid ="qwertzuiopasdfghjklyxcvbnm"
#print(sorted(valid))
valid = sorted(valid)

while True: # még hibás
    karakter = input("Kérek az angol ABC-ből egy betűt: ")
    if karakter in valid:
        break

ismeteld = True
while ismeteld:
    karakter = input("Kérek az angol ABC-ből egy betűt: ").lower()
    
    if karakter in valid:
        ismeteld = False
    else:
        print("Nem agol betűt adtál meg!")
'''
max = 0
gyakori = ""
for k,e in betuk.items():
    if e > max:
        max = e
        gyakori = k
print(max,gyakori)