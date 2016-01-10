from core.shared import *


class Bot:
    def __init__(self, bindings):
        self.bindings = bindings


class Config:
    class Settings:
        def __init__(self, owner, keys, plugins, ignore, start):
            self.owner = owner
            self.keys = keys
            self.plugins = plugins
            self.ignore = ignore
            self.start = start

    class Locale:
        def __init__(self, message, error, plugins):
            self.message = message
            self.error = error
            self.plugins = plugins

    class User:
        def __init__(self, first_name, last_name=None, username=None, tags=None, settings=None):
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.tags = tags
            self.settings = settings

    class Group:
        def __init__(self, title, description=None, realm=None, rules=None, tags=None):
            self.title = title
            self.description = description
            self.realm = realm
            self.rules = rules
            self.tags = tags


class Message:
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
    def __init__(self, uid, first_name, last_name, username, photo):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class Group:
    def __init__(self, gid, title, photo):
        self.gid = gid
        self.title = title
        self.photo = photo
