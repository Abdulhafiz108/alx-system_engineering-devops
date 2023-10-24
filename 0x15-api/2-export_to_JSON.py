#!/usr/bin/python3
"""Exports to CSV"""

from requests import get
from sys import argv
import json


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    data = get(url)
    username = data.json().get('username')

    data = get(url + '/todos')
    tasks = data.json()
    with open('{}.json'.format(user_id), 'w') as file:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
            } for task in tasks]}, file)
