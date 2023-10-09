'''
print("Kérem a neved:",end=" ")
nev = input()
print("Szia "+nev)

nev = input("Kérem a neved2: ")
print("Szia "+nev+"!")

szam = input("Kérek egy egész számot 10 és 100 között: ")
print(szam)
print(szam*2)
print(type(szam))


szam = int(input("Kérek egy egész számot 10 és 100 között: "))
print(szam)
print(szam*2)
print(type(szam))

szam = float(input("Kérek egy egész számot 0 és 1 között: "))
print(szam)
print(szam*2)
print(type(szam))

szam = int(input("Kérek egy egész számot 1 és 100 között: "))

# + - / * ** % //
maradek = szam % 2
if maradek == 0 :
    print("Páros")
else:
    print("Páratlan")

szam = int(input("Kérek egy egész számot: "))
maradek = szam % 3
if maradek == 0 :
    print("Hárommal osztaható")
else:
    print("Hárommal nem osztaható")

szam = int(input("Kérek egy egész számot: "))
pozitiv = szam > 0
negativ = szam < 0
nulla   = szam == 0
# print(type(pozitiv),pozitiv)
if pozitiv :
    print("Pozizív")
if negativ :
    print("Negatív")
if nulla :
    print("Nulla")

if szam > 0 :
    print("Pozizív")
else:
    if szam < 0:
        print("Negatív")
    else:
        print("Nulla")

if szam > 0 :
    print("Pozizív")
elif szam < 0:
    print("Negatív")
else:
    print("Nulla")

szam = int(input("Kérek egy pozitív egész számot: "))
maradek2 = szam % 2
maradek3 = szam % 3

if maradek2 == 0 and  maradek3 != 0 :
    print("Kettővel osztható")
if maradek3 == 0 and  maradek2 != 0 :
    print("Hárommal osztható")
if maradek3 == 0 and  maradek2 == 0 :
    print("Hattal osztható")

if maradek2 == 0 and  maradek3 != 0 :
    print("Kettővel osztható")
elif maradek3 == 0 and  maradek2 != 0 :
    print("Hárommal osztható")
elif maradek3 == 0 and  maradek2 == 0 :
    print("Hattal osztható")

#if szam %2  == 0 and  szam %3 != 0 :
#    print("Kettővel osztható")

# and &&
print("-"*10)

if maradek2 == 0 or maradek3 == 0 :
    print("kettővel vagy hárommal osztható")
else:
    print("Se kettővel se hárommal nem osztható")
'''
if 1.9 :
    print(1)
if 0 :
    print(0)





