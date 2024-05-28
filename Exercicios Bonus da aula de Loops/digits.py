numero = int(input("Digite um numero"))
soma = 0
aux = None
while(numero > 0):
    aux = numero % 10

    soma += aux
    numero -= aux
    numero /= 10

print("A soma dos digitos desse numero eh ",soma)