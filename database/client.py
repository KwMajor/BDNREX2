import os
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class DBClient:
    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBClient, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        try:
            mongo_uri = os.getenv("MONGO_URI")
            db_name = os.getenv("DB_NAME")
            
            if not mongo_uri or not db_name:
                raise ValueError("MONGO_URI ou DB_NAME não configurados.")
            
            self._client = MongoClient(mongo_uri)
            self._client.admin.command('ping')
            self._db = self._client.get_database(db_name)
            print("Conexão com o MongoDB estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            self._client = None
            self._db = None
    
    def get_collection(self, collection_name):
        if self._db is not None:
            return self._db[collection_name]
        return None