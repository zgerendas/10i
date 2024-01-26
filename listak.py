lista =[]
print(type(lista))
lista =list()
print(type(lista))

lista = [1,2,3,4,5]
print(len(lista))
print(sum(lista))

lista.append(10)
print(lista)

lista.append("Alma")
print(lista)
print(len(lista))
#print(sum(lista))

lista2 = ['a','b','c']
lista.append(lista2)
print(lista)
print(len(lista))

#lista.clear()

'''
l = lista
l.append(100)
print(lista)
a = 10
b = a
b = 11
print(a)
'''

l = lista.copy()
l.append(100)
print(l,lista,sep="\n")

print(lista.count(7))
print("Almaa".count('a'))

print(lista.index(5))
lista.insert(3,"szilva")
print(lista)

print(lista.pop(3))
print(lista)


#print(lista.pop(-1))
print(lista.pop(len(lista)-1))
print(lista)

lista.remove("Alma")
print(lista)

lista.append(5)
print(lista)
lista.remove(5)
print(lista)

print(lista[4])
lista[4] = 20
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

mondat = "Quis esse nulla ipsum sunt adipisicing reprehenderit eu Lorem tempor laboris ipsum cupidatat ut cupidatat."
