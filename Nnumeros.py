# Solicita 6 números e armazena em uma lista
numeros = []
for i in range(6):
    numero = int(input(f"Digite o {i+1}º número: ")) #Em cada iteração, solicita ao usuário que insira um número. O número é convertido para inteiro (int) e armazenado na variável numero.
    numeros.append(numero) #Adiciona o número fornecido à lista numeros.

# Exibe a lista completa
print("Lista de números:", numeros) #Exibe a lista completa de números inseridos pelo usuário.

# Solicita duas posições
pos1 = int(input("Escolha a primeira posição (0 a 5): "))
pos2 = int(input("Escolha a segunda posição (0 a 5): "))

# Realiza as operações
num1 = numeros[pos1]
num2 = numeros[pos2]

soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2
divisao = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)" #Calcula a divisão de num1 por num2, mas apenas se num2 não for zero. Se num2 for zero, a divisão é "Indefinido (divisão por zero)" para evitar erro de divisão por zero.
exponenciacao = num1 ** num2 #Calcula num1 elevado à potência de num2.

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Diferença: {diferenca}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {exponenciacao}")
