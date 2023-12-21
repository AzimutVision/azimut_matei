variabila_1 = 1
variabila_2 = 35


print(variabila_1)
print(variabila_2)
# scadere
print(variabila_2 - variabila_1)
"""
comentariu
comment
"""
variabila_float = 23.4
text_1 = "alex"
text_2 = " eric merge"

print(text_1 + text_2)
v1 = 2
v2 = 1
v3 = "A"
v4 = v1 + v2
print(v4)
print(f"{v1+v2}={v3}")
print(v3 , "=" ,v4)

lista = ["nda",4,v2,v4+v1]
print(lista)
print(lista[3] + lista[2])
lista.append("and")
lista.append(lista[3]+lista[2])
print(lista)
lista.insert(4, "treizeci")
print(lista)
lista.insert(3, lista[3]+lista[6])
print(lista)
lista2 =["nad",7,8,21]
lista.extend(lista2)
lista2.extend(lista)
print(lista)
print(lista2)
lista2[3] = "opt"
lista2[2] = "sapte"
print(lista2)
del lista2[7]
print (lista2)
print(lista2[3:10:2])
print(lista2[4:7])
print(lista2[-4:14])
print("lista2 contine:" ,len(lista2), "elemente")
lista3 = ("cnd",55,65,"zbn")
print(lista3)

dictionar = {
    "nume": "Lazea",
    "varsta": 50,
    "casa": "garsoniera"
}
print(dictionar)
dictionar["nume"] = "Andrei"
print(dictionar)
dictionar["lista"] = lista2
print (dictionar)
print("varsta =",dictionar.get('varsta'))