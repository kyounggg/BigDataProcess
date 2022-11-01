#!/usr/bin/python3

import sys
from datetime import datetime

f = open(sys.argv[1], 'r')
fw = open(sys.argv[2], 'wt')

def get_the_day(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	temp = date.split('/')
	_date = datetime(int(temp[2]), int(temp[0]), int(temp[1]))
	day = _date.weekday()
	return days[day]

list_uber = []

for line in f:
	line = line.strip()
	arr_line = line.split(',')
	fw.write(arr_line[0])
	day = get_the_day(arr_line[1])
	fw.write(",")
	fw.write(day)
	fw.write(" ")
	fw.write(arr_line[2])
	fw.write(arr_line[3])
	fw.write("\n")

f.close()
fw.close()

