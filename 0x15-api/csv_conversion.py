#!/usr/bin/python3
import csv

# Example dictionary
my_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

# Open a new CSV file in write mode
with open('my_file.csv', mode='w') as csv_file:
    # Create a writer object
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(my_dict.keys())
    
    # Write the data rows
    for row in zip(*my_dict.values()):
        writer.writerow(row)
