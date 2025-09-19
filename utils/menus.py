from utils.selectors import (
    selecionar_cliente_por_numero,
    selecionar_produto_por_numero,
    selecionar_vendedor_por_numero,
    selecionar_compra_por_numero
)

from crud.cliente.novoCliente import criar_cliente
from crud.cliente.mostrarCliente import mostraCliente, listarTodosClientes
from crud.cliente.atualizarCliente import atualizarCliente
from crud.cliente.deletarCliente import deletaCliente
from crud.cliente.gerenciarFavoritos import adicionarFavorito, removerFavorito

from crud.vendedor.criarVendedor import criar_vendedor
from crud.vendedor.lerVendedor import ler_vendedor, listar_todos_vendedores
from crud.vendedor.atualizarVendedor import atualizar_vendedor
from crud.vendedor.deletarVendedor import deletar_vendedor

from crud.produto.criarProduto import criar_produto
from crud.produto.lerProduto import ler_produto, listar_todos_produtos, buscar_produtos_por_vendedor
from crud.produto.atualizarProduto import atualizar_produto
from crud.produto.deletarProduto import deletar_produto

from crud.compra.novaCompra import criar_compra
from crud.compra.lerCompra import ler_compra, listar_compras_cliente, listar_todas_compras

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Produtos")
        print("4. Gerenciar Compras")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            menu_clientes()
        elif escolha == '2':
            menu_vendedores()
        elif escolha == '3':
            menu_produtos()
        elif escolha == '4':
            menu_compras()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")

