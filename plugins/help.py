from __main__ import *
from utilies import *

commands = [
	'^help',
	'^commands',
	'^h$'
]
parameters = (
	('command', False),
)
description = 'Get list of basic information for all commands, or more detailed documentation on a specified command.'
typing = True
hidden = True

def action(msg):			
	input = get_input(msg['text'])
	
	if input:
		for i,v in plugins.items():
			if not hasattr(v, 'hidden'):
				if config['command_start'] + input == v.commands[0].replace('^', '#'):
					doc = config['command_start'] + v.commands[0].replace('^', '')
					if hasattr(v, 'parameters'):
						doc += format_parameters(v.parameters)
					doc += '\n' + v.description
					return send_message(msg['chat']['id'], doc, parse_mode="Markdown")
	else:
		help = ''
		for i,v in plugins.items():
			if not hasattr(v, 'hidden'):
				help += '\t' + config['command_start']
				help += v.commands[0].replace('^', '')
				
				if hasattr(v, 'parameters'):
						help += format_parameters(v.parameters)
				help += '\n'
			
		message = '*Commands*:\n' + help
		
		if msg['from']['id'] != msg['chat']['id']:
			if not send_message(msg['from']['id'], message, parse_mode="Markdown"):
				return send_message(msg['chat']['id'], message, parse_mode="Markdown")
			return send_message(msg['chat']['id'], 'I have sent it in a *private message*.', parse_mode="Markdown")
		else:
			return send_message(msg['chat']['id'], message, parse_mode="Markdown")