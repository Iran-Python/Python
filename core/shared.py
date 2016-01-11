from core.utils import *
from collections import OrderedDict
from queue import Queue
from core.types import Config

bot = Bot

config = Config.Config
lang = Config.Language
users = OrderedDict()
groups = OrderedDict()

inbox = Queue()
outbox = Queue()

msg_index = 1