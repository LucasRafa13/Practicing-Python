def add_task(tasks, name_task):
    task = {"name": name_task, "completed": False}
    print(f"\n A tarefa {name_task} foi adicionada com sucesso!")
    tasks.append(task)
    return


def list_tasks(tasks):
    print("\nTarefas:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else ""
        print(f"{i}. [{status}] {task['name']}")
        return


def update_task(tasks, i, new_name_task):
    new_i = int(i) - 1
    tasks[new_i]["name"] = new_name_task
    print(f"\nTarefa {i} atualizada para {new_name_task}...")
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
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        list_tasks(tasks)
        i = input("Digite o número da tarefa que deseja atualizar: ")
        new_name_task = input("Digite o novo nome da tarefa: ")
        update_task(tasks, i, new_name_task)
    elif choice == "6":
        print("Saindo do Gerenciador de Tarefas...")
        break
