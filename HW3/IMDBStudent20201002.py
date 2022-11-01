#!/usr/bin/python3
import sys

file_input = sys.argv[1]
file_output = sys.argv[2]

f = open(file_input, "rt")
f_list = f.readlines()
for line in f_list:
	movie_list = line.split("::")
	genre = movie_list[2]
f.close()

genre_dic = dict()

for g in genre:
	genre_list = g.split("|")
	for g2 in genre_list:
		if g2 not in genre_dic:
			genre_dic[g2] = 1
		else:
			genre_dic[g2] += 1
f = open(file_output, "wt")
for key, value in genre.items():
	f.write(key, value)
f.close()
