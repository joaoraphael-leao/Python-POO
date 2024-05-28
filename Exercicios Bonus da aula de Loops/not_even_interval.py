numero_1 = int(input("Digite o primeiro numero do intervalo "))
numero_2 = int(input("Digite o segundo numero do intervalo "))

aux = numero_1
numero_1 += 1 #a questao pede todos os numeros impares ENTRE eles

if(numero_1 % 2 == 0):
    numero_1 += 1
print(f"Esses sao os impares entre {aux} e {numero_2}:")
while(numero_1 <= numero_2):
    print(numero_1)
    numero_1 += 2

