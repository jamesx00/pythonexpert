---
lesson_name: LRU Cache
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

</details>
