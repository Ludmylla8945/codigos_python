import datetime

# Obter o ano atual
ano_atual = datetime.datetime.now().year

# Inicializar a variável do ano de nascimento
ano_nascimento = 0

# Loop para solicitar o ano de nascimento até que o candidato tenha 18 anos ou mais
while True:
    # Solicitar o ano de nascimento do candidato
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    
    # Calcular a idade
    idade = ano_atual - ano_nascimento
    
    # Verificar se a idade é suficiente para se inscrever
    if idade >= 18:
        print("Inscrição realizada com sucesso!")
        break
    else:
        print("Você deve ter 18 anos ou mais para se inscrever. Tente novamente.")
