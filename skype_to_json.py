import csv
import os
import sys
import json
import datetime

data = {}

names = {
	'hamza.breteche': 'hamzabreteche',
	'gabbymacarberry': 'gabriellecarberry',
	'sachinvasudevan27': 'sachinvasudevan',
	'lamsjr': 'alexlams',
	'live:agurling3': 'alistairgurling',
	'kostyam12': 'constantinemalinovski',
	'ossian1234': 'ossiankeith',
	'constantinemalinovski': 'constantinemalinovski',
	'selvinoselbaraju': 'selvinselbaraju'
}

def parse_msg(row):

	name = row[0]

	if name not in names or name == 'chatname' or name[0] == '#' or name[:3] == '19:':
		return

	timestamp = int(row[1])

	date = str(datetime.datetime.fromtimestamp(timestamp))[:10].replace('-','')

	name = names[name]

	if name not in data:
		data[name] = {'total': 0}

	if date not in data[name]:
		data[name][date] = 0

	data[name][date] += 1
	data[name]['total'] += 1


with open('data/skype_data.csv', 'rb') as file:
	reader = csv.reader(file)
	for row in reader:
		parse_msg(row)

with open('msgs/skype_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)






