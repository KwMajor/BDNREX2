from bson.objectid import ObjectId
from database.client import DBClient

def mostraCliente(cliente_id):
    db_client = DBClient()
    colecaoClientes = db_client.get_collection("clientes")

    try:
        return colecaoClientes.find_one({"_id": ObjectId(cliente_id)})
    except Exception as e:
        print(f"Erro ao buscar cliente: {e}")
        return None

def listarTodosClientes():
    db_client = DBClient()
    colecaoClientes = db_client.get_collection("clientes")

    try:
        return list(colecaoClientes.find({}))
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
        return []