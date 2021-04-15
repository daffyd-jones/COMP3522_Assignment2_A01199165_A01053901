from pokemonretriever.facade import Facade
from pokemonretriever.request import Request
import argparse


def main():
    # argparser code
    parser = argparse.ArgumentParser(description='Simulates a Pokedex')
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('mode', metavar='M', help='pokedex mode')

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('--inputfile', )
    parser.add_argument('--input', )
    request = Request()
    # load request
    # -------
    facade = Facade()
    poke_list = facade.execute_request(request)
    print_content(poke_list)


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
