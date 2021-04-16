import aiohttp
import asyncio

from pokemonretriever.Factory import pokemonFactory
from pokemonretriever.pokeData import PokedexObject


def set_environment(request):
    mode = request.get_mode()
    if mode == "pokemon":
        url = "https://pokeapi.co/api/v2/pokemon/"
        factory = pokemonFactory
    elif mode == "ability":
        url = "https://pokeapi.co/api/v2/ability/"
        factory = abilityFactory()
    elif mode == "move":
        url = "https://pokeapi.co/api/v2/move/"
        factory = moveFactory()
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
    response = await session.request(method="GET", url=url)
    print("Response object: \n", response)
    json_dict = await response.json()
    return json_dict


async def execute_request(request) -> PokedexObject:
    url, factory, request_input, request_output, is_expanded = set_environment(request)
    search_id = handle_input(request_input)
    if type(search_id) == list:
        async with aiohttp.ClientSession() as session:
            print("Processing request list")
            list_tasks = [asyncio.create_task(get_pokedex_data(url + id_ + '/', session))
                          for id_ in search_id]
            responses = await asyncio.gather(*list_tasks)
            response_tasks = [asyncio.create_task(factory.create_pokedex_entry(r, is_expanded)) for r in responses]
            object_list = await asyncio.gather(*response_tasks)
    else:
        async with aiohttp.ClientSession as session:
            print("Processing singular request")
            async_task = asyncio.create_task(get_pokedex_data(url + search_id + '/', session))
            response = await async_task
            loop = asyncio.get_event_loop()
            object_list = loop.run_until_complete(factory.create_pokedex_entry(response, is_expanded))
    return object_list
