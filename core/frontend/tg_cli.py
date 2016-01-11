from core.shared import *
from threading import Thread


def inbox_daemon():
    message = Message
    inbox.put(message)


def outbox_daemon():
    message = inbox.get()
    print(message)


inboxd = Thread(target=inbox_daemon, name='Inbox Daemon')
inboxd.setDaemon(True)

outboxd = Thread(target=outbox_daemon, name='Outbox Daemon')
outboxd.setDaemon(True)


def send_message(message):
    pass


def get_me():
    pass


def init():
    inboxd.start()
    outboxd.start()
