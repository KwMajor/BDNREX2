from bson.objectid import ObjectId
from database.client import DBClient

def deletaCliente(clienteId):
    db_client = DBClient()
    colecaoClientes = db_client.get_collection("clientes")

    try:
        resultado = colecaoClientes.delete_one({"_id": ObjectId(clienteId)})
        return resultado.deleted_count
    except Exception as e:
        print(f"Erro ao deletar cliente: {e}")
        return 0