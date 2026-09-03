import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

class RefTwitter:
    def __init__(self):
        self.tweets = []  # list of (time, user_id, tweet_id)
        self.time = 0
        self.following = {}  # user_id -> set of followee_ids

    def post_tweet(self, user_id, tweet_id):
        self.tweets.append((self.time, user_id, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id):
        watching = self.following.get(user_id, set()) | {user_id}
        feed = [t for t in self.tweets if t[1] in watching]
        feed.sort(key=lambda t: t[0], reverse=True)
        return [t[2] for t in feed[:10]]

    def follow(self, user_id, followee_id):
        self.following.setdefault(user_id, set()).add(followee_id)

    def unfollow(self, user_id, followee_id):
        self.following.setdefault(user_id, set()).discard(followee_id)

def run(cls, ops):
    obj = cls()
    output = []
    for op, args in ops:
        method = getattr(obj, op)
        result = method(*args)
        output.append(result if op == 'get_news_feed' else None)
    return output

def test_func(ops):
    return run(RefTwitter, ops)

def run_main(ops):
    return run(main.Twitter, ops)

inputs = [
    ([('post_tweet', (1, 5)), ('follow', (1, 2)), ('post_tweet', (2, 6)), ('get_news_feed', (1,))],),
    ([('post_tweet', (1, 5)), ('post_tweet', (2, 6)), ('get_news_feed', (1,))],),
    ([('post_tweet', (1, 1)), ('follow', (1, 2)), ('post_tweet', (2, 2)), ('unfollow', (1, 2)), ('get_news_feed', (1,))],),
    ([('post_tweet', (1, 1)), ('post_tweet', (1, 2)), ('post_tweet', (1, 3)), ('post_tweet', (1, 4)), ('get_news_feed', (1,))],),
    ([('follow', (1, 2)), ('post_tweet', (2, 9)), ('post_tweet', (1, 10)), ('get_news_feed', (1,))],),
    ([('post_tweet', (5, 1)), ('post_tweet', (5, 2)), ('post_tweet', (5, 3)), ('post_tweet', (5, 4)), ('post_tweet', (5, 5)),
      ('post_tweet', (5, 6)), ('post_tweet', (5, 7)), ('post_tweet', (5, 8)), ('post_tweet', (5, 9)), ('post_tweet', (5, 10)),
      ('post_tweet', (5, 11)), ('post_tweet', (5, 12)), ('get_news_feed', (5,))],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_main(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
