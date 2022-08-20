from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions

    def getPokemonByWeaknessFire(self):
        typeFire = ["Fire"]
        fireWeak = self.collection.find({"weakness": {"$all" : typeFire}}, {"id" : 0,"next_evolution": 0, "prev_evolution": 0,
                                         "type": 0, "weaknesses": 1})
        result = []
        for pokemon in fireWeak:
            result.append(pokemon)
        return result

    def getPokemonGraterSpawnThan(self, spawn: list):
        spawn_chance = self.collection.find({"spawn_chance" :{"$gt": spawn}}, {"_id" : 0,"next_evolution": 0, "prev_evolution": 0,
                                         "type": 0, "weaknesses": 0, "spawn_chance": 1})
        pokemons = []
        for pokemon in spawn_chance:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonLessSpawnThan(self, spawn):
        response = self.collection.find({"spawn_chance" : {"$lt" : spawn}}, {"_id" : 0,"next_evolution": 0, "prev_evolution": 0,
                                     "type": 0, "weaknesses": 0, "weight": 1})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByPokedexNumber(self, number: int):
        pokedex = self.collection.find({"id": number}, {"name": 1})
        pokemons = {}
        for pokemon in pokedex:
            pokemons = pokemon
        return pokemons
    def getPokemonThatStartWithB(self):
        name = self.collection.find({"name": {"$regex": "/^B.*$/"}}, {"_id" : 0,"next_evolution": 0, "prev_evolution": 0,
                                         "type": 0, "weaknesses": 0, "name": 1})
        pokemons = []
        for pokemon in name:
            pokemons.append(pokemon)
        return pokemons

