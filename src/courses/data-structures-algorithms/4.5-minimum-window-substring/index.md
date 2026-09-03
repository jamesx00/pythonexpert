---
lesson_name: Minimum Window Substring
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

### Minimum Window Substring

Given two strings `text` and `chars`, write `min_window(text, chars)` that
returns the shortest contiguous block of `text` that contains every
character in `chars` at least as many times as it appears there (order
doesn't matter). If no block of `text` covers all of `chars`, return an
empty string `""`. When several shortest blocks tie in length, return the
one that starts first.

For example, with `text = "ADOBECODEBANC"` and `chars = "ABC"`, the shortest
block containing at least one `"A"`, one `"B"`, and one `"C"` is `"BANC"`.
With `text = "aa"` and `chars = "aa"`, the whole string is required, so the
answer is `"aa"`.

---

### Tests

<ul>
<li id="test-1"><code>min_window("ADOBECODEBANC", "ABC")</code> should return <code>"BANC"</code></li>
<li id="test-2"><code>min_window("aa", "aa")</code> should return <code>"aa"</code></li>
<li id="test-3"><code>min_window("a", "aa")</code> should return <code>""</code></li>
<li id="test-4"><code>min_window("abc", "b")</code> should return <code>"b"</code></li>
<li id="test-5"><code>min_window("acbbaca", "aba")</code> should return <code>"baca"</code></li>
<li id="test-6"><code>min_window("xyz", "w")</code> should return <code>""</code></li>
<li id="test-7"><code>min_window("aaflslflsldkalskaaa", "aaa")</code> should return <code>"aaa"</code></li>
</ul>
