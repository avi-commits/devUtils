#!/usr/bin/python

import itertools

powers = ['e','f','g','h','i']
combinat = itertools.combinations(powers ,2)
x = sorted(combinat)
print(x)

rows = []
for entry in x:
   rows.append([entry[0], entry[1]])

print(rows)

import csv

file = 'test.csv'
fields = ['Power 1', 'Power 2']

with open(file, 'w') as csvfile:
   
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(fields)

   csvwriter.writerows(rows)
