---
lesson_name: Longest Substring Without Repeating Characters
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

### Longest Substring Without Repeating Characters

Given a string `s`, write `longest_unique_substring(s)` that returns the
length of the longest contiguous run of characters in `s` that contains no
repeated character.

For example, `"xyzxyz"` has a longest run of `3` (`"xyz"`, since after that
the characters start repeating). `"aaaa"` has a longest run of `1`, because
every window bigger than one character contains a repeat. The empty string
has a longest run of `0`.

---

### Tests

<ul>
<li id="test-1"><code>longest_unique_substring("xyzxyz")</code> should return <code>3</code></li>
<li id="test-2"><code>longest_unique_substring("aaaa")</code> should return <code>1</code></li>
<li id="test-3"><code>longest_unique_substring("")</code> should return <code>0</code></li>
<li id="test-4"><code>longest_unique_substring("pwwkew")</code> should return <code>3</code></li>
<li id="test-5"><code>longest_unique_substring("dvdf")</code> should return <code>3</code></li>
<li id="test-6"><code>longest_unique_substring("abcdefg")</code> should return <code>7</code></li>
<li id="test-7"><code>longest_unique_substring("bbtablud")</code> should return <code>6</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def longest_unique_substring(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

</details>
