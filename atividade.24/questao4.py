import random

def jogo_palavra():
    palavras = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 
                'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo']
    
    random.shuffle(palavras)
    palavra_selecionada = random.choice(palavras)
    posicao = palavras.index(palavra_selecionada)
    tentativas = 3

    print("Palavras embaralhadas:", palavras)
    print("Adivinhe a posição da palavra (0 a 14). Você tem 3 tentativas.")

    while tentativas > 0:
        tentativa = int(input("Qual é a posição da palavra? "))
        if tentativa == posicao:
            print("Parabéns! Você acertou!")
            break
        else:
            tentativas -= 1
            print(f"Você errou! Tentativas restantes: {tentativas}")
    
    if tentativas == 0:
        print("Você perdeu! A posição correta era:", posicao)
    
    print("Lista embaralhada:", palavras)

jogo_palavra()
