numero = int(input("Digite um numero "))
aux = numero

fatorial = 0

if(numero > 0):
    fatorial = 1

while(numero > 1):
    fatorial *= numero
    numero -= 1

print(f"O fatorial do numero {aux} eh {fatorial}")