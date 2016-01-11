from core.utils import *
from collections import OrderedDict
from queue import Queue

bot = Bot

config = Config.Config
users = Config.Users
groups = Config.Groups
lang = Config.Language

inbox = Queue()
outbox = Queue()

msg_index = 1
