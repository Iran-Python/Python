from core.frontend.bot_api import *
from core.types import *
from core.utils import *

from collections import OrderedDict
from queue import Queue
import requests
import json
import magic
import mimetypes
import tempfile
from datetime import datetime
import os

config = Config.Settings
config = Config.Locale
users = OrderedDict()
groups = OrderedDict()

inbox = Queue()
outbox = Queue()

msg_index = 1
