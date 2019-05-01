import csv
import os
import sys
import json

path = sys.argv[1]

arr = []

def makejson(filename):
	with open(path + '/' + filename + '/message_1.json', 'r') as file:
		chat = json.load(file)
		if len(chat['participants']) != 2 or os.path.getsize(path + '/' + filename + '/message_1.json') < 50000:
			return
		print filename
		arr.append(filename)
		
for f in os.listdir(path):
	if f != '.DS_Store':
		makejson(f)
	# break

with open('fb_names.json', 'w') as jsonfile:
	json.dump(arr, jsonfile)