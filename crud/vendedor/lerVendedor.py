from bson.objectid import ObjectId
from database.client import DBClient

def ler_vendedor(vendedor_id):
    db_client = DBClient()
    colecao_vendedores = db_client.get_collection("vendedores")
    try:
        return colecao_vendedores.find_one({"_id": ObjectId(vendedor_id)})
    except Exception as e:
        print(f"Erro ao buscar vendedor: {e}")
        return None
    
def listar_todos_vendedores():
    db_client = DBClient()
    colecao_vendedores = db_client.get_collection("vendedores")
    try:
        return list(colecao_vendedores.find({}))
    except Exception as e:
        print(f"Erro ao listar vendedores: {e}")
        return []