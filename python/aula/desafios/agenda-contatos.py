agenda = []
def adicionar_contato(agenda,nome,telefone,email):
    agenda.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    } )
    print(f'Contato "{nome}" adicionado com sucesso!')
    return

def ver_contatos(agenda):
    print("/nLista de contatos")
    for indice, agenda in enumerate(agenda):
        stats = "Favorito" if agenda["favorito"] else ""
        nome = agenda["nome"]
        print(f"{indice + 1}. [{stats}] Nome: {nome} | Telefone:{telefone} | Email:{email} ")
    return

def editar_contatos(agenda,indice, nome, telefone, email):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        agenda[indice_ajustado] ["nome"] = nome
        agenda[indice_ajustado] ["telefone"] = telefone
        agenda[indice_ajustado] ["email"] = email

        print(f"Contato {indice} atualizado com sucesso !!")
    else:
        print("Índice inválido")    
    return

def favoritar_contato(agenda, indice):
    indice_ajustado = int(indice) - 1
    if(indice_ajustado >= 0 and indice_ajustado < len(agenda)):
        agenda[indice_ajustado] ["favorito"] = True
        print(f"Contato {indice} marcado como favorito !!")
    else:
        print("Índice inválido ")



while True: 
    print("\nMenu da Agenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Ver Contatos Cadastrados")
    print("3. Editar Contato")
    print("4. Marcar Contato como Favorito")
    print("5. Remover Contato")
    print("6. Sair")

    opcao = input("Escolha uma opção (1-6): ")
    
    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(agenda, nome, telefone, email)

    if opcao == '2':
        ver_contatos(agenda)    

    if opcao == '3':
        ver_contatos(agenda)
        indice = input("Digite o número do contato que deseja atualizar: ")
        nome = input("Digite o novo nome: ")
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo email: ")    
        editar_contatos(agenda,indice, nome, telefone, email)

    if opcao == '4':
        ver_contatos(agenda)    
        indice = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(agenda, indice)

    elif opcao == '6':
        print("Saindo da agenda de contatos. Até mais!")
        break
