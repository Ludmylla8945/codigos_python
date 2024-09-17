objetos = ('Lápis','Borracha','Caderno')
print(objetos[1])

print(type(objetos))
print(objetos)

print("-"*50)
for item in range(0,3):
    print(objetos[item], end="," )#exibindo todos os itens da tupla


#Exibindo de outra forma os itens
print("")
print("-"*50)
for elementos in objetos:
    print(elementos)

#Iemos tentar alterar o conteudo da tupla
objetos[0] = "Caneta"    