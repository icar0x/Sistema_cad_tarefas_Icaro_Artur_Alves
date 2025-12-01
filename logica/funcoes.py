import json
import os


def carregar_tarefas(caminho="../dados/tarefas.json"):
    """Carrega tarefas do JSON."""
    try:
        if not os.path.exists(caminho):
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        print("Erro ao carregar o arquivo de tarefas.")
        return []


def salvar_tarefas(tarefas, caminho="../dados/tarefas.json"):
    """Salva tarefas no JSON."""
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=4)
    except Exception:
        print("Erro ao salvar as tarefas.")


def criar_tarefa(tarefas, titulo, descricao):
    """Cria uma nova tarefa """
    try:
        if not titulo.strip():
            print("Título não pode estar vazio!")
            return tarefas

        nova = {
            "id": len(tarefas) + 1,
            "titulo": titulo,
            "descricao": descricao if descricao.strip() else "Sem descrição",
            "status": "pendente"
        }

        tarefas.append(nova)
        return tarefas

    except Exception:
        print("Erro ao criar a tarefa.")
        return tarefas


def listar_tarefas(tarefas):
    """Lista todas as tarefas."""
    try:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for t in tarefas:
            print(f"ID: {t['id']} | {t['titulo']} | {t['status']}")
    except Exception:
        print("Erro ao listar tarefas.")


def atualizar_tarefa(tarefas, id_tarefa, novo_titulo, nova_descricao):
    """Atualiza título e descrição."""
    try:
        for t in tarefas:
            if t["id"] == id_tarefa:
                if novo_titulo.strip():
                    t["titulo"] = novo_titulo
                else:
                    print("Título não pode ser vazio!")
                    return False

                t["descricao"] = nova_descricao if nova_descricao.strip(
                ) else "Sem descrição"
                return True
        return False

    except Exception:
        print("Erro ao atualizar a tarefa.")
        return False


def excluir_tarefa(tarefas, id_tarefa):
    """Exclui uma tarefa pelo ID."""
    try:
        for t in tarefas:
            if t["id"] == id_tarefa:
                tarefas.remove(t)
                return True
        return False

    except Exception:
        print("Erro ao excluir a tarefa.")
        return False
