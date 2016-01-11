from core.shared import *
from threading import Thread
from pyfiglet import Figlet


def listener():
    while (True):
        message = inbox.get()
        print('GOT MESSAGE: ' + message.content)


def init():
    f = Figlet(font='standard')
    print(f.renderText('Polaris 2.0'))

    setup()

    bot.f.init()

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
            config.frontend = 'tg_cli'
        else:
            config.keys.bot_api_token = input('\tTelegram Bot API token: ')
            config.frontend = 'bot_api'
        config.save(config)
    else:
        if config.keys.bot_api_token:
            print('\nUsing Telegram Bot API token: {}'.format(config.keys.bot_api_token))
        elif config.keys.tg_cli_port:
            print('\nUsing Telegram-CLI port: {}'.format(config.keys.tg_cli_port))

    bot.set_frontend(config.frontend)
