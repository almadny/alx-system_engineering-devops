#!/usr/bin/python3
"""Script to information about an employee TODO list progress."""
import json
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
    json_filename = "{}.{}".format(int(sys.argv[1]), "json")
    emp_username = ''
    list_to_export = []
    json_dict = {}

    for todo in todo_dict:
        if todo.get('userId') == user_id:
            emp_todo.append(todo)

    for emp in emp_dict:
        if emp.get('id') == user_id:
            emp_username = emp.get('username')

    for i in range(len(emp_todo)):
        dict_to_export = {}
        for todo in emp_todo:
            dict_to_export["task"] = todo.get('title')
            dict_to_export["completed"] = todo.get('completed')
            dict_to_export["username"] = emp_username
        print(dict_to_export)
        list_to_export.append(dict_to_export)
        json_dict["{}".format(user_id)] = list_to_export
        print(json_dict)

    with open(json_filename, "w") as f:
        json.dump(json_dict, f)
