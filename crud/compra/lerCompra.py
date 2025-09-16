from bson.objectid import ObjectId
from database.client import DBClient

def ler_compra(compra_id):
    db_client = DBClient()
    colecao_compras = db_client.get_collection("compras")
    try:
        return colecao_compras.find_one({"_id": ObjectId(compra_id)})
    except Exception as e:
        print(f"Erro ao buscar compra: {e}")
        return None

def listar_compras_cliente(cliente_id):
    db_client = DBClient()
    colecao_compras = db_client.get_collection("compras")
    try:
        return list(colecao_compras.find({"clienteId": cliente_id}))
    except Exception as e:
        print(f"Erro ao listar compras: {e}")
        return []

def listar_todas_compras():
    db_client = DBClient()
    colecao_compras = db_client.get_collection("compras")
    try:
        pipeline = [

            {
                "$lookup": {
                    "from": "clientes",
                    "localField": "clienteId",
                    "foreignField": "_id",
                    "as": "cliente_info"
                }
            },

            {
                "$unwind": "$cliente_info"
            },

            {
                "$unwind": "$produtos"
            },
            {
                "$lookup": {
                    "from": "produtos",
                    "localField": "produtos.produtoId",
                    "foreignField": "_id",
                    "as": "produto_info"
                }
            },
            {
                "$unwind": "$produto_info"
            },

            {
                "$group": {
                    "_id": "$_id",
                    "clienteNome": { "$first": "$cliente_info.nome" },
                    "total": { "$first": "$total" },
                    "dataCompra": { "$first": "$dataCompra" },
                    "produtos": {
                        "$push": {
                            "nomeProduto": "$produto_info.nome",
                            "quantidade": "$produtos.quantidade",
                            "precoUnitario": "$produtos.precoUnitario"
                        }
                    }
                }
            },

            {
                "$project": {
                    "_id": 1,
                    "clienteNome": 1,
                    "total": 1,
                    "dataCompra": 1,
                    "produtos": 1
                }
            }
        ]
        
        return list(colecao_compras.aggregate(pipeline))
    except Exception as e:
        print(f"Erro ao listar todas as compras: {e}")
        return []