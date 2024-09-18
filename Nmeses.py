# Lista dos meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

# Solicita as temperaturas dos 12 meses e armazena na lista
for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: ")) #solicita ao usuário que insira a temperatura média para o mês correspondente (usando o índice i para acessar o mês da lista meses).
    temperaturas.append(temp)

# Calcula a média anual
soma = 0
for temp in temperaturas:
    soma += temp
media_anual = soma / 12

# Exibe a média anual
print(f" Média anual das temperaturas: {media_anual:.2f}°C") #Exibe a média anual das temperaturas, formatada com duas casas decimais usando :.2f.


# Mostra as temperaturas acima da média e os meses correspondentes
print("\nMeses com temperatura acima da média anual:") #O \n é usado para dar espaço na mensagem
for i in range(12): # loop for percorre os 12 meses.
    if temperaturas[i] > media_anual: #Para cada índice i, verifica-se a temperatura do mês correspondente (temperaturas[i]) é maior que a média anual (media_anual).
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")


