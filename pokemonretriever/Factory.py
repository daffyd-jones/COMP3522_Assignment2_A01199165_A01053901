from facade import Mode
from pokemonretriever.pokeData import Pokemon, Ability, Moves


class Factory:
    def __init__(self, mode):
        self.mode = mode

    def make(self, **kwargs):
        if self.mode == Mode.POKEMON:
            return Pokemon(**kwargs)
        elif self.mode == Mode.ABILITY:
            return Ability(**kwargs)
        elif self.mode == Mode.MOVE:
            return Moves(**kwargs)

    def filter_json(self, json):
        if self.mode == Mode.POKEMON:
            pass
        if self.mode == Mode.ABILITY:
            pass
        if self.mode == Mode.MOVE:
            pass
