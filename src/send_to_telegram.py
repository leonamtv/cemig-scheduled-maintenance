import argparse
import telepot


parser = argparse.ArgumentParser(description="Script para enviar para o telegram", add_help=False)

parser.add_argument('-t', '--token', action='store',
                    help='Token do Bot no Telegram')
parser.add_argument('-c', '--chat-id', action='store',
                    help='Id do chat no Telegram')
parser.add_argument('-m', '--message', action='store',
                    help='Mensagem a enviar para o Telegram')
parser.add_argument('-h', '--help', action='help',
                    help='Mostra essa mensagem e sai.')

args = parser.parse_args()


def break_message(messages_to_send):
    return messages_to_send.split("***")


if args.token and args.chat_id and args.message:
    bot = telepot.Bot(token=args.token)
    for message in break_message(args.message):
        if message is not None and message != '':
            bot.sendMessage(chat_id=args.chat_id, text=message)

