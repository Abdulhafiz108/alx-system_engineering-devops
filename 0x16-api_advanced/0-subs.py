#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.
    '''
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
       data = response.json().get('data', {})
       sub_count = data.get('subscribers', 0)
       return sub_count
    else:
        return 0
