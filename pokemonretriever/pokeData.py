from abc import ABC


class PokedexObject(ABC):
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
    def __init__(self, name, pokeId=None, generation=None,
                 effect=None, shortEffect=None, pokemon=None):
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
    def __init__(self, name, base_stat, url=None, name_expanded=None, pokeId=None, isBattleOnly=None, isExpanded=False):
        super().__init__(name, pokeId)
        self.base_stat = base_stat
        self.url = url
        self.name_expanded = name_expanded
        self.isBattleOnly = isBattleOnly
        self.isExpanded = isExpanded

    def __str__(self):
        print(f"Name:         -- {self.name}"
              f"ID:           -- {self.id}"
              f"Battle Only:  -- {self.isBattleOnly}")


class Moves(PokedexObject):
    def __init__(self, name, level_acquired, poke_id=None, generation=None,
                 accuracy=None, pp=None, power=None, types=None,
                 damage_class=None, effect=None):
        super().__init__(name, poke_id)
        self.level_acquired = level_acquired
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.types = types
        self.damageClass = damage_class
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