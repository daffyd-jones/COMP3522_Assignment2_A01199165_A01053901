from pokemonretriever.pokeData import Pokemon, Ability, Moves, Stat
from abc import ABC, abstractmethod


class Factory(ABC):

    @classmethod
    @abstractmethod
    def create_pokedex_entry(cls, d: dict, expanded: bool):
        pass


class pokemonFactory(Factory):

    @classmethod
    def create_pokedex_entry(cls, d: dict, expanded: bool):
        return Pokemon(d.get('name'), d.get('id'), d.get('height'), d.get('weight'), )