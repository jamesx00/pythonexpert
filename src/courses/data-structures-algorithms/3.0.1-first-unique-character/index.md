---
lesson_name: "Warm-up: First Unique Character"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "To know a character is unique, you need its count over the *whole* string. Can you get every count before deciding?"
  - "Make two passes. The first builds a frequency dictionary (the *Counting* block in *Arrays & Hashing Basics*). The second walks the string in order and stops at the first character whose count is `1`."
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

### Warm-up: First Unique Character

Write a function `first_unique(s)` that returns the index of the first character in `s` that appears **exactly once**. If every character repeats (or `s` is empty), return `-1`.

For example, `first_unique("leetcode")` returns `0` because `"l"` appears once, and `first_unique("aabb")` returns `-1`.

---

### Tests

<ul>
<li id="test-1"><code>first_unique(&#x27;leetcode&#x27;)</code> should return <code>0</code></li>
<li id="test-2"><code>first_unique(&#x27;loveleetcode&#x27;)</code> should return <code>2</code></li>
<li id="test-3"><code>first_unique(&#x27;aabb&#x27;)</code> should return <code>-1</code></li>
<li id="test-4"><code>first_unique(&#x27;&#x27;)</code> should return <code>-1</code></li>
<li id="test-5"><code>first_unique(&#x27;z&#x27;)</code> should return <code>0</code></li>
<li id="test-6"><code>first_unique(&#x27;aabbc&#x27;)</code> should return <code>4</code></li>
<li id="test-7">Performance: a 200,001-character string whose only unique character is the last one, within 1 second</li>
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

**Brute force:** for each index, call `s.count(ch)` and return the first index whose count is `1`. `s.count` scans the whole string, so this is `O(n²)`.

**Bottleneck:** every character's count is recomputed from scratch, even though the counts never change.

**Optimal idea:** count every character once in a dictionary, then walk the string in its original order and return the first index whose count is `1`.

**Why it's correct:** after the first pass, `counts[ch]` is exactly how often `ch` appears. The second pass visits indices in order, so the first match is the earliest unique character.

**Complexity:** `O(n)` time for two linear passes. `O(1)` extra space, because the dictionary holds at most one entry per distinct character, and the alphabet is fixed.

**Common mistakes:** returning the character instead of its index. Calling `s.index(ch)` to find the position is another hidden `O(n)` scan, so use `enumerate`.

</details>
