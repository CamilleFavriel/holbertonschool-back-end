#!/usr/bin/python3
""" def """
import requests
import sys


""" def """
employee_id = sys.argv[1]

"""Get employee information"""
response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = response.json()
employee_name = employee_data['name']

"""Get todo list"""
response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
todos = response.json()

"""Count completed tasks"""
completed_tasks = []
for todo in todos:
    if todo['completed=true']:
        completed_tasks.append(todo)
number_of_done_tasks = len(completed_tasks)
total_number_of_tasks = len(todos)

print(f"Employee {employee_name} is done with {number_of_done_tasks}/{total_number_of_tasks} tasks:")

for todo in completed_tasks:
    print("\t", todo['title'])
