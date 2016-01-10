from core.shared import *

def init():
    config.load()
    users.load()
    groups.load()


def inbox_listener():
    while (True):
        inbox.get()
