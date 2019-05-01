import os
import json
import datetime as dt
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
from scipy.ndimage.filters import gaussian_filter1d

people = ['gabriellecarberry', 'ossiankeith', 'shamidezylva', 'ollyspringman', 'maxhaines', 'amyjeffcoate', 'kirachathli']
# people = ['sachinvasudevan', 'hamzabreteche', 'selvinselbaraju']

# pyplot.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
# pyplot.gca().xaxis.set_major_locator(mdates.DayLocator())

def format_date(d):
	return d[6:] + '/' + d[4:6] + '/' + d[:4]

with open('msgs/total_msgs.json', 'r') as file:
# with open('msgs/' + filename, 'r') as file:
	messenger = json.load(file)

	for name in people:
		person = messenger[name]
		del person['total']
		points = zip(person.keys(), person.values())
		points.sort(key=lambda x : x[0])
		points = zip(*points)
		dates = [dt.datetime.strptime(format_date(d), '%d/%m/%Y').date() for d in points[0]]

		y_smooth = gaussian_filter1d(points[1], sigma=10)

		pyplot.plot(dates, y_smooth, label=name)

pyplot.legend()
pyplot.show()
# pyplot.gcf().autofmt_xdate()