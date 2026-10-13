---
lesson_name: Longest Repeating Character Replacement
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "In a window, which characters would you choose to change, and how many changes does that take?"
  - "Keep the most common letter and change the rest: a window needs `window length - count of its most common letter` changes. Grow a window to the right and shrink it from the left while that number is above `k` (the *grow right, shrink left* block in *Sliding Window Basics*)."
  - "Template: count letters in the window and track `max_freq`. After adding `s[right]`, while `(right - left + 1) - max_freq > k`, remove `s[left]` and move `left`. Update `best` with the window length."
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
<li id="test-8">Performance: 100,000 characters with <code>k = 1,000</code>, within 1 second</li>
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

**Brute force:** from every start index, extend the window and keep letter counts until it needs more than `k` changes. That's `O(n²)` windows.

**Bottleneck:** after a window gets too expensive, the brute force restarts from the next index instead of reusing the counts it already has.

**Optimal idea:** one window that grows on the right and shrinks on the left. A window is valid when `length - max_freq <= k`, because the cheapest fix is to change every letter except the most common one.

**Why it's correct:** for each `right`, the window shrinks only until it's valid again, so it's the longest valid window ending at `right`, and `best` takes the maximum of these. `max_freq` is never decreased when letters leave the window. That's still correct: a stale, too-large `max_freq` only lets the window keep its size, never grow, and `best` only increases when a window with a genuinely higher frequency appears.

**Complexity:** `O(n)` time, since `left` and `right` each move at most `n` times. `O(1)` space, because there are only 26 uppercase letters.

**Common mistakes:** checking `length - max_freq >= k` instead of `> k`, which shrinks windows that are exactly allowed. Recomputing `max(counts.values())` every step is correct and still `O(26·n)`, but easy to get wrong when the counts dictionary holds zeros.

</details>
