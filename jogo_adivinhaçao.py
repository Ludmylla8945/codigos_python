import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializar o número de tentativas
tentativas_restantes = 5

print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")
print(f"Você tem {tentativas_restantes} tentativas.")

while tentativas_restantes > 0:
    # Solicitar ao usuário para digitar um palpite
    palpite = int(input("Digite seu palpite: "))
    
    # Verificar se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")
    
    # Atualizar o número de tentativas restantes
    tentativas_restantes -= 1
    print(f"Você tem {tentativas_restantes} tentativas restantes.")

if tentativas_restantes == 0:
    print(f"Você esgotou suas tentativas. O número secreto era {numero_secreto}.")
