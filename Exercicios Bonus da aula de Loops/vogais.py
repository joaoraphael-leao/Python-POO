string = input("Digite uma palavra ou frase ")
contador = 0
vogais = ['a','e','i','o','u']
for i in range(len(string)):
    if(string[i].lower() in vogais):
        contador += 1

print(f"A palavra possui {contador} vogais")