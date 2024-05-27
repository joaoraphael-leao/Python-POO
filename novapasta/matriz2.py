matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
size = len(matriz)
for i in range(size):
    for j in range(len(i)):
        if(i == j):
            print(lista[i][j])