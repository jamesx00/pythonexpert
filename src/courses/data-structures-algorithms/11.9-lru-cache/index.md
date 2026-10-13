---
lesson_name: LRU Cache
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(1) per operation
  space: O(capacity)
hints:
  - "You need to find a key fast *and* keep keys in order of use, with moves to the front. Which structure gives `O(1)` lookup, and which gives `O(1)` reordering?"
  - "Combine a dictionary (key to node) with a doubly linked list ordered by use, with dummy `head`/`tail` nodes as in *Linked List Basics*. Python's `OrderedDict` is exactly that, with `move_to_end()` and `popitem(last=False)`."
  - "Template with `OrderedDict`: `get` returns `-1` if missing, otherwise `move_to_end(key)` and return the value. `put` does `move_to_end(key)` if the key exists, sets the value, and calls `popitem(last=False)` if the size is over `capacity`."
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

### LRU Cache

Implement a class `LRUCache` with a fixed positive `capacity` passed to its constructor. It supports two operations, both of which must run in average O(1) time:

- `get(key)` returns the value associated with `key` if it exists in the cache, or `-1` otherwise. A successful `get` also marks that key as the most recently used.
- `put(key, value)` inserts or updates the value for `key`, marking it as the most recently used. If adding the key would push the cache over its capacity, the least recently used key must be evicted first.

For example, with `capacity = 2`: `put(1, 10)`, `put(2, 20)`, `get(1)` returns `10` (and `1` is now more recently used than `2`), then `put(3, 30)` evicts key `2` since it's now the least recently used, so a following `get(2)` returns `-1`.

---

### Tests

<ul>
<li id="test-1">capacity <code>2</code>: <code>put(1, 10)</code>, <code>put(2, 20)</code>, <code>get(1)</code>, <code>put(3, 30)</code>, <code>get(2)</code>, <code>get(3)</code> should return <code>[None, None, 10, None, -1, 30]</code></li>
<li id="test-2">capacity <code>1</code>: <code>put(1, 1)</code>, <code>get(1)</code>, <code>put(2, 2)</code>, <code>get(1)</code>, <code>get(2)</code> should return <code>[None, 1, None, -1, 2]</code></li>
<li id="test-3">capacity <code>2</code>: <code>put(1, 1)</code>, <code>put(2, 2)</code>, <code>put(3, 3)</code>, <code>get(1)</code>, <code>get(3)</code> should return <code>[None, None, None, -1, 3]</code></li>
<li id="test-4">capacity <code>3</code>: <code>put(1, 1)</code>, <code>put(2, 2)</code>, <code>get(1)</code>, <code>put(3, 3)</code>, <code>put(4, 4)</code>, <code>get(2)</code>, <code>get(1)</code>, <code>get(4)</code> should return <code>[None, None, 1, None, None, -1, 1, 4]</code></li>
<li id="test-5">capacity <code>2</code>: <code>get(1)</code>, <code>put(1, 100)</code>, <code>get(1)</code> should return <code>[-1, None, 100]</code></li>
<li id="test-6">capacity <code>2</code>: <code>put(1, 1)</code>, <code>put(1, 2)</code>, <code>get(1)</code> should return <code>[None, None, 2]</code></li>
<li id="test-7">Performance: capacity 30,000, with 90,002 calls, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

**Brute force:** a dictionary for the values plus a Python list of keys in order of use. On every `get` and `put`, `order.remove(key)` and `order.append(key)`, and evict with `order.pop(0)`. `remove` and `pop(0)` are `O(capacity)`, so every operation is `O(capacity)`.

**Bottleneck:** moving a key to the "most recent" end of a Python list means searching for it and shifting everything after it.

**Optimal idea:** keep the usage order in a doubly linked list, and map each key to its node. With the node in hand, unlinking it and relinking it at the end takes a few pointer changes. `OrderedDict` implements exactly this.

**Why it's correct:** the order always runs from least to most recently used, because every successful `get` and every `put` moves the key to the most recent end. So when the cache is over capacity, the key at the other end is the least recently used one, and `popitem(last=False)` removes it.

**Complexity:** `O(1)` time for `get` and `put`: a dictionary lookup plus a constant number of pointer changes. `O(capacity)` space.

**Common mistakes:** forgetting to mark a key as used on `get`. Updating an existing key's value without moving it, so it's evicted too early. Evicting *before* inserting a key that's already in the cache, which throws out a key for no reason.

</details>
