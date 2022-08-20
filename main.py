from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()

pokemons = pokedex.getPokemonByPokedexNumber(5)
print(pokemons)

