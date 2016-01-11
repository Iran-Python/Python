from core.shared import *
from threading import Thread


def inbox_daemon():
    pass


def outbox_daemon():
    pass


inboxd = Thread(target=inbox_daemon, name='Inbox Daemon')
inboxd.setDaemon(True)
inboxd.start()

outboxd = Thread(target=outbox_daemon, name='Outbox Daemon')
outboxd.setDaemon(True)
outboxd.start()

def send_message(message):
    pass


def get_me():
    pass
