#!/usr/bin/python

import itertools
import random

powers = ['e','f','g','h','i']
weakness = ['h','i','j','k']

combinat = itertools.combinations(powers ,2)
x = sorted(combinat)
print(x)

rows = []
 
for entry in x:
   for element in weakness:
      rows.append([entry[0], entry[1], element])

print(len(powers))
print(len(weakness))
print(len(rows))

import csv

file = 'test.csv'
fields = ['Power 1', 'Power 2']

with open(file, 'w') as csvfile:
   
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(fields)

   csvwriter.writerows(rows)
