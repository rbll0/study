tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefas.append({
        "tarefa": nome_tarefa,
        "completa": False
    })
    print(f'Tarefa "{nome_tarefa}" adicionada com sucesso!')
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas):
        stats = "Concluída" if tarefa["completa"] else "Pendente"
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice + 1}. [{stats}] {nome_tarefa}")
    return

def atualizar_tarefa(tarefas, indice, novo_nome):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["tarefa"] = novo_nome
        print(f"Tarefa {indice} atualizada para {novo_nome}" )
    else:
        print("Índice inválido.")
            
    return

while True:

    print("\nMenu do Gerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Remover Tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção (1-6): ")

    if opcao == '1': 
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif opcao == '2':
        ver_tarefas(tarefas)    

    elif opcao == '3':
        ver_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice, novo_nome)
    elif opcao == '6':
        print("Saindo do gerenciador de tarefas.")
        break
