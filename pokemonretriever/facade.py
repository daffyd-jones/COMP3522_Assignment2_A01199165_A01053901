import json
from enum import Enum, auto

import requests

from pokemonretriever.Factory import Factory


class Mode(Enum):
    POKEMON = auto()
    ABILITY = auto()
    MOVE = auto()


class Facade:
    def __init__(self):
        pass

    def execute_request(self, request):
        url = string_build(request)
        response = requests.get(url)
        got = response.json()
        maker = Factory(request.get_mode())
        poke_list = []
        for i in got:
            # get necessary items from json
            # for now i to kwargs
            poke_dict = maker.filter_json(i)
            temp = maker.make(**poke_dict)
            poke_list[i] = temp
        return poke_list


def string_build(request):
    base = "https://pokeapi.co/api/v2"
    temp = base + f"/{request.endpoint}"
    return temp

