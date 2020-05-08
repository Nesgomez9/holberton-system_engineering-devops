#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    header = {'User-agent': 'My-pc/0.1'}
    js = requests.get(url, headers=header, allow_redirects=False)
    if js.status_code != 200:
        print(None)
        return
    data = js.json()['data']['children']
    if len(data) == 0:
        print(None)
        return
    for post in data[:10]:
        print(post['data']['title'])
