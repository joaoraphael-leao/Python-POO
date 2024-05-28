matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

posicoes_diagonal = [0, 2]
soma = matriz[1][1]
#inicializando a soma das diagonais com o elemento central,
#contando como se fosse somada apenas uma vez

for i in posicoes_diagonal:
    for j in posicoes_diagonal:
        soma += matriz[i][j]

print(soma)