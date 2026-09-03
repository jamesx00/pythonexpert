---
lesson_name: Design Twitter
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Design Twitter

Design a simplified social feed class named `Twitter` that supports posting, following, and reading a news feed. Implement these methods:

- `post_tweet(user_id, tweet_id)` — records that `user_id` posted `tweet_id`.
- `get_news_feed(user_id)` — returns a list of at most the 10 most recent tweet IDs, ordered most-recent-first, from `user_id` and everyone they follow (a user always sees their own posts, whether or not they follow themselves).
- `follow(user_id, followee_id)` — makes `user_id` follow `followee_id`.
- `unfollow(user_id, followee_id)` — makes `user_id` stop following `followee_id`.

Assume `post_tweet` calls happen in increasing chronological order, so a later `post_tweet` call is always more recent than an earlier one.

For example: user `1` posts tweet `5`, then follows user `2`, and user `2` posts tweet `6`. Now `get_news_feed(1)` should return `[6, 5]`, with user `2`'s tweet first since it is more recent.

---

### Tests

<ul>
<li id="test-1">user 1 posts tweet 5, user 1 follows user 2, user 2 posts tweet 6 &mdash; <code>get_news_feed(1)</code> should return <code>[6, 5]</code></li>
<li id="test-2">user 1 posts tweet 5, user 2 posts tweet 6 &mdash; <code>get_news_feed(1)</code> should return <code>[5]</code></li>
<li id="test-3">user 1 posts tweet 1, user 1 follows user 2, user 2 posts tweet 2, user 1 unfollows user 2 &mdash; <code>get_news_feed(1)</code> should return <code>[1]</code></li>
<li id="test-4">user 1 posts tweets 1, 2, 3, 4 in order &mdash; <code>get_news_feed(1)</code> should return <code>[4, 3, 2, 1]</code></li>
<li id="test-5">user 1 follows user 2, user 2 posts tweet 9, user 1 posts tweet 10 &mdash; <code>get_news_feed(1)</code> should return <code>[10, 9]</code></li>
<li id="test-6">user 5 posts tweets 1 through 12 in order &mdash; <code>get_news_feed(5)</code> should return the 10 most recent tweet ids, most-recent-first</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
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
```

</details>
