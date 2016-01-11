from threading import Thread

from core.shared import *


def listener():
    while (True):
        message = inbox.get()
        print(message)


def init():
    setup()

    listenerd = Thread(target=listener, name='Listener Daemon')
    listenerd.setDaemon(True)
    listenerd.start()


def setup():
    print('Loading configuration...')
    config.load(config)
    users.load(users)
    groups.load(groups)

    if not config.keys.bot_api_token and not config.keys.tg_cli_port:
        print('\nFrontend not configured!')
        print('\tSelect the Frontend to use:\n\t\t0. Telegram Bot API\n\t\t1. Telegram-CLI')
        frontend = input('\tFrontend: ')
        if frontend == '1':
            config.keys.tg_cli_port = input('\tTelegram-CLI port: ')
        else:
            config.keys.bot_api_token = input('\tTelegram Bot API token: ')
        config.save(config)
    else:
        if config.keys.bot_api_token:
            print('\nUsing Telegram Bot API token: {}'.format(config.keys.bot_api_token))
        elif config.keys.tg_cli_port:
            print('\nUsing Telegram-CLI port: {}'.format(config.keys.tg_cli_port))
