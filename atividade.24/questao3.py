def gerenciar_eventos():
    eventos = []
    
    while True:
        acao = input("Digite 'adicionar' para adicionar um evento, 'remover' para remover, ou 'sair' para encerrar: ")
        
        if acao == 'adicionar':
            evento = input("Digite o evento para adicionar: ")
            eventos.append(evento)
        elif acao == 'remover':
            evento = input("Digite o evento para remover: ")
            if evento in eventos:
                eventos.remove(evento)
            else:
                print("Evento não encontrado.")
        elif acao == 'sair':
            break
        else:
            print("Ação inválida.")

        print("Eventos atuais:", eventos)

gerenciar_eventos()
