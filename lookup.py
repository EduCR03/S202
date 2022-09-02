from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.carro_dataset import dataset as carro_dataset
from dataset.produto_database import dataset as produto_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

carros = Database(
    database="database",
    collection="carros",
    dataset=carro_dataset
)
carros.resetDatabase()

compras = Database(
    database="database",
    collection="produto",
    dataset=produto_dataset
)
compras.resetDatabase()

result1 = carros.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "dono_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }
    }
])

result2 = compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "comprador"
        }
    },

    {"$group":
        {
            "_id": "$cliente_id",
            "total":{"$sum": "$total"}
        }
    },

    {"$sort":
        {"total": -1}
    },

    {"$unwind": '$_id'},

    {"$project":
        {
            "nome": "$_id.nome",
            "total": "$total",
            "_id": 0,
            "desconto":
                {
                     "$cond":
                        {
                            "if":
                                {"$gte": ["total", 10]}, "then": True, "else": False
                        }
                }
        }
    }
])

writeAJson(result2, "result2")
