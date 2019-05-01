import csv
import os
import sys
import json
import datetime
import time

path = sys.argv[1]

data = {}

names = {
	'sachinvasudevan': 'sachinvasudevan',
	'hamzabreteche': 'hamzabreteche',
	'koineko': 'amyjeffcoate',
	'selvino': 'selvinselbaraju',
	'willstani': 'willstanistreet',
	'nikesh.parmar': 'nikeshparmar',
	'ossian_keith': 'ossiankeith',
	'PARAMOOOOORRREEE': 'amyjeffcoate',
	'sophtheoaf': 'sophiechan',
	'maxhaines1234': 'maxhaines'
}

def parse_msg(msg):
	name = msg['name']

	if name not in names:
		return

	date = msg['date'][:10].replace('-','')

	name = names[name]

	if name not in data:
		data[name] = {'total': 0}

	if date not in data[name]:
		data[name][date] = 0

	data[name][date] += 1
	data[name]['total'] += 1

with open(path + '/chat_history.json', 'r') as jsonfile:
	chats = json.load(jsonfile)
	for msg in chats['Received Chat History']:
		parse_msg({'name': msg['From'], 'date': msg['Created']})
		# break

	for msg in chats['Sent Chat History']:
		parse_msg({'name': msg['To'], 'date': msg['Created']})
		# break

with open(path + '/snap_history.json', 'r') as jsonfile:
	chats = json.load(jsonfile)
	for msg in chats['Received Snap History']:
		parse_msg({'name': msg['From'], 'date': msg['Created']})
		# break

	for msg in chats['Sent Snap History']:
		parse_msg({'name': msg['To'], 'date': msg['Created']})
		# break

with open('msgs/sc_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)