from pokemonretriever.pokeData import Pokemon, Ability, Moves, Stat
from abc import ABC, abstractmethod
import aiohttp
import asyncio


class Factory(ABC):

    @classmethod
    @abstractmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool, session: aiohttp.ClientSession):
        pass

    @classmethod
    @abstractmethod
    def grab_urls(cls, d: dict):
        pass


async def get_expanded_object(url, session):
    response = await session.request(method="GET", url=url)
    json_dict = await response.json()
    return json_dict


class pokemonFactory(Factory):

    @classmethod
    def grab_urls(cls, d: dict):
        try:
            stat_urls = [s.get("stat").get("url") for s in d.get("stats")]
            ability_urls = [a.get("ability").get("url") for a in d.get("abilities")]
            move_urls = [m.get("move").get("url") for m in d.get("moves")]
            return stat_urls, ability_urls, move_urls
        except TypeError:
            pass

    @classmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool, session: aiohttp.ClientSession):
        if d is not None:
            try:
                if expanded:
                    stat_urls, ability_urls, move_urls = cls.grab_urls(d)
                    if stat_urls and ability_urls and move_urls is not None:
                        # Get expanded type returns all the necessary variables in a list that are used for
                        # the expanded variant of the corresponding type.
                        list_stat_tasks = [asyncio.create_task(get_expanded_object(url, session)) for url in stat_urls]
                        stat_responses = await asyncio.gather(*list_stat_tasks)
                        list_ability_tasks = [asyncio.create_task(get_expanded_object(url, session)) for url in
                                              ability_urls]
                        ability_responses = await asyncio.gather(*list_ability_tasks)
                        list_move_tasks = [asyncio.create_task(get_expanded_object(url, session)) for url in move_urls]
                        move_responses = await asyncio.gather(*list_move_tasks)
                        stat_dicts = [s for s in d.get("stats")]
                        ability_dicts = [a for a in d.get("abilities")]
                        move_dicts = [m for m in d.get("moves")]
                        list_of_stats = []
                        for (s1, s2) in zip(stat_dicts, stat_responses):
                            list_of_stats.append(
                                Stat(s1.get("stat").get("name"), s1.get("base_stat"), None, s2.get("name"),
                                     s2.get("id"), s2.get("is_battle_only")))
                        p_lists = list()
                        for r in ability_responses:
                            p_lists.append(r.get("pokemon"))
                        pokemon_lists = list()
                        for a_list in p_lists:
                            temp_list = [p.get("pokemon").get("name") for p in a_list]
                            pokemon_lists.append(temp_list)
                        list_of_abilities = []
                        for (a1, a2, p) in zip(ability_dicts, ability_responses, pokemon_lists):
                            list_of_abilities.append(
                                Ability(a1.get("ability").get("name"), a2.get("id"), a2.get("generation")
                                        .get("name"), a2.get("effect_entries")[0].get("effect"), a2
                                        .get("effect_entries")[0].get("short_effect"), p))
                        list_of_moves = []
                        for (m1, m2) in zip(move_dicts, move_responses):
                            list_details = m1.get("version_group_details")
                            list_of_moves.append(Moves(m1.get("move").get("name"), list_details[0]
                                                       .get("level_learned_at"), m2.get("id"),
                                                       m2.get("generation").get("name"), m2
                                                       .get("accuracy"), m2.get("pp"), m2.get("power"),
                                                       m2.get("type").get("name"),
                                                       m2.get("damage_class").get("name")))
                        list_of_types = [t.get("type").get("name") for t in d.get("types")]
                        # Loop through corresponding responses and dictionaries above to append the
                        # corresponding objects into the corresponding lists. indexes at stat_responses will line up
                        # with indexes and stat_dicts for each pokemon. Grab necessary data from each and append to
                        # corresponding list.
                        return Pokemon(d.get('name'), d.get('id'), d.get('height'), d.get('weight'), list_of_stats,
                                       list_of_types,
                                       list_of_abilities, list_of_moves)

                else:
                    list_of_stats = [Stat(s.get("stat").get("name"), s.get("base_stat")) for s in d.get("stats")]
                    list_of_types = [t.get("type").get("name") for t in d.get("types")]
                    list_of_abilities = [Ability(a.get("ability").get("name")) for a in d.get("abilities")]
                    list_of_moves = [Moves(m.get("move").get("name"), m.get("version_group_details")
                                           .get("level_learned_at")) for m in d.get("moves")]
                    return Pokemon(d.get('name'), d.get('id'), d.get('height'), d.get('weight'), list_of_stats,
                                   list_of_types,
                                   list_of_abilities, list_of_moves)
            except AttributeError:
                pass


class abilityFactory(Factory):

    @classmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool, session: aiohttp.ClientSession):
        learned_list = d.get("pokemon")
        final_list = list()
        for p in learned_list:
            final_list.append(p.get("pokemon").get("name"))
        return Ability(d.get("name"), d.get("id"), d.get("generation").get("name"), d.get("effect_entries")[1]
                       .get("effect"), d
                       .get("effect_entries")[1].get("short_effect"), final_list)

    @classmethod
    def grab_urls(cls, d: dict):
        try:
            return [a.get("ability").get("url") for a in d.get("abilities")]
        except TypeError:
            pass


class moveFactory(Factory):

    @classmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool, session: aiohttp.ClientSession):
        if d is not None:
            learned_list = d.get("learned_by_pokemon")
            final_list = list()
            for p in learned_list:
                final_list.append(p.get("name"))
            return Moves(d.get("name"), "N/A", d.get("id"), d.get("generation").get("name"),
                         d.get("accuracy"), d.get("pp"), d.get("power"), d.get("type").get("name"),
                         d.get("damage_class").get("name"))

    @classmethod
    def grab_urls(cls, d: dict):
        try:
            return [m.get("move").get("url") for m in d.get("moves")]
        except TypeError:
            pass
