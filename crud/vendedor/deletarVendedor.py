from bson.objectid import ObjectId
from database.client import DBClient

def deletar_vendedor(vendedor_id):
    db_client = DBClient()
    colecao_vendedores = db_client.get_collection("vendedores")
    try:
        resultado = colecao_vendedores.delete_one({"_id": ObjectId(vendedor_id)})
        return resultado.deleted_count
    except Exception as e:
        print(f"Erro ao deletar vendedor: {e}")
        return 0