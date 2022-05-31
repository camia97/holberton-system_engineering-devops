#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """Top Ten"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My User Agent'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        for post in req.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
