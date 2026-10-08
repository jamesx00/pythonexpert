---
lesson_name: Longest Substring Without Repeating Characters
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(k)
hints:
  - "Grow a window to the right one character at a time. When the new character is already in the window, what's the smallest change that makes the window valid again?"
  - "Use a variable-size window (the *grow right, shrink left* block in *Sliding Window Basics*). Remember the last index of each character, so when a repeat arrives, `left` can jump straight past the earlier copy."
  - "Template: for each `right, ch`, if `ch` was last seen at an index `>= left`, set `left` to that index `+ 1`. Record `seen[ch] = right` and update `best` with `right - left + 1`."
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
<li id="test-8">Performance: 100,000 characters with a longest run of 20,000, within 1 second</li>
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

Here `k` is the number of distinct characters.

**Brute force:** from every start index, extend a substring until a character repeats, using a set. That's `O(n·k)`, which is `O(n²)` when there are many distinct characters.

**Bottleneck:** after a repeat, the brute force throws the whole window away and starts again one index later, rechecking characters it already knows are unique.

**Optimal idea:** keep one window `[left, right]` with no repeats. When `s[right]` repeats a character inside the window, move `left` just past that character's last index.

**Why it's correct:** the window `[left, right]` never contains a repeat. Any longer valid substring ending at `right` would have to include the earlier copy of `s[right]`, so `right - left + 1` is the longest valid length ending at `right`. Taking the maximum over every `right` gives the answer.

**Complexity:** `O(n)` time, since each index is visited once and each update is `O(1)`. `O(k)` space for the last-seen dictionary.

**Common mistakes:** jumping `left` to `seen[ch] + 1` without checking `seen[ch] >= left`. An old copy outside the window moves `left` backwards, as in `"abba"`.

</details>
