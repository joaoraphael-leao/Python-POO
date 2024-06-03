from utils import stages, desenho_final, opcoes_de_paises, introducao, opcoes_de_jogo, alfabeto
from functions import palavra_correta, jogo
import random

#Mensagem de introducao + uma serie de opcoes de paises
print(introducao)
paises = opcoes_de_paises
quantidade_de_opcoes = len(paises)

palavra_a_adivinhar = paises[random.randint(0, quantidade_de_opcoes - 1)] # -1 por que a lista comeca a ser contada do 0

tamanho_da_palavra = len(palavra_a_adivinhar)
palavra_oculta = list('_' * tamanho_da_palavra)  # cria uma lista de caracteres, para manipular os elementos com base no indice
letras_usadas = []

contador_de_erros = 0
acabou_o_jogo = False

while not acabou_o_jogo:
    if contador_de_erros == 6:
        print("Você Perdeu")
        print(desenho_final)
        acabou_o_jogo = True

    elif '_' not in palavra_oculta:
        print("Parabens, Você Venceu!")
        acabou_o_jogo = True

    else:
        opcao = input(opcoes_de_jogo)

        if(opcao.lower() == 'p'):
            tentativa = input("Qual voce acha que eh o pais ?")

            if(tentativa.lower() == palavra_a_adivinhar.lower()):
                print("Voce venceu")
                acabou_o_jogo = True
            else:
                print("Voce perdeu")
                print(desenho_final)
                acabou_o_jogo = True

        else:
            contador = jogo(letras_usadas, palavra_a_adivinhar, palavra_oculta, contador_de_erros)
            print(f"Atualmente, a palavra está assim: {''.join(palavra_oculta)}\n\n")

