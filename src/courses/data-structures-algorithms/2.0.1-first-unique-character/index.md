---
lesson_name: "Warm-up: First Unique Character"
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

### Warm-up: First Unique Character

Write a function `first_unique(s)` that returns the index of the first character in `s` that appears **exactly once**. If every character repeats (or `s` is empty), return `-1`.

For example, `first_unique("leetcode")` returns `0` because `"l"` appears once, and `first_unique("aabb")` returns `-1`.

**Hint:** make two passes. The first pass counts every character in a dictionary. The second pass finds the first index whose count is `1`. That's `O(n)` instead of calling `s.count(ch)` for every character (`O(n²)`).

---

### Tests

<ul>
<li id="test-1"><code>first_unique(&#x27;leetcode&#x27;)</code> should return <code>0</code></li>
<li id="test-2"><code>first_unique(&#x27;loveleetcode&#x27;)</code> should return <code>2</code></li>
<li id="test-3"><code>first_unique(&#x27;aabb&#x27;)</code> should return <code>-1</code></li>
<li id="test-4"><code>first_unique(&#x27;&#x27;)</code> should return <code>-1</code></li>
<li id="test-5"><code>first_unique(&#x27;z&#x27;)</code> should return <code>0</code></li>
<li id="test-6"><code>first_unique(&#x27;aabbc&#x27;)</code> should return <code>4</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
```

The first loop builds a frequency map. The second loop walks the string in its original order, so the first character with a count of `1` is the earliest unique one. Each loop is `O(n)`.

</details>
