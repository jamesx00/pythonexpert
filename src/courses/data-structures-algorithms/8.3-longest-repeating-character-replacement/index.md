---
lesson_name: Longest Repeating Character Replacement
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

### Longest Repeating Character Replacement

You're given a string `s` made of uppercase letters and an integer `k`. You
may change up to `k` characters in `s` to any other uppercase letter you
like. Write `longest_replacement(s, k)` that returns the length of the
longest substring you can end up with where every character is the same,
after making at most `k` such changes.

For instance, with `s = "AABABBA"` and `k = 1`, changing the single `"B"` at
index 3 to `"A"` produces `"AAAABBA"`, giving a run of `4` matching
characters — the best possible with only one swap allowed. With `k = 0` no
changes are allowed at all, so the answer is just the length of the longest
run already present in `s`.

---

### Tests

<ul>
<li id="test-1"><code>longest_replacement("AABABBA", 1)</code> should return <code>4</code></li>
<li id="test-2"><code>longest_replacement("ABAB", 2)</code> should return <code>4</code></li>
<li id="test-3"><code>longest_replacement("AAAA", 0)</code> should return <code>4</code></li>
<li id="test-4"><code>longest_replacement("ABCDE", 1)</code> should return <code>2</code></li>
<li id="test-5"><code>longest_replacement("A", 0)</code> should return <code>1</code></li>
<li id="test-6"><code>longest_replacement("AABBCC", 2)</code> should return <code>4</code></li>
<li id="test-7"><code>longest_replacement("BAAAB", 2)</code> should return <code>5</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter

def longest_replacement(s, k):
    counts = Counter()
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

</details>
