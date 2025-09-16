from bson.objectid import ObjectId
from database.client import DBClient

def atualizar_produto(produto_id, novos_dados):
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    try:
        resultado = colecao_produtos.update_one(
            {"_id": ObjectId(produto_id)},
            {"$set": novos_dados}
        )
        return resultado.modified_count
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
        return 0