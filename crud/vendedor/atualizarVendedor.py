from bson.objectid import ObjectId
from database.client import DBClient

def atualizar_vendedor(vendedor_id, novos_dados):
    db_client = DBClient()
    colecao_vendedores = db_client.get_collection("vendedores")
    try:
        resultado = colecao_vendedores.update_one(
            {"_id": ObjectId(vendedor_id)},
            {"$set": novos_dados}
        )
        return resultado.modified_count
    except Exception as e:
        print(f"Erro ao atualizar vendedor: {e}")
        return 0