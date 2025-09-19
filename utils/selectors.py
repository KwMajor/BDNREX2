from crud.cliente.mostrarCliente import listarTodosClientes
from crud.produto.lerProduto import listar_todos_produtos, ler_produto
from crud.vendedor.lerVendedor import listar_todos_vendedores
from crud.compra.lerCompra import listar_todas_compras

def selecionar_cliente_por_numero():
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

    escolha = input("Digite o número do produto (ou '0' para cancelar): ")
    if escolha == '0':
        return None

    produto_selecionado = mapa_produtos.get(escolha)
    if not produto_selecionado:
        print("Opção inválida.")
        return None

    return produto_selecionado

def selecionar_vendedor_por_numero():
    vendedores = listar_todos_vendedores()
    if not vendedores:
        print("\nNenhum vendedor cadastrado.")
        return None

    print("\n--- Selecione um Vendedor ---")
    mapa_vendedores = {}
    for i, vendedor in enumerate(vendedores, 1):
        mapa_vendedores[str(i)] = str(vendedor['_id'])
        print(f"{i}. Nome: {vendedor['nome']}, ID: {vendedor['_id']}")

    escolha = input("Digite o número do vendedor (ou '0' para cancelar): ")
    if escolha == '0':
        return None

    vendedor_id = mapa_vendedores.get(escolha)
    if not vendedor_id:
        print("Opção inválida.")
        return None

    return vendedor_id

def selecionar_compra_por_numero():
    compras = listar_todas_compras()
    if not compras:
        print("\nNenhuma compra registrada.")
        return None
    
    print("\n--- Selecione a Compra ---")
    mapa_compras = {}
    for i, compra in enumerate(compras, 1):
        mapa_compras[str(i)] = str(compra['_id'])
        print(f"{i}. Compra de {compra.get('clienteNome', 'N/A')} - Total: R${compra.get('total', 0):.2f}")
        
    escolha = input("Digite o número da compra (ou '0' para cancelar): ")
    if escolha == '0':
        return None
        
    compra_id = mapa_compras.get(escolha)
    if not compra_id:
        print("Opção inválida.")
        return None
    
    return compra_id