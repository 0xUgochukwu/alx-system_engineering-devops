#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
from sys import argv


BASE_URL = 'https://jsonplaceholder.typicode.com'


def get_progress(emp_id):
    """ Prints info about employee's progress """

    user = requests.get(f"{BASE_URL}/users/{emp_id}").json()
    todos = requests.get(f"{BASE_URL}/todos?userId={emp_id}").json()

    done = len([todo for todo in todos if todo['completed']])

    print(f"Employee {user['name']} is done with tasks({done}/{len(todos)}):")

    for todo in todos:
        print(f"\t {todo['title']}")


if __name__ == '__main__':
    get_progress(argv[1])
