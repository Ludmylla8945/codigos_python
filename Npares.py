# Inicializa uma lista vazia para armazenar os valores
valores = []

# Solicita valores do usuário até que um valor negativo seja inserido
while True:
    entrada = input("Digite um valor (ou um valor negativo para encerrar): ")
    
    # Converte a entrada para float
    valor = float(entrada)
    
    # Verifica se o valor é negativo para encerrar o loop
    if valor < 0:
        break
    
    # Adiciona o valor à lista
    valores.append(valor)

# Exibe a lista criada
print("\nLista criada:")
print(valores)

# Inicializa uma nova lista para armazenar valores ímpares
valores_filtrados = []

# Itera sobre a lista para remover os números pares
for valor in valores:
    if valor % 2 != 0: #Remove os numeros pares e != é um operador de comparação que significa "diferente de".
        valores_filtrados.append(valor)

# Exibe a lista após remoção dos números pares
print("\nLista após remoção dos números pares:")
print(valores_filtrados)


