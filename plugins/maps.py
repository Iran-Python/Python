from __main__ import *
from utilies import *

commands = [
	'^map',
	'^m ',
	'^location',
	'^loc ',
	'^l ',
]
parameters = (
	('location', True),
)
description = 'Returns a map for a specified location.'
typing = True

def action(msg):
	input = get_input(msg['text'])

	if not input:
		doc = get_doc(commands, parameters, description)
		return send_message(msg['chat']['id'], doc, parse_mode="Markdown")	
		
	lat,lon,locality,country = get_coords(input)
	
	if get_command(msg['text']).startswith('m'): 
		photo_url = 'https://maps.googleapis.com/maps/api/staticmap'
		photo_params = {
			'size': '640x320',
			'markers': 'color:red|label:X|' + str(lat) + ',' + str(lon),
			'key': config['api']['googledev']
		}
		
		message = locality + ' (' + country + ')'
		
		map = download(photo_url, params=photo_params)
		
		if map:
			send_photo(msg['chat']['id'], map)
		else:
			send_message(msg['chat']['id'], locale[get_locale(msg['chat']['id'])]['errors']['download'], parse_mode="Markdown")
	else:
		send_location(msg['chat']['id'], lat, lon)