---
lesson_name: Regular Expression Matching
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

### Regular Expression Matching

Write a function `is_match(s, p)` that returns `True` if the pattern `p` matches the entire string `s`, or `False` otherwise. The pattern supports two special symbols: `.` matches any single character, and `*` means the character immediately before it may repeat zero or more times. The match must cover the whole of `s`, not just a prefix.

For example, the pattern `"z*a*b"` matches `"zzab"` because `z*` can absorb both leading `z`s, `a*` absorbs the single `a`, and the final `b` matches literally, so `is_match("zzab", "z*a*b")` should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>is_match("zzab", "z*a*b")</code> should return <code>True</code></li>
<li id="test-2"><code>is_match("greengrass", "gre*n.*s")</code> should return <code>True</code></li>
<li id="test-3"><code>is_match("abc", "abc")</code> should return <code>True</code></li>
<li id="test-4"><code>is_match("", "a*")</code> should return <code>True</code></li>
<li id="test-5"><code>is_match("ab", ".*")</code> should return <code>True</code></li>
<li id="test-6"><code>is_match("abcd", "abc")</code> should return <code>False</code></li>
</ul>
