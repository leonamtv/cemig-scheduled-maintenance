import argparse

from core.config import argument_parser_description

parser = argparse.ArgumentParser(description=argument_parser_description, add_help=False)

parser.add_argument('-c', '--city', action='store',
                    help='Nome da cidade a procurar')
parser.add_argument('-t', '--token', action='store',
                    help='Token do Bot no Telegram')
parser.add_argument('-h', '--help', action='help',
                    help='Mostra essa mensagem e sai.')

args = parser.parse_args()


def get_city():
    if args.city:
        return args.city
    return None
