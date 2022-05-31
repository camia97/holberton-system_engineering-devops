#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """How many subs?"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    else:
        return 0
