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

    def __str__(self):
        print(f"Name:      -- {self.name} \n"
              f"Id:        -- {self.id}"
              f"Height:    -- {self.weight}"
              f"Stats:     -- {self.stats}"
              f"Types:     -- {self.types}"
              f"Abilities: -- {self.moves}")


class Ability(PokedexObject):
    def __init__(self, name, pokeId, generation,
                 effect, shortEffect, pokemon):
        super().__init__(name, pokeId)
        self.generation = generation
        self.effect = effect
        self.shortEffect = shortEffect
        self.pokemon = pokemon

    def __str__(self):
        print(f"Name:       -- {self.name}"
              f"ID:         -- {self.id}"
              f"Generation: -- {self.generation}"
              f"Effect:     -- {self.effect}"
              f"Sh-Effect:  -- {self.shortEffect}"
              f"Pokemon:    -- {self.pokemon}")


class Stat(PokedexObject):
    def __init__(self, name, pokeId, battleOnly):
        super().__init__(name, pokeId)
        self.battleOnly = battleOnly

    def __str__(self):
        print(f"Name:         -- {self.name}"
              f"ID:           -- {self.id}"
              f"Battle Only:  -- {self.battleOnly}")


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

    def __str__(self):
        print(f"Name:        -- {self.name}"
              f"ID:          -- {self.id}"
              f"Generations: -- {self.generation}"
              f"Accuracy:    -- {self.accuracy}"
              f"PP:          -- {self.pp}"
              f"Power:       -- {self.power}"
              f"Types:       -- {self.types}"
              f"Damage Class -- {self.damageClass}"
              f"Effect:      -- {self.effect}")