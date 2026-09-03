---
lesson_name: Permutation in String
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

### Permutation in String

Given two strings `pattern` and `text`, write `contains_permutation(pattern, text)`
that returns `True` if any contiguous block of `text` is a rearrangement
(anagram) of `pattern`, and `False` otherwise.

For example, with `pattern = "abc"` and `text = "eidbacoo"`, the block
`"bac"` starting at index 3 uses exactly the letters `a`, `b`, `c` once each,
so the function should return `True`. With `pattern = "abc"` and
`text = "eidboaoo"`, no five-character... rather no three-character block of
`text` rearranges to `"abc"`, so the function should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>contains_permutation("abc", "eidbacoo")</code> should return <code>True</code></li>
<li id="test-2"><code>contains_permutation("abc", "eidboaoo")</code> should return <code>False</code></li>
<li id="test-3"><code>contains_permutation("ab", "eidbaaooo")</code> should return <code>True</code></li>
<li id="test-4"><code>contains_permutation("adc", "dcda")</code> should return <code>True</code></li>
<li id="test-5"><code>contains_permutation("xyz", "xy")</code> should return <code>False</code></li>
<li id="test-6"><code>contains_permutation("a", "a")</code> should return <code>True</code></li>
<li id="test-7"><code>contains_permutation("hello", "ooolleoooleh")</code> should return <code>False</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter

def contains_permutation(pattern, text):
    need = Counter(pattern)
    have = Counter()
    L = len(pattern)
    if L > len(text):
        return False
    for i in range(L):
        have[text[i]] += 1
    if have == need:
        return True
    for i in range(L, len(text)):
        have[text[i]] += 1
        have[text[i - L]] -= 1
        if have[text[i - L]] == 0:
            del have[text[i - L]]
        if have == need:
            return True
    return False
```

</details>
