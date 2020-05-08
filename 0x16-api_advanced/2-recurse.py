#!/usr/bin/python3
""" Program that use Reddit API and list the top ten with recursion"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    header = {'User-Agent': 'My-pc/0.1'}
    req = requests.get(url, headers=header, allow_redirects=False)

    if (req.status_code == 200):
        json = req.json()
        data = json['data']['children']
        for post in data:
            hot_list.append(post['data']['title'])
        after = json['data']['after']
        if (after is not None):
            recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    else:
        return (None)
    return (hot_list)
