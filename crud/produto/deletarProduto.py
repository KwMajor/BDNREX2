from bson.objectid import ObjectId
from database.client import DBClient

def deletar_produto(produto_id):
    db_client = DBClient()
    colecao_produtos = db_client.get_collection("produtos")
    try:
        resultado = colecao_produtos.delete_one({"_id": ObjectId(produto_id)})
        return resultado.deleted_count
    except Exception as e:
        print(f"Erro ao deletar produto {e}")
        return 0