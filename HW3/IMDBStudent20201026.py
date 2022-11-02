#!/usr/bin/python3

import sys

f = open(sys.argv[1], 'r')
fw = open(sys.argv[2], 'wt')

dic_genre = {}

for line in f:
	line = line.strip()
	temp = line.split('::')
	genre = temp[2].split('|')
	for word in genre:
		if word in dic_genre:
			dic_genre[word] += 1
		else:
			dic_genre[word] = 1
	
for k, v in dic_genre.items():
	fw.write(k+" "+str(v)+"\n")

f.close()
fw.close()	
