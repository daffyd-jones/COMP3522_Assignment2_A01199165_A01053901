import facade
from pokemonretriever.request import Request
import argparse


def main():
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
    facade.execute_request(request)


def print_content(poke_list):
    for i in poke_list:
        print(i)


# def main():
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                         help='an integer for the accumulator')
#     parser.add_argument('--sum', dest='accumulate', action='store_const',
#                         const=sum, default=max,
#                         help='sum the integers (default: find the max)')
#
#     args = parser.parse_args('')
#     print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
