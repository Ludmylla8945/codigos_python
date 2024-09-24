def intersecao_listas():
    lista1 = list(map(int, input("Digite os números da primeira lista (separados por espaço): ").split()))
    lista2 = list(map(int, input("Digite os números da segunda lista (separados por espaço): ").split()))
    
    intersecao = sorted(set(lista1) & set(lista2))
    print("Números em comum (ordem crescente):", intersecao)

intersecao_listas()
