import uuid
from datetime import datetime
from database.client import DBClient
from crud.vendedor.lerVendedor import listar_todos_vendedores
from bson.objectid import ObjectId

def selecionar_vendedor_por_numero():
    """Lista todos os vendedores e permite a seleção por número."""
    vendedores = listar_todos_vendedores()
    if not vendedores:
        print("\nNenhum vendedor cadastrado.")
        return None

    print("\n--- Selecione um Vendedor ---")
    mapa_vendedores = {}
    for i, vendedor in enumerate(vendedores, 1):
        mapa_vendedores[str(i)] = vendedor['_id']
        print(f"{i}. Nome: {vendedor['nome']}")

    escolha = input("Digite o número do vendedor (ou '0' para cancelar): ")
    if escolha == '0':
        return None

    vendedor_id = mapa_vendedores.get(escolha)
    if not vendedor_id:
        print("Opção inválida.")
        return None

    return vendedor_id

def criar_produto():
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    if colecao_produtos is None:
        print("Erro: Coleção 'produtos' não encontrada.")
        return None
    
    vendedor_id = selecionar_vendedor_por_numero()
    if not vendedor_id:
        print("Criação de produto cancelada.")
        return None

    print("\n--- Cadastro de Novo Produto ---")
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido. Criação de produto cancelada.")
        return None

    dados_produto = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "vendedorId": vendedor_id,
        "createAt": datetime.now().isoformat()
    }

    try:
        resultado = colecao_produtos.insert_one(dados_produto)
        print(f"\nProduto criado com sucesso! ID:{str(resultado.inserted_id)}")
        return str(resultado.inserted_id)
    except Exception as e:
        print(f"\nErro ao criar produto: {e}")
        return None