---
lesson_name: Partition Labels
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "The first chunk contains `s[0]`. How far must it reach at the very least?"
  - "Record the last index of every letter, as in *Record last positions* in *Greedy Basics*. A chunk must reach the last index of every letter in it. As soon as the scan gets to that point, you can cut."
  - "Template: `last = {c: i for i, c in enumerate(s)}`. Scan with `start` and `end`: `end = max(end, last[c])`, and when `i == end`, append `end - start + 1` and set `start = i + 1`."
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

### Partition Labels

You're given a lowercase string `s`. Split `s` into the largest possible number of contiguous chunks so that no letter appears in more than one chunk — every occurrence of a given letter must fall inside the same chunk. Write a function `partition_labels(s)` that returns a list of the chunk lengths, in the order the chunks appear.

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
<li id="test-7"><code>partition_labels("ababcbacadefegdehijhklij")</code> should return <code>[9, 7, 8]</code></li>
<li id="test-8">Performance: a string of 520,000 letters, within 1 second</li>
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

**Brute force:** for each position, find how far the current chunk must reach with `s.rindex(c)`, or test every cut point by comparing the letters on each side. Both rescan the string for every position, so they're `O(n^2)`.

**Bottleneck:** looking up a letter's last index again and again by scanning the string.

**Optimal idea:** build `last`, the last index of each letter, in one pass. Then scan again, keeping `end`, the farthest last index of any letter in the current chunk. When `i` reaches `end`, every letter in the chunk is finished, so cut there.

**Why it's correct:** a chunk that contains a letter must reach that letter's last index, otherwise the letter shows up in a later chunk too. So the current chunk can't end before `end`. When `i == end`, no letter in `s[start..i]` appears later, so cutting here is valid. Cutting at the earliest valid point is always best: the rest of the string doesn't depend on where earlier chunks ended, and ending a chunk sooner leaves more room for later cuts. So you get the most chunks.

**Complexity:** `O(n)` time, two passes. `O(1)` extra space, since `last` holds at most 26 letters (the output list aside).

**Common mistakes:** cutting when `i == last[c]` for the current letter only, instead of tracking the max over the whole chunk (`"abab"` would cut after the second `a`). Returning the chunks themselves instead of their lengths.

</details>
