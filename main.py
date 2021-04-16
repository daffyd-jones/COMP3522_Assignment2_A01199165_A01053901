from facade import Facade
from pokemonretriever.request import Request
import argparse


class FileHandler:
    def __init__(self, file):
        self.file = file

    def file_in(self):
        line_list = []
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip()
                line_list.append(line)
        return line_list

    def file_out(self, poke_list):
        with open(self.file, 'w') as file:
            for poke in poke_list:
                file.write("%s\n" % poke)
        print(f"file {self.file} has been written")


def main():
    # argparser code
    parser = argparse.ArgumentParser(description='Simulates a Pokedex')
    parser.add_argument('mode', choices=["pokemon", "ability", "move"], required=True, help="Modes: pokemon | ability "
                                                                                            "| move", metavar='M',
                        dest='mode')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--inputfile', dest='type')
    group.add_argument('--inputdata', dest='type')
    parser.add_argument('--expanded', action='store_true', dest='exp')
    parser.add_argument('--output', dest='out')
    args = parser.parse_args()
    request = Request(args.mode, args.type, args.exp, args.out)
    facade = Facade()
    poke_list = facade.execute_request(request)
    print_content(poke_list)


def print_content(poke_list):
    for i in poke_list:
        print(i)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
