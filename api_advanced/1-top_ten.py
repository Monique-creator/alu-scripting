#!/usr/bin/python3
"""Module to query Reddit API for top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:top.ten:v1.0 (by /u/yourusername)"
    }
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
