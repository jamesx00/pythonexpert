---
lesson_name: "Warm-up: Hash Map"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(1) average per operation
  space: O(n)
hints:
  - "Every operation starts the same way: which bucket would this key be in? Once you're in that bucket, how do you tell whether the key is already there?"
  - "Follow *Hash Map* in *Build-It-Yourself Data Structures Basics*. `put`, `get` and `remove` each scan `self._buckets[self._bucket_index(key)]` for a pair whose key `==` the key. After `put` adds a **new** key, if `self._size > 0.75 * len(self._buckets)`, build twice as many empty buckets and re-insert every pair, recomputing each bucket index."
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

### Warm-up: Hash Map

Python's `dict` is a **hash map**. Build one that handles collisions with **separate chaining**: `self._buckets` is a list of buckets, each bucket is a list of `[key, value]` pairs, and a key always lives in bucket `self._bucket_index(key)`, which is `hash(key) % len(self._buckets)`.

Implement:

- `put(key, value)`: if the key is already in its bucket, update its value. Otherwise add a new `[key, value]` pair and increase `self._size`. Then, if `self._size > 0.75 * len(self._buckets)`, **resize**: double the number of buckets and move every pair into its bucket in the new list.
- `get(key)`: return the key's value, or raise `KeyError` if it isn't there.
- `remove(key)`: delete the key's pair and decrease `self._size`, or raise `KeyError` if it isn't there.

Don't use a `dict` or `set` inside the class. A new map has 8 buckets, so the 7th key triggers the first resize (7 > 0.75 × 8). Small integers hash to themselves, which makes collisions easy to test: `1`, `9` and `17` all land in bucket `1` of 8.

---

### Tests

<ul>
<li id="test-1">put <code>&#x27;a&#x27;</code> → 1 and <code>&#x27;b&#x27;</code> → 2: <code>get</code> should return <code>1</code> and <code>2</code></li>
<li id="test-2">putting <code>&#x27;a&#x27;</code> twice should update its value and keep <code>len()</code> at <code>1</code></li>
<li id="test-3">keys <code>1</code>, <code>9</code> and <code>17</code> collide in bucket 1 of 8: <code>get(9)</code> should return its value and bucket 1 should hold <code>3</code> pairs</li>
<li id="test-4">after <code>remove(9)</code> from the colliding keys, <code>1</code> and <code>17</code> should still be found and <code>len()</code> should be <code>2</code></li>
<li id="test-5"><code>get</code> and <code>remove</code> of a missing key should raise <code>KeyError</code></li>
<li id="test-6">tuple keys work: <code>put((1, 2), &#x27;x&#x27;)</code>, then <code>get((1, 2))</code> should return <code>&#x27;x&#x27;</code></li>
<li id="test-7"><code>put([1, 2], &#x27;x&#x27;)</code> should raise <code>TypeError</code>, because a list can't be hashed</li>
<li id="test-8"><code>bucket_count()</code> after each of 7 puts should be <code>8</code> six times, then <code>16</code></li>
<li id="test-9">after resizing to 16 buckets, keys <code>1, 9, 17, 25, 33, 41, 49</code> should be re-hashed: <code>4</code> pairs in bucket 1, <code>3</code> in bucket 9, and every key still found</li>
<li id="test-10">Performance: 20,000 puts followed by 20,000 gets, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class HashMap:
    def __init__(self):
        self._buckets = [[] for _ in range(8)]
        self._size = 0

    def __len__(self):
        return self._size

    def bucket_count(self):
        return len(self._buckets)

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):
        bucket = self._buckets[self._bucket_index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self._size += 1
        if self._size > 0.75 * len(self._buckets):
            self._resize(2 * len(self._buckets))

    def get(self, key):
        for k, v in self._buckets[self._bucket_index(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        bucket = self._buckets[self._bucket_index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def _resize(self, new_count):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_count)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._buckets[self._bucket_index(key)].append([key, value])
```

**Brute force:** a single list of `[key, value]` pairs, scanned from the start on every operation. Every `get` and `put` is `O(n)`. Keeping 8 buckets forever is the same thing with a smaller constant: with 20,000 keys each bucket holds 2,500 pairs.

**Bottleneck:** scanning entries that can't possibly be the key you want.

**Optimal idea:** use the hash to jump straight to one bucket, and keep the buckets short by resizing. Doubling the bucket count whenever there are more than 0.75 entries per bucket keeps the average chain length below 1.

**Why it's correct:** a key is always stored in bucket `hash(key) % len(self._buckets)`. `get`, `put` and `remove` compute the same index, so they look in the only place the key can be. Resizing changes the modulus, which changes most keys' bucket, so every pair has to be re-inserted with the new index (not copied to the same position). Keys must be **hashable** and must not change while stored: a key whose hash changed would be looked for in the wrong bucket. That's why `hash([1, 2])` raises `TypeError` while tuples work.

**Complexity:** with a good hash, keys spread evenly, so a bucket holds `O(1)` pairs on average and every operation is `O(1)` on average. A resize is `O(n)`, but like the dynamic array, doubling makes it `O(1)` amortized. In the worst case, when every key lands in the same bucket, operations are `O(n)`. `O(n)` space.

**Common mistakes:** appending a duplicate pair instead of updating the existing one, which makes `len()` wrong. Resizing by copying the buckets as they are, so keys end up in the wrong bucket for the new modulus. Increasing `_size` when a `put` only updates a value. Removing items from a bucket while looping over it with `for pair in bucket`.

</details>
