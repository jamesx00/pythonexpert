---
lesson_name: Partition Labels
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

### Partition Labels

You're given a lowercase string `s`. Split `s` into the smallest possible number of contiguous chunks so that no letter appears in more than one chunk — every occurrence of a given letter must fall inside the same chunk. Write a function `partition_labels(s)` that returns a list of the chunk lengths, in the order the chunks appear.

For example, `s = "abacbc"` needs to keep all of its `a`'s together and all of its `c`'s together, so no valid split point exists and the whole string becomes a single chunk of length `6`. But `s = "abcdef"` has every letter appearing exactly once, so it splits into six chunks of length `1` each.

---

### Tests

<ul>
<li id="test-1"><code>partition_labels("abacbc")</code> should return <code>[6]</code></li>
<li id="test-2"><code>partition_labels("abcabc")</code> should return <code>[6]</code></li>
<li id="test-3"><code>partition_labels("aaaa")</code> should return <code>[4]</code></li>
<li id="test-4"><code>partition_labels("abcdef")</code> should return <code>[1, 1, 1, 1, 1, 1]</code></li>
<li id="test-5"><code>partition_labels("eccbbbeee")</code> should return <code>[9]</code></li>
<li id="test-6"><code>partition_labels("aabbccddeeff")</code> should return <code>[2, 2, 2, 2, 2, 2]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result
```

</details>
