import json


import requests

from pokemonretriever.Factory import Factory


class Facade:
    def __init__(self):
        pass


def set_environment(request):
    mode = request.get_mode()
    if mode == "pokemon":
        url = "https://pokeapi.co/api/v2/pokemon/"
        factory = pokemonFactory()
    elif mode == "ability":
        url = "https://pokeapi.co/api/v2/ability/"
        factory = abilityFactory()
    elif mode == "move":
        url = "https://pokeapi.co/api/v2/move/"
        factory = moveFactory()
    else:
        raise ValueError
    return url, factory


def execute_request(request):
    url, factory = set_environment(request)

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
