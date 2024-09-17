# Solicita valores ao usuário até um valor negativo ser inserido e cria a lista
lista = []
while (valor := int(input("Digite um valor (negativo para encerrar): "))) >= 0:
    lista.append(valor) # O := Atribui o valor retornado pela função int(input(...)) à variável valor e retorna esse valor para ser usado na condição do while.

# Exibe a lista completa
print("Lista completa:", lista)

# Cria e exibe uma nova lista apenas com números ímpares
lista_sem_pares = [numero for numero in lista if numero % 2 != 0] # Isso itera sobre cada item (número) na lista e o entre chaves é uma condição que filtra os números. 
print("Lista sem números pares:", lista_sem_pares)
