from db.database import Database
from bson.objectid import ObjectId

class Pessoa:
    def __init__(self):
        self.db = Database(database="Biblioteca", collection="Livros")
        self.collection = self.db.collection

    def read_all(self):
        res = self.collection.fuind()
        return res

    def update_preco(self, id: int, preco: int):
        res = self.collection.update_one({"_id": id}, {"$set":{"preco": preco}})
        return res

    def create_livro(self, id: int, titulo: str, autor: str, ano: int, preco: int):
        res = self.collection.insert_one({"id": id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
        return res

    def delete_livro(self, id: int):
        res = self.collection.delete_one({"_id": id})
        return res.deleted_count

