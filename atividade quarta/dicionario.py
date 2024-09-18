#Criando um dicionario, sendo uma lista com indice textual
pessoa = {
    'Nome':'Maria',
    'Idade':20,
    'Endereco':'Avenida 23'
}

print(pessoa)

#Exibindo as chaves ultilizando o comando keys
print(pessoa.keys())

#Exibindo valores ultilizando o comando values()
print(pessoa.values())

#Exibindo tanto chave quanto valor
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")


#Adicionando dados
#Forma 1
pessoa["Peso"] = 98
print(pessoa)

#Forma 2 - usando update
pessoa.update({"Profissão" : "Diretora"})

#Removendo os itens
#1 Forma
pessoa.pop("Peso")
print(pessoa)

#Forma 2
del(pessoa["Endereco"])
print(pessoa)