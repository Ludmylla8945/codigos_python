animais =  ["Cachorro", "Gato", "Ovelha"]
print(type(animais))

print(animais)

#Exibindo todos os itens da lista
print("-"*50)
for itens in animais:
    print(itens)

#Atualizando dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2 modo de atualiizar
print("-"*50)
#fORMA 1- USANDO APPEND
animais.append("Cavalo")#irá inserir um novo item no final da lista
print(animais)

#2º Forma - Usando Insert
animais.insert(1, "Pássaro") #O insert precisa de 2 valores, o 1º será o indice que desejo inserir o valor e o 2º é o que eu quero inserir na lista 
print(animais)

#3º Forma - Usando Pop
print("-"*50)
animais.pop()#Remove o ultimo
print(animais)

# Forma 2 - Usando Pop com indice
animais.pop(0)# Aqui iremos escolher qual indice da lista sera excluido
print(animais)

#3º Forma - Usando remove
animais.remove("Ovelha")
print(animais)