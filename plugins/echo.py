from polaris.utils import *

commands = {
    '^echo': {('text', True)}
}
description = 'Repeat a string.'
action = 'typing'

def run(msg):
    input = get_input(msg.text)

    if not input:
        doc = get_doc(commands, description)
        return send_message(msg.cid, doc, markup=True)

    send_message(msg.cid, input, markup=True)
