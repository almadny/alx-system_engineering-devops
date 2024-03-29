#!/usr/bin/python3
"""Script to information about an employee TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    emp_list = requests.get("https://jsonplaceholder.typicode.com/users")

    todo_dict = todo_list.json()
    emp_dict = emp_list.json()

    emp_todo = []
    emp_name = ''
    user_id = int(sys.argv[1])
    csv_filename = "{}.{}".format(int(sys.argv[1]), "csv")
    emp_username = ''
    list_to_export = []

    for todo in todo_dict:
        if todo.get('userId') == user_id:
            emp_todo.append(todo)

    for emp in emp_dict:
        if emp.get('id') == user_id:
            emp_username = emp.get('username')

    for todo in emp_todo:
        row = "{}, {}, {}, {}".format(
               str(user_id), emp_username,
               todo.get('completed'), todo.get('title')
               )
        list_to_export.append(row)

    with open(csv_filename, 'w') as filename:
        writer = csv.writer(filename, quoting=csv.QUOTE_ALL)
        for row in list_to_export:
            sub_string = row.split(', ')
            writer.writerow(sub_string)
