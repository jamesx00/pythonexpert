---
lesson_name: Time Based Key-Value Store
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
</ul>
