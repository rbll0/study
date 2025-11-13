tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefas.append({
        "Tarefa": nome_tarefa,
        "completa": False
    })
    print(f'Tarefa "{nome_tarefa}" adicionada com sucesso!')
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

    elif opcao == '6':
        print("Saindo do gerenciador de tarefas.")
        break
