---
lesson_name: Distinct Subsequences
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

### Distinct Subsequences

Given two strings `s` and `t`, write a function `num_distinct(s, t)` that returns the number of distinct ways `t` can be formed by deleting zero or more characters from `s` (keeping the remaining characters in their original order). Deletions at different positions that happen to remove the same characters still count as separate ways.

For example, with `s = "xcaxcxaxxc"` and `t = "xc"`, you can pick any `x` that comes before any later `c`; counting every such `(x, c)` pair gives `num_distinct("xcaxcxaxxc", "xc")` a return value of `8`.

---

### Tests

<ul>
<li id="test-1"><code>num_distinct("xcaxcxaxxc", "xc")</code> should return <code>8</code></li>
<li id="test-2"><code>num_distinct("mississippi", "mis")</code> should return <code>6</code></li>
<li id="test-3"><code>num_distinct("abc", "abc")</code> should return <code>1</code></li>
<li id="test-4"><code>num_distinct("abc", "abcd")</code> should return <code>0</code></li>
<li id="test-5"><code>num_distinct("aaaa", "aa")</code> should return <code>6</code></li>
<li id="test-6"><code>num_distinct("", "a")</code> should return <code>0</code></li>
</ul>
