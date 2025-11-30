from logica.funcoes import (
    carregar_tarefas, cadastrar_tarefa, listar_tarefas,
    atualizar_tarefa, remover_tarefa, gerar_relatorio
)
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    tarefas = carregar_tarefas()

    while True:
        limpar_tela()
        print("===== SISTEMA DE TAREFAS =====")
        print("1 - Cadastrar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Atualizar Tarefa")
        print("4 - Remover Tarefa")
        print("5 - Relatório")
        print("6 - Sair")
        print("===============================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
            input("\nENTER para continuar...")

        elif opcao == "2":
            listar_tarefas(tarefas)
            input("\nENTER para continuar...")

        elif opcao == "3":
            atualizar_tarefa(tarefas)
            input("\nENTER para continuar...")

        elif opcao == "4":
            remover_tarefa(tarefas)
            input("\nENTER para continuar...")

        elif opcao == "5":
            gerar_relatorio(tarefas)
            input("\nENTER para continuar...")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
            input("\nENTER para continuar...")


if __name__ == "__main__":
    menu()
