import csv
import os
import sys
import json

path = sys.argv[1]

data = {}

def makejson(filename):
	person_chats = {}
	total = 0
	with open(path + '/' + filename, 'rb') as file:
		reader = csv.reader(file)
		for row in reader:
			total += 1
			if len(row) == 0 or row[0][0:4] != '2013':
				continue
			if row[0][:8] in person_chats:
				person_chats[row[0][:8]] += 1

			else:
				person_chats[row[0][:8]] = 1
	person_chats['total'] = total
	data[filename[:-4]] = person_chats
for f in os.listdir(path):
	if '.csv' in f:
		makejson(f)

with open('msgs/bbm_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)