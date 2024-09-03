#Solicita a idade da pessoa em anos 
idade_anos = int(input("Digite sua idade em anos"))

#Converte a idade para meses e dias 
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365

#Exibe a idade convertida
print(f"Sua idade em meses é:{idade_meses}")
print (f"Sua idade em dias é:{idade_dias}")