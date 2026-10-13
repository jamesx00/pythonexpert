---
lesson_name: Minimum Window Substring
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(k)
hints:
  - "Once a window covers every character of `chars`, can it get shorter and still cover them?"
  - "Use a variable-size window (the *grow right, shrink left* block in *Sliding Window Basics*): grow `right` until the window covers `chars`, then shrink `left` as far as possible while it still covers them, recording the shortest window you see."
  - "Template: keep `need` counts and a `missing` total. Adding `text[right]` lowers `missing` if it was still needed. While `missing == 0`, record the window, give back `text[left]` (raising `missing` if it becomes needed again), and move `left`."
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

### Minimum Window Substring

Given two strings `text` and `chars`, write `min_window(text, chars)` that
returns the shortest contiguous block of `text` that contains every
character in `chars` at least as many times as it appears there (order
doesn't matter). If no block of `text` covers all of `chars`, return an
empty string `""`. When several shortest blocks tie in length, return the
one that starts first.

For example, with `text = "ADOBECODEBANC"` and `chars = "ABC"`, the shortest
block containing at least one `"A"`, one `"B"`, and one `"C"` is `"BANC"`.
With `text = "aa"` and `chars = "aa"`, the whole string is required, so the
answer is `"aa"`.

---

### Tests

<ul>
<li id="test-1"><code>min_window("ADOBECODEBANC", "ABC")</code> should return <code>"BANC"</code></li>
<li id="test-2"><code>min_window("aa", "aa")</code> should return <code>"aa"</code></li>
<li id="test-3"><code>min_window("a", "aa")</code> should return <code>""</code></li>
<li id="test-4"><code>min_window("abc", "b")</code> should return <code>"b"</code></li>
<li id="test-5"><code>min_window("acbbaca", "aba")</code> should return <code>"baca"</code></li>
<li id="test-6"><code>min_window("xyz", "w")</code> should return <code>""</code></li>
<li id="test-7"><code>min_window("aaflslflsldkalskaaa", "aaa")</code> should return <code>"aaa"</code></li>
<li id="test-8">Performance: 100,000 characters, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter

def min_window(text, chars):
    if not chars or not text:
        return ""
    need = Counter(chars)
    missing = len(chars)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(text):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[text[left]] += 1
            if need[text[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float("inf") else text[best[1]:best[2]]
```

Here `k` is the number of distinct characters.

**Brute force:** from every start index, extend the window until it covers `chars`, and keep the shortest. That's `O(n²)` windows, each checked against the counts.

**Bottleneck:** each start index rescans characters that the previous start already counted.

**Optimal idea:** one window. Grow `right` until everything is covered, then shrink `left` while the window still covers everything. A single `missing` counter makes "is it covered?" an `O(1)` check.

**Why it's correct:** for each `right`, the shrinking stops at the last `left` that still covers `chars`, so the shortest covering window ending at `right` is recorded. Every possible end is tried, so the overall shortest is found. A window replaces `best` only when it's strictly shorter, so ties keep the one that starts first.

**Complexity:** `O(n)` time, since `left` and `right` each move at most `n` times. `O(k)` space for the counts.

**Common mistakes:** decrementing `missing` for every character instead of only those still needed, which breaks with repeated characters such as `chars = "aa"`. Recording the window after moving `left` instead of before.

</details>
