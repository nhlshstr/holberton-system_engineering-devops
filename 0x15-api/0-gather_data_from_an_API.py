#!/usr/bin/python3
""" Return TODO progress """

import requests
from sys import argv

if __name__ == '__main__':
    user_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1]))

    name = user_json.json().get("name")

    tasks_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()

    completed_tasks = []

    for i in range(0, len(tasks_json)):
        if (tasks_json[i].get("completed")) is True:
            completed_tasks.append(tasks_json[i].get("title"))

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(completed_tasks),
                                                          len(tasks_json)))

    for i in range(0, len(completed_tasks)):
        print("\t {}".format(completed_tasks[i]))
