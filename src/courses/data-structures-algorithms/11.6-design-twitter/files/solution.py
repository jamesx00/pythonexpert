import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # user_id -> [(time, tweet_id), ...]
        self.following = defaultdict(set)  # user_id -> followee_ids

    def post_tweet(self, user_id, tweet_id):
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id):
        heap = []  # newest unread tweet of each user: (-time, tweet_id, user, index)
        for uid in self.following[user_id] | {user_id}:
            tweets = self.tweets[uid]
            if tweets:
                time, tweet_id = tweets[-1]
                heap.append((-time, tweet_id, uid, len(tweets) - 1))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            _, tweet_id, uid, i = heapq.heappop(heap)
            feed.append(tweet_id)
            if i > 0:
                time, older_id = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-time, older_id, uid, i - 1))
        return feed

    def follow(self, user_id, followee_id):
        self.following[user_id].add(followee_id)

    def unfollow(self, user_id, followee_id):
        self.following[user_id].discard(followee_id)
