#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:recurse.hot:v1.0 (by /u/yourusername)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        if not hot_list:
            return None
        return hot_list
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))
    next_after = data.get("after")
    if next_after is None:
        return hot_list
    return recurse(subreddit, hot_list, next_after)
