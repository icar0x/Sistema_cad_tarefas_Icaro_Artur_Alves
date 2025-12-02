import json
import os


def carregar_produtos(arquivo="produtos.json"):
    """Carrega os produtos do arquivo JSON."""
    try:
        if not os.path.exists(arquivo):
            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        print("Erro ao carregar o arquivo de produtos.")
        return []


def salvar_produtos(produtos, arquivo="produtos.json"):
    """Salva os produtos no arquivo JSON."""
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(produtos, f, indent=4)
    except Exception:
        print("Erro ao salvar produtos.")


def cadastrar_produto(produtos, codigo_cad, categorias):
    """Cadastra um novo produto com validações e tratamento de erros."""

    try:
        codigo = int(input("Código do produto: "))
        if codigo in codigo_cad:
            print(" Código já cadastrado.")
            return produtos
    except Exception:
        print(" Código inválido.")
        return produtos

    nome = input("Nome do produto: ").strip()
    if not nome:
        print(" O nome não pode ser vazio.")
        return produtos

    try:
        preco = float(input("Preço: "))
    except Exception:
        print(" Preço inválido.")
        return produtos

    try:
        quantidade = int(input("Quantidade em estoque: "))
    except Exception:
        print(" Quantidade inválida.")
        return produtos

    print("\nCategorias disponíveis:")
    for i, c in enumerate(categorias, start=1):
        print(f"{i} - {c}")

    try:
        escolha = int(input("Escolha a categoria (número): "))
        categoria = categorias[escolha - 1]
    except Exception:
        print(" Categoria inválida.")
        return produtos

    novo = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
    }

    produtos.append(novo)
    codigo_cad.add(codigo)

    print("✅ Produto cadastrado com sucesso!")
    return produtos


def listar_produtos(produtos):
    """Lista todos os produtos cadastrados."""
    try:
        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        print("\n=== LISTA DE PRODUTOS ===")
        for p in produtos:
            print(
                f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} "
                f"| Qtd: {p['quantidade']} | Categoria: {p['categoria']}"
            )

    except Exception:
        print("Erro ao listar produtos.")


def atualizar_produto(produtos):
    """Atualiza as informações de um produto existente."""

    try:
        codigo = int(input("Código do produto para atualizar: "))
    except Exception:
        print(" Código inválido.")
        return produtos

    produto = next((p for p in produtos if p["codigo"] == codigo), None)

    if not produto:
        print(" Produto não encontrado.")
        return produtos

    print(f"Produto atual: {produto}")

    novo_nome = input("Novo nome (Enter para manter): ").strip()
    if novo_nome:
        produto["nome"] = novo_nome

    novo_preco = input("Novo preço (Enter para manter): ").strip()
    if novo_preco:
        try:
            produto["preco"] = float(novo_preco)
        except Exception:
            print("Preço inválido — mantendo original.")

    nova_qtd = input("Nova quantidade (Enter para manter): ").strip()
    if nova_qtd:
        try:
            produto["quantidade"] = int(nova_qtd)
        except Exception:
            print("Quantidade inválida — mantendo original.")

    print("✅ Produto atualizado com sucesso!")
    return produtos


def excluir_produto(produtos, codigo_cad):
    """Exclui um produto existente."""

    try:
        codigo = int(input("Código do produto para excluir: "))
    except Exception:
        print(" Código inválido.")
        return produtos

    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            codigo_cad.discard(codigo)
            print(" Produto excluído com sucesso!")
            return produtos

    print(" Produto não encontrado.")
    return produtos
