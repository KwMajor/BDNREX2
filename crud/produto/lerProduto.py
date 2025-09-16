from bson.objectid import ObjectId
from database.client import DBClient

def ler_produto(produto_id):
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    try:
        return colecao_produtos.find_one({"_id": ObjectId(produto_id)})
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return None

def listar_todos_produtos():
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    try:
        pipeline = [
            {
                "$lookup": {
                    "from": "vendedores",
                    "let": { "vendedorIdStr": "$vendedorId" },
                    "pipeline": [
                        { "$match": {
                            "$expr": { "$eq": [ "$_id", { "$toObjectId": "$$vendedorIdStr" } ] }
                        }}
                    ],
                    "as": "vendedor_info"
                }
            },
            {
                "$unwind": {
                    "path": "$vendedor_info",
                    "preserveNullAndEmptyArrays": True
                }
            }
        ]
        
        return list(colecao_produtos.aggregate(pipeline))
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return []

def buscar_produtos_por_vendedor(vendedor_id):
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    try:
        return list(colecao_produtos.find({"vendedorId": vendedor_id}))
    except Exception as e:
        print(f"Erro ao buscar produtos do vendedor: {e}")
        return []