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

def print_list_uber(list_uber):
	for i in list_uber:
		fw.write(i[0]+","+i[1]+" "+i[2]+","+i[3]+"\n")	
list_uber = []

for line in f:
	line = line.strip()
	arr_line = line.split(',')
	day = get_the_day(arr_line[1])
	arr_list = []
	arr_list.append(arr_line[0])
	arr_list.append(day)
	arr_list.append(arr_line[2])
	arr_list.append(arr_line[3]) 
	list_uber.append(arr_list) 
print_list_uber(list_uber)

f.close()
fw.close()

