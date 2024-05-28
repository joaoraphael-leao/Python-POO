import random as rd
number = rd.randint(1, 100)

guess = None
diference = None
while(1):
    guess = int(input("Escolha um numero de 1 a 100 "))
    diference = number - guess
    if(diference == 0):
        print("Voce acertou")
        break
    elif(diference < 0 and diference < -25):
        print("Esta muito acima")
    elif(diference < 0):
        print("Esta pouco acima")
    elif(diference <= 25 and diference > 0):
        print("Está pouco abaixo")
    else:
        print("Esta muito abaixo")
