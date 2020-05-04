#!/usr/bin/python3
""" Return TODO progress """

import requests
from sys import argv
import csv

if __name__ == '__main__':
    user_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1]))

    name = user_json.json().get("name")

    tasks_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()

    with open("{}.csv".format(argv[1]), 'w') as file:
        fileWriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in range(0, len(tasks_json)):
            if tasks_json[i].get("completed") is True:
                fileWriter.writerow([str(tasks_json[i].get("userId")),
                                     str(name),
                                    str(tasks_json[i].get("completed")),
                                    str(tasks_json[i].get("title"))])
            elif tasks_json[i].get("completed") is False:
                fileWriter.writerow([str(tasks_json[i].get("userId")),
                                     str(name),
                                    str(tasks_json[i].get("completed")),
                                    str(tasks_json[i].get("title"))])
