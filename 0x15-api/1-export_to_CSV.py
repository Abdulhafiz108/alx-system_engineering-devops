#!/usr/bin/python3
"""Exports to CSV"""

from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    data = get(url)
    user_name = data.json().get('username')

    data = get(url + '/todos')
    tasks = data.json()
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(user_id, user_name, task.get('completed'),
                        task.get('title')))
