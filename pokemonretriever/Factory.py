from pokeData import Pokemon, Ability, Moves, Stat
from abc import ABC, abstractmethod
import aiohttp
import asyncio


class Factory(ABC):

    @classmethod
    @abstractmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool):
        pass

    @classmethod
    @abstractmethod
    def grab_urls(cls, d: dict):
        pass


class pokemonFactory(Factory):

    @classmethod
    def grab_urls(cls, d: dict):
        stat_urls = [s.get("stats").get("url") for s in d.get("stats")]
        type_urls = [t.get("type").get("url") for t in d.get("types")]
        ability_urls = [a.get("ability").get("url") for a in d.get("abilities")]
        move_urls = [m.get("move").get("url") for m in d.get("moves")]
        return stat_urls, type_urls, ability_urls, move_urls

    @classmethod
    async def create_pokedex_entry(cls, d: dict, expanded: bool):
        if expanded:
            stat_urls, type_urls, ability_urls, move_urls = cls.grab_urls(d)
            async with aiohttp.ClientSession() as session:
                # Get expanded type returns all the necessary variables in a list that are used for
                # the expanded variant of the corresponding type.
                list_stat_tasks = [asyncio.create_task(get_expanded_stats(url, session)) for url in stat_urls]
                list_type_tasks = [asyncio.create_task(get_expanded_types(url, session)) for url in type_urls]
                list_ability_tasks = [asyncio.create_task(get_expanded_abilities(url, session)) for url in ability_urls]
                list_move_tasks = [asyncio.create_task(get_expanded_moves(url, session)) for url in move_urls]
                stat_responses = await asyncio.gather(*list_stat_tasks)
                type_responses = await asyncio.gather(*list_type_tasks)
                ability_responses = await asyncio.gather(*list_ability_tasks)
                move_responses = await asyncio.gather(*list_move_tasks)
                stat_dicts = [s for s in d.get("stats")]
                type_dicts = [t for t in d.get("types")]
                ability_dicts = [a for a in d.get("abilities")]
                move_dicts = [m for m in d.get("moves")]
                list_of_stats = list()
                list_of_types = list()
                list_of_abilities = list()
                list_of_moves = list()
                # Loop through corresponding responses and dictionaries above to append the
                # corresponding objects into the corresponding lists. indexes at stat_responses will line up
                # with indexes and stat_dicts for each pokemon. Grab necessary data from each and append to
                # corresponding list.

        else:
            list_of_stats = [Stat(s.get("stat").get("name"), s.get("base_stat")) for s in d.get("stats")]
            list_of_types = [t.get("type").get("name") for t in d.get("types")]
            list_of_abilities = [Ability(a.get("ability").get("name")) for a in d.get("abilities")]
            list_of_moves = [Moves(m.get("move").get("name"), m.get("version_group_details")
                                   .get("level_learned_at")) for m in d.get("moves")]
        return Pokemon(d.get('name'), d.get('id'), d.get('height'), d.get('weight'), list_of_stats, list_of_types,
                        list_of_abilities, list_of_moves)
