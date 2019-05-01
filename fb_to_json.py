import csv
import os
import sys
import json
import datetime
import time

path = sys.argv[1]

data = {}

def makejson(filename):
	person_chats = {}
	total = 0
	with open(path + '/' + filename + '/message_1.json', 'r') as file:
		chat = json.load(file)
		for msg in chat['messages']:
			total += 1
			date = str(datetime.datetime.fromtimestamp(msg['timestamp_ms']/1000.0))[:10].replace('-','')
			if date in person_chats:
				person_chats[date] += 1
			else:
				person_chats[date] = 1
	person_chats['total'] = total
	data[filename[:-11]] = person_chats

with open('fb_names.json', 'r') as jsonfile:
	names = json.load(jsonfile)
	for name in names:
		makejson(name)
		

with open('msgs/fb_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)