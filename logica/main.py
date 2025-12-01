from funcoes import (
    carregar_tarefas,
    salvar_tarefas,
    criar_tarefa,
    listar_tarefas,
    atualizar_tarefa,
    excluir_tarefa
)


def menu():
    print("\n========== SISTEMA CRUD ==========")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")
    print("==================================")


def main():
    tarefas = carregar_tarefas()

    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except Exception:
            print("Digite apenas números.")
            continue

        # Criar
        if opcao == 1:
            titulo = input("Título: ")
            descricao = input("Descrição: ")

            tarefas = criar_tarefa(tarefas, titulo, descricao)
            salvar_tarefas(tarefas)

        # Listar
        elif opcao == 2:
            listar_tarefas(tarefas)

        # Atualizar
        elif opcao == 3:
            try:
                id_tarefa = int(input("ID da tarefa: "))
            except Exception:
                print("ID inválido.")
                continue

            novo_titulo = input("Novo título: ")
            nova_desc = input("Nova descrição: ")

            if atualizar_tarefa(tarefas, id_tarefa, novo_titulo, nova_desc):
                salvar_tarefas(tarefas)
                print("Tarefa atualizada!")
            else:
                print("Tarefa não encontrada ou título inválido.")

        # Excluir
        elif opcao == 4:
            try:
                id_tarefa = int(input("ID da tarefa: "))
            except Exception:
                print("ID inválido.")
                continue

            if excluir_tarefa(tarefas, id_tarefa):
                salvar_tarefas(tarefas)
                print("Tarefa excluída!")
            else:
                print("Tarefa não encontrada.")

        # Sair
        elif opcao == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
