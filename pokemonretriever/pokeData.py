class PokedexObject:
    def __init__(self, name, pokeId):
        self.name = name
        self.id = pokeId


class Pokemon(PokedexObject):
    def __init__(self, name, pokeId, height, weight,
                 stats, types, abilities, moves):
        super().__init__(name, pokeId)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves


class Ability(PokedexObject):
    def __init__(self, name, pokeId, generation,
                 effect, shortEffect, pokemon):
        super().__init__(name, pokeId)
        self.generation = generation
        self.effect = effect
        self.shortEffect = shortEffect
        self.pokemon = pokemon


class Stat(PokedexObject):
    def __init__(self, name, pokeId, battleOnly):
        super().__init__(name, pokeId)
        self.battleOnly = battleOnly


class Moves(PokedexObject):
    def __init__(self, name, pokeId, generation,
                 accuracy, pp, power, types,
                 damageClass, effect):
        super().__init__(name, pokeId)
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.types = types
        self.damageClass = damageClass
        self.effect = effect
