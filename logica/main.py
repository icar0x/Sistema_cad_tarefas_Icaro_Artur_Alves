from funcoes import (
    carregar_produtos,
    salvar_produtos,
    cadastrar_produto,
    listar_produtos,
    atualizar_produto,
    excluir_produto
)


def menu():
    print("\n====== SISTEMA DE PRODUTOS ======")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("0 - Sair")
    print("=================================")


def main():
    categorias = ("Comida", "Limpeza", "Bebidas", "Higiene", "Cosméticos")
    produtos = carregar_produtos()
    codigo_cad = {p["codigo"] for p in produtos}

    while True:
        menu()

        try:
            opcao = int(input("Escolha: "))
        except Exception:
            print(" Opção inválida.")
            continue

        if opcao == 1:
            produtos = cadastrar_produto(produtos, codigo_cad, categorias)
            salvar_produtos(produtos)

        elif opcao == 2:
            listar_produtos(produtos)

        elif opcao == 3:
            produtos = atualizar_produto(produtos)
            salvar_produtos(produtos)

        elif opcao == 4:
            produtos = excluir_produto(produtos, codigo_cad)
            salvar_produtos(produtos)

        elif opcao == 0:
            print("Saindo do sistema... Obrigado!")
            break

        else:
            print(" Opção inválida.")


if __name__ == "__main__":
    main()
