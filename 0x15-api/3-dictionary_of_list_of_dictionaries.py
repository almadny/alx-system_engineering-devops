#!/usr/bin/python3
"""Script to information about an employee TODO list progress."""
import json
import requests
import sys


if __name__ == "__main__":
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    emp_list = requests.get("https://jsonplaceholder.typicode.com/users")
    # Get list of TODOS
    todo_dict = todo_list.json()
    # Get list of staff
    emp_dict = emp_list.json()

    json_dict = {}

    # Version 2
    for emp_d in emp_dict:
        emp_list = []
        emp_id = emp_d.get('id')
        emp_username = emp_d.get('username')
        for todo in todo_dict:
            emp_dic = {}
            if todo.get('userId') == emp_id:
                emp_dic["username"] = emp_username
                emp_dic["task"] = todo.get('title')
                emp_dic["completed"] = todo.get('completed')
                emp_list.append(emp_dic)
        json_dict["{}".format(emp_id)] = emp_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(json_dict, f)
