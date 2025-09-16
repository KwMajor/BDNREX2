from datetime import datetime
from database.client import DBClient
from crud.cliente.mostrarCliente import listarTodosClientes
from crud.produto.lerProduto import listar_todos_produtos
from bson.objectid import ObjectId
from crud.cliente.mostrarCliente import listarTodosClientes
from crud.produto.lerProduto import listar_todos_produtos
from bson.objectid import ObjectId

def selecionar_cliente_por_numero():
    """Lista todos os clientes e permite a seleção por número."""
    clientes = listarTodosClientes()
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return None

    print("\n--- Selecione o Cliente ---")
    mapa_clientes = {}
    for i, cliente in enumerate(clientes, 1):
        mapa_clientes[str(i)] = cliente['_id']
        print(f"{i}. Nome: {cliente['nome']}")

    escolha = input("Digite o número do cliente (ou '0' para cancelar): ")
    if escolha == '0':
        return None

    cliente_id = mapa_clientes.get(escolha)
    if not cliente_id:
        print("Opção inválida.")
        return None

    return cliente_id

def selecionar_produto_por_numero():
    """Lista todos os produtos e permite a seleção por número."""
    produtos = listar_todos_produtos()
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return None

    print("\n--- Selecione um Produto ---")
    mapa_produtos = {}
    for i, produto in enumerate(produtos, 1):
        mapa_produtos[str(i)] = produto
        vendedor_nome = produto.get('vendedor_info', {}).get('nome', 'Vendedor não encontrado')
        print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Vendedor: {vendedor_nome}")

    escolha = input("Digite o número do produto (ou '0' para finalizar a compra): ")
    if escolha == '0':
        return 'sair'

    produto_selecionado = mapa_produtos.get(escolha)
    if not produto_selecionado:
        print("Opção inválida.")
        return None

    return produto_selecionado


def criar_compra():
    db_client = DBClient()
    colecao_compras = db_client.get_collection("compras")

    print("\n--- Registrar Nova Compra ---")
    
    cliente_id = selecionar_cliente_por_numero()
    if not cliente_id:
        print("Criação de compra cancelada.")
        return None

    produtos_comprados = []
    total_compra = 0

    while True:
        produto_info = selecionar_produto_por_numero()

        if produto_info == 'sair':
            break
        
        if not produto_info:
            continue

        try:
            quantidade = int(input(f"Quantidade de '{produto_info.get('nome')}': "))
            
            subtotal = produto_info.get("preco", 0) * quantidade
            total_compra += subtotal

            produtos_comprados.append({
                "produtoId": produto_info.get('_id'),
                "nomeProduto": produto_info.get("nome"),
                "precoUnitario": produto_info.get("preco"),
                "quantidade": quantidade,
                "vendedorId": produto_info.get('vendedorId')
            })
            
            print(f"Produto adicionado. Subtotal: R${subtotal:.2f}")

        except ValueError:
            print("Quantidade inválida. Por favor, digite um número.")
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")

    if not produtos_comprados:
        print("\nCompra cancelada. Nenhum produto adicionado.")
        return None

    dados_compra = {
        "clienteId": cliente_id,
        "produtos": produtos_comprados,
        "total": total_compra,
        "dataCompra": datetime.now().isoformat()
    }
    
    try:
        resultado = colecao_compras.insert_one(dados_compra)
        print(f"\nCompra registrada com sucesso! ID:{str(resultado.inserted_id)}")
        return str(resultado.inserted_id)
    except Exception as e:
        print(f"\nErro ao registrar compra: {e}")
        return None