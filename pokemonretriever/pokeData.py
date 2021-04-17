from abc import ABC


class PokedexObject(ABC):
    """
    PokedexObject abstract class
    """
    def __init__(self, name, pokeId):
        """
        PokedexObject init
        :param name: name of pokemon - string
        :param pokeId: pokemon id - string
        """
        self.name = name
        self.id = pokeId


class Pokemon(PokedexObject):
    """
    Pokemon class

    - extends PokedexObject
    """
    def __init__(self, name, pokeId, height, weight,
                 stats, types, abilities, moves):
        """
        Pokemon init
        :param name: pokemon name - string
        :param pokeId: pokemon id - string
        :param height: pokemon height - string
        :param weight: pokemon weight - string
        :param stats: pokemons stats - if expanded is Stats obj else list
        :param types: pokemon type - string
        :param abilities: pokemon abilities - if expanded is Abilities obj else list
        :param moves: pokemon moves - if expanded is Moves obj else list
        """
        super().__init__(name, pokeId)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        """
                string method
                :return: object printout - string
                """
        stat = ""
        for s in self.stats:
            a_string = str(s)
            stat = stat + a_string + "\n"
        abilt = ""
        for a in self.abilities:
            a_string = str(a)
            abilt = abilt + a_string + "\n"
        move = ""
        for m in self.moves:
            a_string = str(m)
            move += a_string + "\n\n"
        return f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Height: {self.height} decimeters\n" \
               f"weight: {self.weight} hectograms\n" \
               f"Types: {self.types}\n" \
               f"\n" \
               f"Stats:\n" \
               f"-----\n" \
               f"{stat}\n" \
               f"\n" \
               f"Abilities:\n" \
               f"-----\n" \
               f"\n" \
               f"{abilt}\n" \
               f"\n" \
               f"Moves:\n" \
               f"\n" \
               f"{move}\n"

    def __repr__(self):
        """
                string method
                :return: object printout - string
                """
        stat = ""
        for s in self.stats:
            a_string = str(s)
            stat = stat + a_string + "\n"
        abilt = ""
        for a in self.abilities:
            a_string = str(a)
            abilt = abilt + a_string + "\n"
        move = ""
        for m in self.moves:
            a_string = str(m)
            move += a_string + "\n\n"
        return f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Height: {self.height} decimeters\n" \
               f"weight: {self.weight} hectograms\n" \
               f"Types: {self.types}\n" \
               f"\n" \
               f"Stats:\n" \
               f"-----\n" \
               f"{stat}\n" \
               f"\n" \
               f"Abilities:\n" \
               f"-----\n" \
               f"\n" \
               f"{abilt}\n" \
               f"\n" \
               f"Moves:\n" \
               f"\n" \
               f"{move}\n"


class Ability(PokedexObject):
    """
    Ability class

    - extends PokedexObject
    """
    def __init__(self, name, pokeId=None, generation=None,
                 effect=None, shortEffect=None, pokemon=None):
        """
        Ability init
        :param name: ability name - string
        :param pokeId: ability id - string
        :param generation: ability generation - string
        :param effect: ability effect - string
        :param shortEffect: ability effect (short) - string
        :param pokemon: ability pokemon - list
        """
        super().__init__(name, pokeId)
        self.generation = generation
        self.effect = effect
        self.shortEffect = shortEffect
        self.pokemon = pokemon

    def __str__(self):
        poke = ""
        for p in self.pokemon:
            a_string = str(p)
            poke += a_string + ", "
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(Short): {self.shortEffect}\n" \
               f"Pokemon: {poke}\n"

    def __repr__(self):
        poke = ""
        for p in self.pokemon:
            a_string = str(p)
            poke += a_string + ", "
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(Short): {self.shortEffect}\n" \
               f"Pokemon: {poke}\n"


class Stat(PokedexObject):
    """
    Stat object

    - extends PokedexObject
    - used when Pokemon is extended
    """
    def __init__(self, name, base_stat, url=None, name_expanded=None, pokeId=None, isBattleOnly=None, isExpanded=False):
        super().__init__(name, pokeId)
        self.base_stat = base_stat
        self.url = url
        self.name_expanded = name_expanded
        self.isBattleOnly = isBattleOnly
        self.isExpanded = isExpanded

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Battle Only: {self.isBattleOnly}\n"

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Battle Only: {self.isBattleOnly}\n"


class Moves(PokedexObject):
    def __init__(self, name, level_acquired, poke_id=None, generation=None,
                 accuracy=None, pp=None, power=None, types=None,
                 damage_class=None):
        super().__init__(name, poke_id)
        self.level_acquired = level_acquired
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.types = types
        self.damageClass = damage_class

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generations: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Types: {self.types}\n" \
               f"Damage Class: {self.damageClass}\n"

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generations: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Types: {self.types}\n" \
               f"Damage Class: {self.damageClass}\n"