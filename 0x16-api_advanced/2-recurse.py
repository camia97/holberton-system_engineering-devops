#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recurse it!"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if data.get('data').get('after'):
            return recurse(subreddit, hot_list)
        return hot_list
    return None
