lista = [2, 2, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10]

for i in lista:
    if(lista.count(i) > 1):
        while(lista.count(i) > 1):
            lista.remove(i)

print(lista)

