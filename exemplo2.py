nome = "Ludmylla Melo"
endereco = "Cond Riviera Cohtrac"
idade = 17

# print(nome, endereco, idade)
# 1ª forma de concatenação
print("Olá ",nome, "seu endereço é", endereco, "sua idade é", idade)

#2ª forma de concatenação
print("Seja bem vindo {} sua residencia está na {} e você possui {} anos".format(nome,endereco,idade)) 

#3ª forma de concatenação - f string
print(f"Olá seja bem vindo {nome} o seu endereço é {endereco} e sua idade é {idade}")