from core.shared import *
import json
from datetime import datetime


class Bot:
    frontend = None
    user = None

    def __init__(self, frontend=None):
        self.frontend = frontend


# This classes define and manage configuration files and stored data.
class Config:
    class Config:
        owner = None
        keys = Config.Config.Keys
        plugins = []
        start = '/'

        def load(self):
            try:
                with open('data/config.json', 'r') as f:
                    config_json = json.load(f, object_pairs_hook=OrderedDict)
                    keys = Config.Config.Keys
                    keys.bot_api_token = config_json['bot_api_token']
                    keys.tg_cli_port = config_json['tg_cli_port']
                    keys.cat_api = config_json['cat_api']
                    keys.giphy = config_json['giphy']
                    keys.league_of_legends = config_json['league_of_legends']
                    keys.openweathermap = config_json['openweathermap']
                    keys.google_developer_console = config_json['google_developer_console']
                    keys.azure_key = config_json['azure_key']
                    self.owner = config_json['owner']
                    self.keys = keys
                    self.plugins = config_json['plugins']
                    self.start = config_json['start']
                    print('\t[OK] ' + 'config.json LOADED')
            except:
                print('\t[Failed] ' + 'config.json NOT LOADED')
                keys = Config.Config.Keys
                keys.bot_api_token = None
                keys.tg_cli_port = None
                keys.cat_api = None
                keys.giphy = None
                keys.league_of_legends = None
                keys.openweathermap = None
                keys.google_developer_console = None
                keys.azure_key = None
                self.keys = keys

        def save(self):
            try:
                with open('data/config.json', 'r') as f:
                    config = OrderedDict
                    keys = OrderedDict
                    keys['bot_api_token'] = self.keys.bot_api_token
                    keys['tg_cli_port'] = self.keys.tg_cli_port
                    keys['cat_api'] = self.keys.cat_api
                    keys['giphy'] = self.keys.giphy
                    keys['league_of_legends'] = self.keys.league_of_legends
                    keys['openweathermap'] = self.keys.openweathermap
                    keys['google_developer_console'] = self.keys.google_developer_console
                    keys['azure_key'] = self.keys.azure_key

                    config['owner'] = self.owner
                    config['keys'] = keys
                    config['plugins'] = self.plugins
                    config['start'] = self.start

                    json.dump(config, f, sort_keys=True, indent=4)
                    print('\t[OK] config.json SAVED')
            except:
                print('\t[Failed] config.json NOT SAVED')

        # Keys store the API keys
        class Keys:
            bot_api_token = None
            tg_cli_port = None
            cat_api = None
            giphy = None
            league_of_legends = None
            openweathermap = None
            google_developer_console = None
            azure_key = None


class Language:
    message = OrderedDict()
    error = OrderedDict()
    plugins = OrderedDict()


class User:
    first_name = None
    last_name = None
    username = None
    tags = None
    settings = None

    def __init__(self, first_name, last_name=None, username=None, tags=None, settings=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.tags = tags
        self.settings = settings


class Group:
    title = None
    description = None
    realm = None
    rules = None
    tags = None

    def __init__(self, title, description=None, realm=None, rules=None, tags=None):
        self.title = title
        self.description = description
        self.realm = realm
        self.rules = rules
        self.tags = tags


class Message:
    mid = None
    sender = None
    receiver = None
    content = None
    type = None
    selfdate = None
    reply_id = None
    markup = None

    def __init__(self, sender, receiver, content, type='text', reply_id=None, markup=None):
        msg_index += 1
        self.mid = msg_index
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.type = type
        self.date = datetime.now()
        self.reply_id = reply_id
        self.markup = markup


class User:
    uid = None
    first_name = None
    last_name = None
    username = None
    photo = None

    def __init__(self, uid, first_name, last_name, username, photo):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class Group:
    gid = None
    title = None
    photo = None

    def __init__(self, gid, title, photo):
        self.gid = gid
        self.title = title
        self.photo = photo
