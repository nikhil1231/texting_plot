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
		shami = re.findall('Shami', chat)
		nikhil = re.findall('Nikhil', chat)

		print "Beg percentage: " + str(100 * float(len(shami)) / (float(len(shami) + len(nikhil)))) + "%"

for f in os.listdir(path):
	if '.txt' in f:
		makejson(f)