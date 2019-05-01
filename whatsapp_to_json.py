import csv
import os
import sys
import json
import datetime
import time
import re

path = sys.argv[1]

data = {}

def makejson(filename):
	person_chats = {}
	with open(path + '/' + filename, 'r') as file:
		chat = file.read()
		dates = re.findall('\d{2}/\d{2}/\d{4}', chat)

		datedict = {}
		for date in dates:
			date = date[6:10] + date[3:5] + date[0:2]
			if date not in datedict:
				datedict[date] = 0
			datedict[date] += 1

		data[filename[:-4]] = datedict
		data[filename[:-4]]['total'] = len(dates)

for f in os.listdir(path):
	if '.txt' in f:
		makejson(f)
		

with open('msgs/whatsapp_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)