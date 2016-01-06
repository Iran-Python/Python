class Bot:
    def __init__(self, bindings):
        self.bindings = bindings


class Bindings:
    def __init__(self, module):
        self.module = module


class Update:
    def __init__(self, message, type):
        self.message = message
        self.type = type


class Message:
    def __init__(self, id, sender, receiver, content, type, date, reply_id):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.type = type
        self.date = date
        self.reply_id = reply_id


class User:
    def __init__(self, message, type):
        self.message = message
        self.type = type
