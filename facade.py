import aiohttp
import asyncio

from aiohttp import ContentTypeError

from pokemonretriever.Factory import pokemonFactory, abilityFactory, moveFactory
from pokemonretriever.pokeData import PokedexObject


def set_environment(request):
    """
    sets the mode that the request is querying
    sets factoty to appropriate Factory sub-class
    - pokemon, ability, move
    :param request: Request obj
    :return: endpoint url - string
             appropriate Factory - Factory
             request input - string
             request output - string
             request is_expanded - bool
    """
    mode = request.get_mode()
    if mode == "pokemon":
        url = "https://pokeapi.co/api/v2/pokemon/"
        factory = 1
    elif mode == "ability":
        url = "https://pokeapi.co/api/v2/ability/"
        factory = 2
    elif mode == "move":
        url = "https://pokeapi.co/api/v2/move/"
        factory = 3
    else:
        raise ValueError
    return url, factory, request.get_input(), request.get_output(), request.is_expanded()


def parse_file(url):
    with open(url, mode='r', encoding='utf-8') as input_file:
        data = list()
        for line in input_file.readlines():
            if line != "\n":
                data.append(line.strip('\n'))
        return data


def handle_input(request_input):
    if '.txt' in str(request_input):
        search_id = parse_file(request_input)
    else:
        search_id = request_input
    return search_id


async def get_pokedex_data(url, session):
    """
    queries endpoint and processes/returns it to/as json
    :param url: endpoint - string
    :param session: async session - "async with" var
    :return: json dict
    """
    try:
        response = await session.request(method="GET", url=url)
        json_dict = await response.json()
        print("Got json data")
        return json_dict
    except ContentTypeError:
        pass


async def execute_request(request) -> PokedexObject:
    """
    processes facade functionality request

    async queries endpoint and builds PokedexObject list
    :param request: request to be processed - Request
    :return: PokedexObject list
    """

    url, factory, request_input, request_output, is_expanded = set_environment(request)
    search_id = handle_input(request_input)
    print(search_id)
    async with aiohttp.ClientSession() as session:
        if type(search_id) == list:

            print("Processing request list")
            print(url)
            list_tasks = [asyncio.create_task(get_pokedex_data(url + id_ + '/', session))
                          for id_ in search_id]
            responses = await asyncio.gather(*list_tasks)
            if factory == 1:
                response_tasks = [asyncio.create_task(pokemonFactory.create_pokedex_entry(r, is_expanded, session)
                                                      ) for r in responses]
            elif factory == 2:
                response_tasks = [asyncio.create_task(abilityFactory.create_pokedex_entry(r, is_expanded, session)
                                                      ) for r in responses]
            elif factory == 3:
                response_tasks = [asyncio.create_task(moveFactory.create_pokedex_entry(r, is_expanded, session)
                                                      ) for r in responses]
            object_list = await asyncio.gather(*response_tasks)

        else:
            print("Processing singular request")
            response = await get_pokedex_data(url + search_id + '/', session)
            if factory == 1:
                object_list = await pokemonFactory.create_pokedex_entry(response, is_expanded, session)
            elif factory == 2:
                object_list = await abilityFactory.create_pokedex_entry(response, is_expanded, session)
            elif factory == 3:
                object_list = await moveFactory.create_pokedex_entry(response, is_expanded, session)
    return object_list
