---
lesson_name: Permutation in String
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "A permutation of `pattern` has the same length as `pattern`. What does that tell you about the size of the windows to check?"
  - "Slide a fixed window of `len(pattern)` over `text` (the *Fixed size `k`* block in *Sliding Window Basics*). A window matches when its letter counts equal `pattern`'s letter counts, like *Valid Anagram*."
  - "Template: count `pattern` and the first window. On each slide, add the entering letter and remove the leaving one (deleting zero counts), and return `True` as soon as the two counts are equal."
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

### Permutation in String

Given two strings `pattern` and `text`, write `contains_permutation(pattern, text)`
that returns `True` if any contiguous block of `text` is a rearrangement
(anagram) of `pattern`, and `False` otherwise.

For example, with `pattern = "abc"` and `text = "eidbacoo"`, the block
`"bac"` starting at index 3 uses exactly the letters `a`, `b`, `c` once each,
so the function should return `True`. With `pattern = "abc"` and
`text = "eidboaoo"`, no three-character block of `text` rearranges
to `"abc"`, so the function should return `False`.

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
<li id="test-8">Performance: a 1,000-letter pattern in a 100,000-letter text, within 1 second</li>
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

Here `n` is the length of `text` and `m` the length of `pattern`.

**Brute force:** for every window of length `m`, sort it and compare it with the sorted pattern. That's `O(n·m log m)`.

**Bottleneck:** neighbouring windows differ by one letter in and one letter out, but each window is rebuilt and sorted from scratch.

**Optimal idea:** keep the letter counts of the current window. Sliding one step changes two counts, and comparing two count dictionaries is `O(26)`.

**Why it's correct:** two strings are permutations of each other exactly when their letter counts are equal. The sliding counts always match the current window, and every window of length `m` is checked.

**Complexity:** `O(n)` time: `O(1)` work per slide plus an `O(26)` comparison. `O(1)` space, because the counts hold at most 26 letters each.

**Common mistakes:** comparing plain dictionaries that still hold zero counts: `{"a": 1, "b": 0}` isn't equal to `{"a": 1}`, so delete letters whose count drops to zero. (`Counter` ignores zero counts when comparing, from Python 3.10 on.) Forgetting the case where `pattern` is longer than `text`, where building the first window runs off the end of `text`.

</details>
