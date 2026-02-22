#!/usr/bin/python3
"""Module to recursively count keywords in Reddit hot article titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Parse titles of hot articles and print sorted keyword counts."""
    if not counts:
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:count.words:v1.0 (by /u/yourusername)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    children = data.get("children", [])
    for post in children:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1
    next_after = data.get("after")
    if next_after is None:
        sorted_counts = sorted(
            counts.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, next_after)
