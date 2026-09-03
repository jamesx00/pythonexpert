---
lesson_name: Interleaving String
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

### Interleaving String

Given three strings `s1`, `s2`, and `s3`, write a function `is_interleave(s1, s2, s3)` that returns `True` if `s3` can be formed by interleaving the characters of `s1` and `s2` while preserving each string's own internal character order, and `False` otherwise. `s3` must use every character of `s1` and `s2` exactly once and be the same length as `s1` and `s2` combined.

For example, `s1 = "abc"` and `s2 = "def"` can interleave into `s3 = "adbcef"` (take `a` from `s1`, `d` from `s2`, `b` from `s1`, `c` from `s1`, `e` from `s2`, `f` from `s2`), so `is_interleave("abc", "def", "adbcef")` should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>is_interleave("abc", "def", "adbcef")</code> should return <code>True</code></li>
<li id="test-2"><code>is_interleave("abc", "def", "abdecf")</code> should return <code>True</code></li>
<li id="test-3"><code>is_interleave("", "", "")</code> should return <code>True</code></li>
<li id="test-4"><code>is_interleave("abc", "", "abc")</code> should return <code>True</code></li>
<li id="test-5"><code>is_interleave("aabcc", "dbbca", "aadbbbaccc")</code> should return <code>False</code></li>
<li id="test-6"><code>is_interleave("ab", "bc", "babc")</code> should return <code>True</code></li>
</ul>
