class Twitter:
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
