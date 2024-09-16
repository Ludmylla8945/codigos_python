#1° forma de ultilizar while - semelhante ao FOR

contador = 1 

while contador <= 5:
    print (contador)
    contador = contador +1 

#2º forma de ultilizar enquanto - loop condicional normal
valor = 0

while valor >=0: 
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar:)"))

    print(f"Voce digitou {valor}")

    print ("="*40)

    #3º forma de ultilizar o enquanto - semelhante a estrutura faça..enquanto 
    while True:
        senha = input("Informe sua senha: ") 
        print("Parabéns, senha correta")
        break #forma de encerra o lopp

    else:
        print("Senhas, não conferem, tente novamente")