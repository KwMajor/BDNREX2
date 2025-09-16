from bson.objectid import ObjectId
from database.client import DBClient

def atualizarCliente(clienteId, novosDados):
    db_cliente = DBClient()
    colecaoClientes = db_cliente.get_collection("clientes")

    try:
        resultado = colecaoClientes.update_one(
            {"_id": ObjectId(clienteId)},
            {"$set": novosDados}
        )
        return resultado.modified_count
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        return 0