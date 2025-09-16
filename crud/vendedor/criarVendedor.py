import uuid
from datetime import datetime
from database.client import DBClient

def criar_vendedor():
    db_client = DBClient()
    colecao_vendedores = db_client.get_collection("vendedores")
    if colecao_vendedores is None:
        print("Erro: coleção 'vendedores' não encontrada.")
        return None
    
    print("\n-- Cadastro de novo vendedor --")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    nomeLoja = input("Nome da loja: ")
    cnpj = input("CNPJ: ")
    dataNasc = input("Data de Nascimento (DD/MM/AAAA): ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

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
            confirmarPrincipal = input("Este é o seu endereço principal? (s/n): ").lower()
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

    dadosVendedor = {
        "nome": nome,
        "cpf": cpf,
        "nomeLoja": nomeLoja,
        "cnpj": cnpj,
        "dataNasc": dataNasc,
        "telefone": telefone,
        "email": email
    }

    try:
        resultado = colecao_vendedores.insert_one(dadosVendedor)
        print(f"\nVendedor criado com sucesso! ID: {str(resultado.inserted_id)}")
        return str(resultado.inserted_id)
    except Exception as e:
        print(f"\nErro ao criar vendedor: {e}")
        return None