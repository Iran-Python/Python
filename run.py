from core.shared import *

if not config.keys:
    print('NO CONFIGURATION FILE FOUND!')
    print('But we will set up one now.')
    print('\nSelect the frontend to use:\n\t0. Telegram Bot API\n\t1. Telegram-CLI')
    choice = input('Choice: ')
    print('\nYour choice: {}'.format(choice))
