from core.types import *
from queue import Queue

bot = Bot()

config = Config.Config
users = Config.Users
groups = Config.Groups
lang = Config.Language

inbox = Queue()
outbox = Queue()

msg_index = 1
user_index = 1
group_index = 1
