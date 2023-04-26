#!/usr/bin/python3
import csv

my_list = [('apple', 1), ('banana', 2), ('orange', 3), ('grape', 4)]
filename = 'my_list.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in my_list:
        writer.writerow(row)
