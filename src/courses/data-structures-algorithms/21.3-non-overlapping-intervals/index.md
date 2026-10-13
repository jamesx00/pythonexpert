---
lesson_name: Non-overlapping Intervals
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "Turn it around: what's the largest number of intervals you can keep? When two intervals clash, which one is safer to keep?"
  - "Keep the one that ends first: it leaves the most room for the rest. Sort by **end**, not by start (see *Tips & Gotchas* in *Intervals Basics*)."
  - "Template: sort by end, keep `prev_end` of the last kept interval. For each `[start, end]`: if `start < prev_end`, count a removal; else set `prev_end = end`."
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

### Non-overlapping Intervals

Write a function `erase_overlap_intervals(intervals)` that takes a list of `[start, end]` intervals and returns the minimum number of intervals you must remove so that none of the remaining intervals overlap each other. Intervals that only touch at an endpoint (like `[1, 2]` and `[2, 3]`) are not considered overlapping.

For example, given `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`, removing `[1, 3]` leaves `[1, 2], [2, 3], [3, 4]`, which don't overlap, so the answer is `1`.

---

### Tests

<ul>
<li id="test-1"><code>erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])</code> should return <code>1</code></li>
<li id="test-2"><code>erase_overlap_intervals([[1, 2], [1, 2], [1, 2]])</code> should return <code>2</code></li>
<li id="test-3"><code>erase_overlap_intervals([[1, 2], [2, 3]])</code> should return <code>0</code></li>
<li id="test-4"><code>erase_overlap_intervals([])</code> should return <code>0</code></li>
<li id="test-5"><code>erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]])</code> should return <code>2</code></li>
<li id="test-6"><code>erase_overlap_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]])</code> should return <code>2</code></li>
<li id="test-7"><code>erase_overlap_intervals([[-5, -2], [-3, 1], [2, 5]])</code> should return <code>1</code></li>
<li id="test-8">Performance: 100,000 shuffled intervals <code>[i, i + 2]</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    ordered = sorted(intervals, key=lambda iv: iv[1])
    removed = 0
    prev_end = ordered[0][1]
    for start, end in ordered[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end
    return removed
```

**Brute force:** try every subset of intervals and keep the largest one with no overlaps. That's `O(2^n)`. A better brute force sorts by start and uses dynamic programming: `best[i]` is the most intervals you can keep ending with interval `i`, found by checking every `j < i`. That's `O(n^2)`.

**Bottleneck:** the dynamic programming compares every pair. But you never need more than one choice per clash.

**Optimal idea:** the answer is `n` minus the most intervals you can keep. To keep the most, sort by end and sweep. Keep an interval if it starts at or after the end of the last one kept. Otherwise remove it.

**Why it's correct:** take any best set of kept intervals. Its first interval can be swapped for the interval that ends earliest overall: that one ends no later, so it clashes with nothing the first one didn't. Repeat the argument for the rest. So picking the earliest end each time keeps as many intervals as any other choice. Touching intervals don't overlap here, so the check is `start < prev_end`.

**Complexity:** `O(n log n)` time for the sort, `O(n)` for the sweep. `O(n)` space for the sorted copy.

**Common mistakes:** sorting by start and always keeping the first interval, which keeps `[1, 100]` and throws away everything inside it. Using `<=`, which counts `[1, 2]` and `[2, 3]` as a clash. Not handling an empty list.

</details>
