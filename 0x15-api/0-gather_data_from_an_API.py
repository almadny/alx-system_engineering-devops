#!/usr/bin/python3
""" Script to information about an employee TODO list progress """
import requests
import sys


if __name__ == "__main__":
    # request for todo list and employees
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    emp_list = requests.get("https://jsonplaceholder.typicode.com/users")

    # convert todo response to a dictionary (deserialize todo)
    todo_dict = todo_list.json()
    emp_dict = emp_list.json()

    emp_todo = []
    emp_task_done = 0
    emp_task_undone = 0
    emp_total_task = 0
    emp_name = ''
    user_id = int(sys.argv[1])

    for todo in todo_dict:
        if todo.get('userId') == user_id:
            emp_todo.append(todo)
            emp_total_task = emp_total_task + 1

    for task in emp_todo:
        if task.get('completed'):
            emp_task_done = emp_task_done + 1
        else:
            emp_task_undone = emp_task_undone + 1

    for emp in emp_dict:
        if emp.get('id') == user_id:
            emp_name = emp.get('name')

    emp_total_task = emp_task_done + emp_task_undone

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, emp_task_done, emp_total_task))

    for i in range(len(emp_todo)):
        if emp_todo[i].get('completed'):
            print(f"\t {emp_todo[i].get('title')}")
