def palavra_correta(letra_atual, palavra_a_adivinhar, palavra_oculta):
    print("Essa letra estava na palavra, muito bem")

    for i in range(len(palavra_a_adivinhar)):
        if letra_atual == palavra_a_adivinhar[i].lower():
            palavra_oculta[i] = letra_atual

def jogo(letras_usadas, palavra_a_adivinhar, palavra_oculta, contador_de_erros):

    aviso_alfabeto = "Voce precisa digitar uma letra "
    aviso_caractere = "Digite apenas um caractere para tentar"
    aviso_letra_repetida =  f"{letras_usadas} Você não pode usar mais nenhuma dessas letras, pois já foram usadas: "

    letra_atual = input("Digite uma letra que você acha que está na palavra: ").lower()

    while (letra_atual not in alfabeto.lower()) or len(letra_atual) > 1 or letra_atual in letras_usadas:
        print("Por favor, que seu palpite cumpra os 3 requisitos abaixo:")
        print(aviso_alfabeto)
        print(aviso_caractere)
        print(aviso_letra_repetida)
        letra_atual = input("Agora digite seu palpite corretamente ")
    letras_usadas.append(letra_atual)

    if letra_atual in palavra_a_adivinhar.lower():
        palavra_correta(letra_atual, palavra_a_adivinhar.lower(), palavra_oculta)
    else:
        contador_de_erros += 1
        print("Que pena, essa letra não está no nome desse país")
        print(stages[contador])

    return contador_de_erros
