import json
from enum import Enum, auto

import requests


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
        # build objects based on Mode value


def string_build(request):
    base = "https://pokeapi.co/api/v2"
    temp = base + f"/{request.mode}"
    return temp
