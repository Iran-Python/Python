from core.shared import *
from threading import Thread
import requests

# Telegram Bot API bindings
api_url = 'https://api.telegram.org/bot' + config.keys.bot_api_token + '/'
started = True


def send_request(url, params=None, headers=None, files=None, data=None):
    print('\tRequest: ' + url)

    result = requests.get(url, params=params, headers=headers, files=files, data=data)
    print('\t\t' + result)

    if result.status_code != 200:
        print('NOT OK')
        print(result.text)
        return False
    else:
        print('OK')

    print(result.text)

    return json.loads(result.text)


def api_request(api_method, params=None, headers=None, files=None):
    url = api_url + api_method

    return send_request(url, params, headers, files)


def get_updates(offset=None, limit=None, timeout=None):
    params = {}
    if offset:
        params['offset'] = offset
    if limit:
        params['limit'] = limit
    if timeout:
        params['timeout'] = timeout
    return api_request('getUpdates', params)


def get_me():
    result = api_request('getMe')
    print(result)
    bot.first_name = result['result']['first_name']
    bot.last_name = result['result']['last_name']
    bot.username = result['result']['username']
    bot.uid = result['result']['id']
    print('got me')


def send_message(message):
    pass


def inbox_daemon():
    print('Starting inbox daemon...')
    last_update = 0

    while started:
        updates = get_updates(last_update + 1)
        result = updates['result']

        print(updates)
        print(result)

        if result:
            for update in result:
                if update['update_id'] > last_update:
                    last_update = update['update_id']
                    msg = update['message']

                    if not 'inline_query' in update:
                        if hasattr(msg, 'text'):
                            # Generates a Message object and sends it to the inbox queue.
                            if msg['chat']['id'] > 0:
                                receiver = User
                                receiver.first_name = msg['chat']['title']
                            receiver.uid = msg['chat']['id']
                            sender = User
                            sender.uid = msg['from']['id']
                            sender.first_name = msg['from']['first_name']
                            sender.last_name = msg['from']['last_name']
                            sender.username = msg['from']['username']

                            message = Message(sender, receiver, msg['text'], type='text')
                            inbox.put(message)
                            print('INBOX: ' + message)
        else:
            print('Failed to get results')


def outbox_daemon():
    message = inbox.get()
    print('OUTBOX: ' + message)


inboxd = Thread(target=inbox_daemon, name='Inbox Daemon')
inboxd.setDaemon(True)

outboxd = Thread(target=outbox_daemon, name='Outbox Daemon')
outboxd.setDaemon(True)


def init():
    print('Initializing Telegram Bot API daemons...')
    inboxd.start()
    outboxd.start()
