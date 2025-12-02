🛒 Sistema de Gerenciamento de Produtos (CRUD)

Este é um sistema simples de CRUD de produtos feito em Python, utilizando armazenamento em JSON e totalmente baseado no terminal.
O objetivo é permitir o cadastro, listagem, atualização e exclusão de produtos de maneira prática e organizada.


⚙️ Funcionalidades
📝 1 - Cadastrar Produto

Permite registrar um novo produto informando:

Código (único)

Nome

Preço

Quantidade em estoque

Categoria (selecionada de uma lista pré-definida)

🔒 O sistema impede cadastro de códigos duplicados.

🛑 Também evita campos vazios e valores inválidos usando try/except.

📋 2 - Listar Produtos

Exibe todos os produtos cadastrados mostrando:

Código | Nome | Preço | Quantidade | Categoria


Caso a lista esteja vazia:

Nenhum produto cadastrado.

✏️ 3 - Atualizar Produto

Permite alterar:

Nome

Preço

Quantidade

⚠️ Basta pressionar Enter para manter o valor atual.

O sistema impede erros de digitação com tratamento de exceções.

🗑️ 4 - Excluir Produto

Remove um produto pelo código.

Se o código não existir:

Produto não encontrado.

🚪 0 - Sair

Finaliza o programa exibindo:

Saindo...

🧠 Estrutura Interna
Estrutura	Função
produtos.json	Armazena todos os produtos cadastrados
produtos (list)	Lista principal de produtos
codigo_cad (set)	Garante códigos únicos
categorias (tuple)	Opções fixas de categoria
🧱 Funções Principais (funcoes.py)

carregar_produtos() → Lê o JSON

salvar_produtos() → Salva no JSON

cadastrar_produto() → Adiciona novo produto

listar_produtos() → Mostra todos

atualizar_produto() → Edita informações

excluir_produto() → Remove produto
