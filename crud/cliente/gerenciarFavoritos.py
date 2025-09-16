from bson.objectid import ObjectId
from database.client import DBClient

def adicionarFavorito(cliente_id, produto_id):
    db_client = DBClient()
    colecao_clientes = db_client.get_collection("clientes")

    try:
        resultado = colecao_clientes.update_one(
            {"_id": ObjectId(cliente_id)},
            {"$addToSet": {"favoritos": produto_id}}
        )
        return resultado.modified_count
    except Exception as e:
        print(f"Erro ao adicionar favorito: {e}")
        return 0

def removerFavorito(cliente_id, produto_id):
    db_client = DBClient()
    colecao_clientes = db_client.get_collection("clientes")

    try:
        resultado = colecao_clientes.update_one(
            {"_id": ObjectId(cliente_id)},
            {"$pull": {"favoritos": produto_id}}
        )
        return resultado.modified_count
    except Exception as e:
        print(f"Erro ao remover favorito: {e}")
        return 0