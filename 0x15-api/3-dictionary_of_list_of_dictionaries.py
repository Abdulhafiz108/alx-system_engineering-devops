#!/usr/bin/python3
"""Exports to CSV"""

from requests import get
from sys import argv
import json


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    data = get(url)
    users = data.json()

    my_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        data = get(url + '/{}/todos'.format(user_id))
        tasks = data.json()
        my_dict[user_id] = []
        for task in tasks:
            my_dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(my_dict, file)
