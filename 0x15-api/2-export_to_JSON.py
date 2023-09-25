#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import requests
from sys import argv


BASE_URL = 'https://jsonplaceholder.typicode.com'


def export_progress(emp_id):
    """ Exports info about employee's progress into a JSON file """

    user = requests.get(f"{BASE_URL}/users/{emp_id}").json()
    todos = requests.get(f"{BASE_URL}/todos?userId={emp_id}").json()

    username = user.get("username")
    formatted_todos = {emp_id: [{
        "task": todo["title"],
        "completed": todo["completed"],
        "username": username
        } for todo in todos]
    }

    with open(f"{emp_id}.json", 'w', encoding='UTF8') as f:
        json.dump(formatted_todos, f)


if __name__ == '__main__':
    export_progress(argv[1])