def menu_clientes():
    while True:
        print("\n--- Menu de Clientes ---")
        print("1. Cadastrar novo Cliente")
        print("2. Ler dados de um Cliente")
        print("3. Atualizar um Cliente")
        print("4. Deletar um Cliente")
        print("5. Gerenciar Produtos Favoritos")
        print("6. Listar todos os Clientes")
        print("7. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            criar_cliente()
        elif escolha == '2':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                cliente = mostraCliente(cliente_id)
                if cliente:
                    print("\n--- Dados Completos do Cliente ---")
                    for chave, valor in cliente.items():
                        if chave == 'favoritos' and valor:
                            print("\n--- Produtos Favoritos ---")
                            for produto_id in valor:
                                produto = ler_produto(produto_id)
                                if produto:
                                    print(f"  - {produto['nome']} (ID: {produto['_id']})")
                                else:
                                    print(f"  - Produto com ID '{produto_id}' não encontrado.")
                        elif chave == 'favoritos':
                            print("\n--- Produtos Favoritos ---")
                            print("Nenhum produto favorito cadastrado.")
                        else:
                            print(f"{chave.capitalize()}: {valor}")
                else:
                    print("Cliente não encontrado.")
        elif escolha == '3':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                novos_dados = {"email": input("Novo e-mail: ")}
                modificados = atualizarCliente(cliente_id, novos_dados)
                if modificados > 0:
                    print("Cliente atualizado com sucesso.")
                else:
                    print("Falha ao atualizar cliente.")
        elif escolha == '4':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                deletados = deletaCliente(cliente_id)
                if deletados > 0:
                    print("Cliente deletado com sucesso.")
                else:
                    print("Falha ao deletar cliente.")
        elif escolha == '5':
            menu_favoritos()
        elif escolha == '6':
            clientes = listarTodosClientes()
            print("--- Lista de Clientes ---")
            for cliente in clientes:
                print(f"ID: {cliente['_id']}, Nome: {cliente['nome']}")
        elif escolha == '7':
            break
        else:
            print("Opção inválida.")

def menu_favoritos():
    while True:
        print("\n--- Gerenciar Favoritos ---")
        print("1. Adicionar Produto Favorito")
        print("2. Remover Produto Favorito")
        print("3. Voltar ao Menu de Clientes")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                produto = selecionar_produto_por_numero()
                if produto:
                    produto_id = str(produto['_id'])
                    if adicionarFavorito(cliente_id, produto_id) > 0:
                        print("Produto adicionado aos favoritos com sucesso.")
                    else:
                        print("Falha ao adicionar favorito.")
        elif escolha == '2':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                produto = selecionar_produto_por_numero()
                if produto:
                    produto_id = str(produto['_id'])
                    if removerFavorito(cliente_id, produto_id) > 0:
                        print("Produto removido dos favoritos com sucesso.")
                    else:
                        print("Falha ao remover favorito.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")

def menu_vendedores():
    while True:
        print("\n--- Menu de Vendedores ---")
        print("1. Cadastrar novo Vendedor")
        print("2. Ler dados de um Vendedor")
        print("3. Atualizar um Vendedor")
        print("4. Deletar um Vendedor")
        print("5. Listar todos os Vendedores")
        print("6. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_vendedor()
        elif escolha == '2':
            vendedor_id = selecionar_vendedor_por_numero()
            if vendedor_id:
                vendedor = ler_vendedor(vendedor_id)
                if vendedor:
                    print("Dados do Vendedor:", vendedor)
                else:
                    print("Vendedor não encontrado.")
        elif escolha == '3':
            vendedor_id = selecionar_vendedor_por_numero()
            if vendedor_id:
                novos_dados = {"email": input("Novo e-mail: ")}
                modificados = atualizar_vendedor(vendedor_id, novos_dados)
                if modificados > 0:
                    print("Vendedor atualizado com sucesso.")
                else:
                    print("Falha ao atualizar vendedor.")
        elif escolha == '4':
            vendedor_id = selecionar_vendedor_por_numero()
            if vendedor_id:
                deletados = deletar_vendedor(vendedor_id)
                if deletados > 0:
                    print("Vendedor deletado com sucesso.")
                else:
                    print("Falha ao deletar vendedor.")
        elif escolha == '5':
            vendedores = listar_todos_vendedores()
            print("--- Lista de Vendedores ---")
            for vendedor in vendedores:
                print(f"ID: {vendedor['_id']}, Nome: {vendedor['nome']}")
        elif escolha == '6':
            break
        else:
            print("Opção inválida.")

def menu_produtos():
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Cadastrar novo Produto")
        print("2. Ler dados de um Produto")
        print("3. Atualizar um Produto")
        print("4. Deletar um Produto")
        print("5. Listar todos os Produtos")
        print("6. Buscar produtos de um Vendedor")
        print("7. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_produto()
        elif escolha == '2':
            produto_selecionado = selecionar_produto_por_numero()
            if produto_selecionado:
                print("\n--- Dados Detalhados do Produto ---")
                vendedor_nome = produto_selecionado.get('vendedor_info', {}).get('nome', 'Vendedor não encontrado')
                print(f"ID do Produto: {produto_selecionado['_id']}")
                print(f"Nome: {produto_selecionado['nome']}")
                print(f"Descrição: {produto_selecionado['descricao']}")
                print(f"Preço: R${produto_selecionado['preco']:.2f}")
                print(f"Vendedor: {vendedor_nome}")
            else:
                print("Produto não encontrado ou operação cancelada.")
        elif escolha == '3':
            produto_selecionado = selecionar_produto_por_numero()
            if produto_selecionado:
                produto_id = produto_selecionado['_id']
                novos_dados = {"preco": float(input("Novo preço: "))}
                modificados = atualizar_produto(produto_id, novos_dados)
                if modificados > 0:
                    print("Produto atualizado com sucesso.")
                else:
                    print("Falha ao atualizar produto.")
        elif escolha == '4':
            produto_selecionado = selecionar_produto_por_numero()
            if produto_selecionado:
                produto_id = produto_selecionado['_id']
                deletados = deletar_produto(produto_id)
                if deletados > 0:
                    print("Produto deletado com sucesso.")
                else:
                    print("Falha ao deletar produto.")
        elif escolha == '5':
            produtos = listar_todos_produtos()
            print("--- Lista de Produtos ---")
            for produto in produtos:
                vendedor_nome = produto.get('vendedor_info', {}).get('nome', 'Vendedor não encontrado')
                print(f"ID: {produto['_id']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Vendedor: {vendedor_nome}")
        elif escolha == '6':
            vendedor_id = selecionar_vendedor_por_numero()
            if vendedor_id:
                produtos_vendedor = buscar_produtos_por_vendedor(vendedor_id)
                if produtos_vendedor:
                    print(f"--- Produtos do Vendedor {vendedor_id} ---")
                    for produto in produtos_vendedor:
                        print(f"ID: {produto['_id']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
                else:
                    print("Nenhum produto encontrado para este vendedor.")
        elif escolha == '7':
            break
        else:
            print("Opção inválida.")

def menu_compras():
    while True:
        print("\n--- Menu de Compras ---")
        print("1. Registrar nova Compra")
        print("2. Ler dados de uma Compra")
        print("3. Listar compras de um Cliente")
        print("4. Listar todas as Compras")
        print("5. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_compra()
        elif escolha == '2':
            compra_id = selecionar_compra_por_numero()
            if compra_id:
                compra = ler_compra(compra_id)
                if compra:
                    print("\n--- Dados da Compra ---")
                    print(f"ID da Compra: {compra['_id']}")
                    print(f"Cliente ID: {compra['clienteId']}")
                    print(f"Data da Compra: {compra['dataCompra']}")
                    print(f"Total da Compra: R${compra['total']:.2f}")
                    print("\n--- Itens da Compra ---")
                    for item in compra['produtos']:
                        print(f"  - Produto: {item['nomeProduto']}")
                        print(f"    Quantidade: {item['quantidade']}")
                        print(f"    Preço Unitário: R${item['precoUnitario']:.2f}")
                else:
                    print("Compra não encontrada.")
            else:
                print("Operação cancelada.")
        elif escolha == '3':
            cliente_id = selecionar_cliente_por_numero()
            if cliente_id:
                compras = listar_compras_cliente(cliente_id)
                if compras:
                    print(f"--- Compras do Cliente ---")
                    for compra in compras:
                        print(f"ID da Compra: {compra['_id']}, Total: R${compra['total']:.2f}, Data: {compra['dataCompra']}")
                        for item in compra['produtos']:
                            print(f"  - Produto: {item['nomeProduto']} ({item['quantidade']} unidades)")
                else:
                    print("Nenhuma compra encontrada para este cliente.")
            else:
                print("Operação cancelada.")
        elif escolha == '4':
            compras = listar_todas_compras()
            print("--- Todas as Compras ---")
            if compras:
                for compra in compras:
                    print(f"\nID da Compra: {compra.get('_id', 'N/A')}")
                    print(f"Comprador: {compra.get('clienteNome', 'N/A')}")
                    print(f"Total: R${compra.get('total', 0):.2f}")
                    print(f"Data: {compra.get('dataCompra', 'N/A')}")
                    print("  - Produtos:")
                    for item in compra.get('produtos', []):
                        print(f"    - {item.get('nomeProduto', 'N/A')} ({item.get('quantidade', 'N/A')} unid. a R${item.get('precoUnitario', 0):.2f})")
            else:
                print("Nenhuma compra encontrada.")
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")