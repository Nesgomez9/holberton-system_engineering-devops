#!/usr/bin/python3
"""Function that queries the Reddit API
and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    try:
        header = {'User-agent': 'My-computador/0.0,1'}
        url ="https://www.reddit.com/r/{}/about.json".format(subreddit)
        js = requests.get(url, headers=header, allow_redirects=False)
        subs = js.json().get('data').get('subscribers')
        return subs
    except:
        return 0
