from core.shared import *
from threading import Thread


def get_me():
    print('get_me()')
    pass


def send_message(message):
    print('send_message({})'.format(message))
    pass


def inbox_daemon():
    pass


def outbox_daemon():
    pass


inboxd = Thread(target=inbox_daemon, name='Inbox Daemon')
inboxd.setDaemon(True)

outboxd = Thread(target=outbox_daemon, name='Outbox Daemon')
outboxd.setDaemon(True)


def init():
    print('None...')
    inboxd.start()
    outboxd.start()
