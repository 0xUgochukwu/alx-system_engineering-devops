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


def export_progress():
    """ Exports info about all employees progress into a JSON file """

    users = requests.get(f"{BASE_URL}/users/").json()
    todos = requests.get(f"{BASE_URL}/todos/").json()

    formatted_todos = {}

    for user in users:
        username, u_id = user.get("username"), user.get("id")
        formatted_todos[u_id] = [{
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
            } for todo in [todo for todo in todos if todo["userId"] == u_id]]

    with open("todo_all_employees.json", 'w', encoding='UTF8') as f:
        json.dump(formatted_todos, f)


if __name__ == '__main__':
    export_progress()
