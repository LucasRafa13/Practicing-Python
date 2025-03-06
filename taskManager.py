def add_task(tasks, name_task):
    task = {"name": name_task, "completed": False}
    tasks.append(task)
    print(f"Task {name_task} adicionada com sucesso!")
    return


tasks = []

while True:
    print("\nMenu do Gerenciador de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    choice = input("Digite a opção desejada: ")

    if choice == "1":
        name_task = input("Digite o nome da tarefa: ")
        add_task(tasks, name_task)
    elif choice == "6":
        print("Saindo do Gerenciador de Tarefas...")
        break
