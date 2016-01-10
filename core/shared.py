from core.frontend.bot_api import *
from core.types import *
from core.utils import *

from collections import OrderedDict
from queue import Queue
from threading import Thread
import requests
import json
import magic
import mimetypes
import tempfile
from datetime import datetime
import os

config = Config.Settings
lang = Config.Language
users = OrderedDict()
groups = OrderedDict()

inbox = Queue()
outbox = Queue()

msg_index = 1