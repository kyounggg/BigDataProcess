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
	day = get_the_day(arr_line[1])
	arr_list = []
	arr_list.append(arr_line[0])
	arr_list.append(day)
	arr_list.append(arr_line[2])
	arr_list.append(arr_line[3]) 
	list_uber.append(arr_list) 

dic_uber = {}
for line in list_uber:
	temp = []
	temp_list = []
	temp.append(line[1])
	temp.append(line[2])
	temp.append(line[3])
	if line[0] in dic_uber:
		temp_list.extend(dic_uber[line[0]])	
		temp_list.append(temp)
	else:
		temp_list.append(temp)
	dic_uber[line[0]] = temp_list	

for k, v in dic_uber.items():
	for i in v:
		fw.write(k+","+i[0]+" "+i[1]+","+i[2]+"\n")

f.close()
fw.close()

