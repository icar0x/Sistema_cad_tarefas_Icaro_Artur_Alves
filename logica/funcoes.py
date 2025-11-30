import json
from pathlib import Path

# Caminho absoluto para o arquivo JSON (garante que funciona de qualquer cwd)
BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"
CAMINHO_ARQUIVO = DADOS_DIR / "tarefas.json"


def _garantir_estrutura():
    """Cria pasta 'dados' e arquivo JSON se não existirem."""
    DADOS_DIR.mkdir(parents=True, exist_ok=True)
    if not CAMINHO_ARQUIVO.exists():
        CAMINHO_ARQUIVO.write_text("[]", encoding="utf-8")


def carregar_tarefas():
    """Carrega e retorna a lista de tarefas do JSON (lista de dicionários)."""
    _garantir_estrutura()
    try:
        data = json.loads(CAMINHO_ARQUIVO.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
        else:
            # se o JSON não for lista, corrige
            return []
    except json.JSONDecodeError:
        # arquivo corrompido -> reescreve como lista vazia e retorna []
        CAMINHO_ARQUIVO.write_text("[]", encoding="utf-8")
        return []


def salvar_tarefas(tarefas):
    # Salva a lista de tarefas no JSON
    _garantir_estrutura()
    CAMINHO_ARQUIVO.write_text(json.dumps(
        tarefas, indent=4, ensure_ascii=False), encoding="utf-8")


# funções
def cadastrar_tarefa(tarefas):
    # Cria uma nova tarefa
    print("\n--- Cadastrar Tarefa ---")
    descricao = input("Descrição: ").strip()
    if descricao == "":
        print("Descrição não pode ser vazia.")
        return

    status = input("Status (Pendente / Concluída): ").strip()
    prazo = input("Prazo (AAAA-MM-DD): ").strip()

    # gera ID: 1 + maior id atual (ou 1 se lista vazia)
    novo_id = 1
    if tarefas:
        try:
            max_id = max(t.get("id", 0) for t in tarefas)
            novo_id = max_id + 1
        except Exception:
            novo_id = len(tarefas) + 1

    nova = {
        "id": novo_id,
        "descricao": descricao,
        "status": status,
        "prazo": prazo
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✔ Tarefa cadastrada com sucesso.")


def listar_tarefas(tarefas):

    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for t in tarefas:
        print(f"\nID: {t.get('id')}")
        print(f"Descrição: {t.get('descricao')}")
        print(f"Status: {t.get('status')}")
        print(f"Prazo: {t.get('prazo')}")
    print()


def atualizar_tarefa(tarefas):
    # Atualiza uma tarefa escolhida pelo ID.
    print("\n--- Atualizar Tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa para atualizar.")
        return

    listar_tarefas(tarefas)
    try:
        tarefa_id = int(
            input("Digite o ID da tarefa que deseja atualizar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    # encontrar por id
    for t in tarefas:
        if t.get("id") == tarefa_id:
            print("Deixe em branco para manter o valor atual.")
            nova_desc = input(
                f"Nova descrição [{t.get('descricao')}]: ").strip()
            novo_status = input(f"Novo status [{t.get('status')}]: ").strip()
            novo_prazo = input(f"Novo prazo [{t.get('prazo')}]: ").strip()

            if nova_desc != "":
                t["descricao"] = nova_desc
            if novo_status != "":
                t["status"] = novo_status
            if novo_prazo != "":
                t["prazo"] = novo_prazo

            salvar_tarefas(tarefas)
            print("✔ Tarefa atualizada.")
            return

    print("Tarefa não encontrada.")


def remover_tarefa(tarefas):
    # Remove tarefa por ID
    print("\n--- Remover Tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return

    listar_tarefas(tarefas)
    try:
        tarefa_id = int(
            input("Digite o ID da tarefa que deseja remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    # verifica existência
    existe = any(t.get("id") == tarefa_id for t in tarefas)
    if not existe:
        print("Tarefa não encontrada.")
        return

    confirma = input("Confirma remoção? (s/N): ").strip().lower()
    if confirma != "s":
        print("Remoção cancelada.")
        return

    nova_lista = [t for t in tarefas if t.get("id") != tarefa_id]
    # reatribui ids numéricos a partir de 1
    for i, t in enumerate(nova_lista, start=1):
        t["id"] = i

    # substitui conteúdo da lista original
    tarefas.clear()
    tarefas.extend(nova_lista)

    salvar_tarefas(tarefas)
    print(" Tarefa removida.")


def gerar_relatorio(tarefas):
    # Imprime relatório simples
    total = len(tarefas)
    pendentes = sum(1 for t in tarefas if str(
        t.get("status", "")).lower() == "pendente")
    concluidas = sum(1 for t in tarefas if str(t.get("status", "")).lower() in (
        "concluída", "concluida", "feito", "concluído"))

    print("\n--- Relatório ---")
    print(f"Total de tarefas: {total}")
    print(f"Tarefas pendentes: {pendentes}")
    print(f"Tarefas concluídas: {concluidas}")
