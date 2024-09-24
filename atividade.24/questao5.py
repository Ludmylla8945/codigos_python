import random

def lancamento_moeda():
    resultados = []
    
    while True:
        resultado = random.choice(["Cara", "Coroa"])
        resultados.append(resultado)
        print("Resultado do lançamento:", resultado)
        
        continuar = input("Deseja lançar a moeda novamente? (s/n): ")
        if continuar.lower() != 's':
            break

    print("Resultados dos lançamentos:", resultados)

lancamento_moeda()
