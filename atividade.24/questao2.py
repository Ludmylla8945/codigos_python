def notas_acima_da_media():
    notas = []
    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)
    
    media = sum(notas) / len(notas) if notas else 0
    acima_media = sum(1 for nota in notas if nota > 7)
    print("Quantidade de alunos com notas acima da média:", acima_media)

notas_acima_da_media()
