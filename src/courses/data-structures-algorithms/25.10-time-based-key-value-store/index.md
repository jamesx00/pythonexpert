---
lesson_name: Time Based Key-Value Store
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log n) per get
  space: O(n)
hints:
  - "Pattern: *Binary Search*."
  - "Timestamps for each key arrive in increasing order. What does that mean for each key's list of `(timestamp, value)` entries?"
  - "Each key's list is already sorted by timestamp, so `get` is a binary search for the last entry with a timestamp `<= t` (template 2 in *Binary Search Basics*, or the `bisect` module)."
  - "Template: store `self.store[key] = [(timestamp, value), ...]`. In `get`, find `i`, the number of entries with timestamp `<= t`, and return `entries[i - 1][1]` if `i > 0`, else `\"\"`."
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

### Time Based Key-Value Store

Design a class `TimeMap` that stores multiple values for the same key, each tagged with a timestamp, and can later answer "what was this key's value at or before this moment?"

Implement two methods:

- `set(key, value, timestamp)` — records that `key` held `value` starting at `timestamp`. Calls for the same key always arrive with strictly increasing timestamps.
- `get(key, timestamp)` — returns the value that was set for `key` with the largest recorded timestamp that is `<=` the given `timestamp`. If `key` has no such recorded value (either the key was never set, or every recorded timestamp for it is larger than the one asked for), return `""`.

For example, after calling `set("temp", "72F", 1)` and `set("temp", "75F", 4)`, calling `get("temp", 4)` returns `"75F"`, `get("temp", 2)` returns `"72F"` (the closest entry at or before time `2`), and `get("temp", 0)` returns `""` since nothing was recorded that early.

---

### Tests

<ul>
<li id="test-1">after <code>set("temp", "72F", 1)</code>, <code>get("temp", 1)</code> should return <code>"72F"</code></li>
<li id="test-2">after also <code>set("temp", "75F", 4)</code>, <code>get("temp", 2)</code> should return <code>"72F"</code></li>
<li id="test-3">continuing from above, <code>get("temp", 4)</code> should return <code>"75F"</code></li>
<li id="test-4">continuing from above, <code>get("temp", 10)</code> should return <code>"75F"</code></li>
<li id="test-5">continuing from above, <code>get("temp", 0)</code> should return <code>""</code></li>
<li id="test-6"><code>get("missing", 5)</code> on a store with no calls for <code>"missing"</code> should return <code>""</code></li>
<li id="test-7">after <code>set("a", "1", 1)</code>, <code>set("a", "2", 2)</code>, <code>set("a", "3", 3)</code>, <code>get("a", 3)</code> should return <code>"3"</code>, then <code>get("a", 2)</code> should return <code>"2"</code></li>
<li id="test-8">Performance: 50,000 <code>set</code> calls on one key, then 50,000 <code>get</code> calls, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import bisect


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        entries = self.store.get(key, [])
        i = bisect.bisect_right(entries, (timestamp, chr(0x10FFFF)))
        return entries[i - 1][1] if i > 0 else ""
```

**Brute force:** store each key's entries in a list and, in `get`, scan them for the last timestamp `<= t`. That's `O(n)` per `get`.

**Bottleneck:** the entries are already in timestamp order, but the scan doesn't use it.

**Optimal idea:** binary search each key's list. `bisect_right` with `(timestamp, chr(0x10FFFF))` finds how many entries have a timestamp `<= t`, because that tuple sorts after every real entry with the same timestamp.

**Why it's correct:** the entries for a key are sorted by timestamp because `set` calls arrive in increasing order. Index `i - 1` is then the latest entry at or before `t`. If `i` is `0`, every entry is later than `t` or the key doesn't exist.

**Complexity:** `O(1)` per `set` (an append) and `O(log n)` per `get`. `O(n)` space for all entries.

**Common mistakes:** searching for `(timestamp, "")` with `bisect_right`. The empty string sorts before every value, so an entry at exactly `timestamp` counts as later and is missed. Keeping one dictionary from timestamp to value, which loses the ordering needed to find "at or before".

</details>
