numero = 0
contador = 0
montante_total = 0

while(1):
    numero = float(input("Adicione um numero à sequencia "))
    if(numero < 0):
        break
    contador += 1
    montante_total += numero
    print(f"Atualmente, a media da sua sequencia eh {montante_total / contador}")