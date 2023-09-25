#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests, csv
from sys import argv


BASE_URL = 'https://jsonplaceholder.typicode.com'


def export_progress(emp_id):
    """ Exports info about employee's progress into a CSV file """

    user = requests.get(f"{BASE_URL}/users/{emp_id}").json()
    todos = requests.get(f"{BASE_URL}/todos?userId={emp_id}").json()

    with open(f"{emp_id}.csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        for todo in todos:
            row = []
            row.append(str(emp_id))
            row.append(user["name"])
            row.append(str(todo["completed"]))
            row.append(todo["title"])

            writer.writerow(row)


if __name__ == '__main__':
    export_progress(argv[1])
