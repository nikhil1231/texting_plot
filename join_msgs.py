import os
import json
from collections import Counter

data = {}

def load_json_file(filename):
	global data
	with open('msgs/' + filename, 'r') as file:
		messenger = json.load(file)

		if not data:
			data = messenger
			return

		for name in messenger:
			if name not in data:
				data[name] = messenger[name]
			else:
				for date in messenger[name]:
					if date not in data[name]:
						data[name][date] = messenger[name][date]
					else:
						data[name][date] += messenger[name][date]


		# print(data)

for f in os.listdir('./msgs'):
	if '.json' in f:
		load_json_file(f)


with open('msgs/total_msgs.json', 'w') as jsonfile:
	json.dump(data, jsonfile)