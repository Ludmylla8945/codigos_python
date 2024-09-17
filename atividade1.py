# Inicializa a lista para armazenar os valores
valores = []

# Loop para solicitar valores ao usuário
while True:
    # Solicita um valor ao usuário
    valor = int(input("Digite um valor (ou um número negativo para encerrar): "))
    
    # Se o valor for negativo, encerra o loop
    if valor < 0:
        break
    
    # Adiciona o valor à lista
    valores.append(valor)

# Exibe a lista criada
print("Lista criada:", valores)

# Remove todos os números pares da lista
valores = [x for x in valores if x % 2 != 0] #verifica se o número é ímpar.

# Exibe a lista após a remoção dos números pares
print("Lista após remover os números pares:", valores)
