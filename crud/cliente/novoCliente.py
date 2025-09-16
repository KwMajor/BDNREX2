import uuid
import hashlib
from datetime import datetime
from database.client import DBClient

def criar_cliente():
    db_client = DBClient()
    colecao_clientes = db_client.get_collection("clientes")
    if colecao_clientes is None:
        print("Erro: Coleção 'clientes' não encontrada.")
        return None
    
    print("-- Cadastro de Novos Clientes --")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    dataNasc = input("Data de Nascimento(DD/MM/AAAA): ")
    email = input("E-mail: ")
    senha = hashlib.sha256(input("Digite a senha: ").encode()).hexdigest()

    enderecos = []
    principalDefinido = False

    while True:
        print("\n -- Cadastro de Endereço --")
        enderecoId = str(uuid.uuid4())
        estado = input("Estado: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        is_principal = False
        if not principalDefinido:
            confirmarPrincipal = input("Este é o endereço principal? (s/n): ").lower()
            if confirmarPrincipal == 's':
                is_principal = True
                principalDefinido = True

        enderecos.append({
            "enderecoId": enderecoId,
            "estado": estado,
            "cidade": cidade,
            "cep": cep,
            "principal": is_principal
        })

        enderecoSecundario = input("Deseja adicionar outro endereço? (s/n): ").lower()
        if enderecoSecundario == 'n':
            if not principalDefinido and len(enderecos) > 0:
                enderecos[0]["principal"] = True
            break
            
    print(f"endereços coletados {enderecos}")
    
    dadosCliente = {
        "nome": nome,
        "cpf": cpf,
        "dataNasc": dataNasc,
        "email": email,
        "senha": senha,
        "enderecos": enderecos,
        "favoritos": [],
        "createAt": datetime.now().isoformat()
    }

    try:
        resultado = colecao_clientes.insert_one(dadosCliente)
        print(f"\nCliente criado com sucesso! ID:{str(resultado.inserted_id)}")
        return str(resultado.inserted_id)
    except Exception as e:
        print(f"\nErro ao criar cliente: {e}")
        return None