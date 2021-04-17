import datetime

import facade
from pokemonretriever.request import Request
import argparse
import asyncio


class FileHandler:
    """
    handles file in/out
    """
    def __init__(self, file):
        """
        file to be manipulated
        :param file: string
        """
        self.file = file

    def file_in(self):
        """
        reads file and returns line_list
        :return: string
        """
        line_list = []
        try:
            with open(self.file, "r") as file:
                for line in file:
                    line = line.strip()
                    line_list.append(line)
            return line_list
        except FileNotFoundError:
            print("Incorrect file name")

    def file_out(self, poke_list):
        """
        takes in list and writes to file
        :param poke_list: list of PokemonObjects - list
        :return: void
        """
        try:
            with open(self.file, 'w') as file:
                now = datetime.datetime.now()

                file.write(f"Timestamp: {now}")
                file.write(f"Number of requests: {len(poke_list)}\n")
                for poke in poke_list:
                    file.write("%s\n" % poke)
            print(f"file {self.file} has been written")
        except FileExistsError:
            print("please use another file name")


def main():
    """
    runs program

    uses argparse to obtain user arguments
    uses gained arguments  to build Request object
    Request passed to Facade
    :return: void
    """
    # argparser code
    parser = argparse.ArgumentParser(description='Simulates a Pokedex')
    parser.add_argument('mode', choices=["pokemon", "ability", "move"], help="Modes: pokemon | ability "
                                                                             "| move", metavar='M')
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--inputfile', dest='type')
    input_group.add_argument('--inputdata', dest='type')
    parser.add_argument('--expanded', action='store_true', dest='exp')
    parser.add_argument('--output', dest='out')
    args = parser.parse_args()
    request = Request(args.mode, args.type, args.exp, args.out)
    loop = asyncio.get_event_loop()
    pokedex_object_list = loop.run_until_complete(facade.execute_request(request))
    # if ".txt" in request.get_input():
    #     reader = FileHandler(request.get_input())
    #     file_list = reader.file_in()
    #     request.set_input(file_list)
    # facade = Facade()
    # poke_list = execute_request(request)
    if request.get_output() is not None:
        if ".txt" in request.get_output():
            writer = FileHandler(request.get_output())
            writer.file_out(pokedex_object_list)
        else:
            pass
            print_content(pokedex_object_list)
    else:
        pass
        print_content(pokedex_object_list)


def print_content(poke_list):
    """
    prints pokedex_object_list
    :param poke_list: pokedex_object_list - list
    :return: void
    """
    now = datetime.datetime.now()
    print(f"Timestamp: {now}\n"
          f"Number of requests: {len(poke_list)}\n")
    for i in poke_list:
        print(i)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
