---
lesson_name: Design Twitter
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(f + 10 log f) per feed, f = followees
  space: O(tweets + follows)
hints:
  - "Each user's own tweets are already in time order. How would you get the 10 newest tweets out of several lists that are each sorted?"
  - "This is *merge k sorted lists*: put the newest tweet of each followed user (and the user) in a max-heap keyed by time, with tuples as in *Tuples for priorities* in *Heap / Priority Queue Basics*. Pop the newest, then push the next older tweet from the same user."
  - "Template: store `self.tweets[user] = [(time, tweet_id), ...]`. In `get_news_feed`, push `(-time, tweet_id, user, index)` for each user's last tweet. Pop up to 10 times; after each pop, push `index - 1` from the same user if `index > 0`."
rich_test_results: true
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
<li id="test-6">user 5 posts tweets 1 through 12 in order &mdash; <code>get_news_feed(5)</code> should return <code>[12, 11, 10, 9, 8, 7, 6, 5, 4, 3]</code></li>
<li id="test-7">Performance: 50,000 tweets from 10 followed users, then 2,000 <code>get_news_feed</code> calls, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
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
```

Here `f` is the number of users someone follows and `t` the total number of tweets.

**Brute force:** keep one list of every tweet ever posted. On each `get_news_feed`, filter the tweets by author, sort them by time, and take 10. Every call reads all `t` tweets, so it's `O(t log t)` per call.

**Bottleneck:** a feed only shows 10 tweets, but every call scans the whole history of every user.

**Optimal idea:** keep each user's tweets in their own list, which is already in time order. The feed is then the first 10 items of a merge of `f + 1` sorted lists, newest first. A heap holding the newest unread tweet of each list gives the next tweet in `O(log f)`, as in *Merge K Sorted Lists*.

**Why it's correct:** the heap always holds the newest tweet not yet taken from each user, so its top is the newest remaining tweet in the feed. Pushing the next older tweet of the same user keeps that true. Ten pops give the ten newest. The global `time` counter makes every key unique, so ties never fall through to compare other fields.

**Complexity:** `get_news_feed` is `O(f + 10 log f)`: building the heap is `O(f)` and each of the 10 pops and pushes is `O(log f)`. `post_tweet`, `follow` and `unfollow` are `O(1)`. `O(t + follows)` space.

**Common mistakes:** forgetting that users see their own tweets even without following themselves. Raising on `unfollow` of someone not followed (use `discard`, not `remove`). Using the tweet ID as the time, which breaks when IDs aren't posted in increasing order.

</details>
