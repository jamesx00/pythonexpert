---
lesson_name: Insert Interval
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "The list is already sorted and non-overlapping. Which intervals can't touch `new_interval` at all, and where are they in the list?"
  - "Everything that ends before `new_interval` starts comes first, unchanged. Then come the intervals that overlap it, and after those the ones that start after it ends (see the *Insert Interval* tip in *Intervals Basics*)."
  - "Template: three loops over one index `i`. Copy while `intervals[i][1] < start`. Merge while `intervals[i][0] <= end` (`start = min(...)`, `end = max(...)`), then append `[start, end]`. Copy the rest."
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

### Insert Interval

Write a function `insert_interval(intervals, new_interval)` that takes a list of non-overlapping `[start, end]` intervals already sorted by start time, plus one extra `new_interval`, and returns a new list with `new_interval` merged in. Any intervals that overlap the newly inserted one should be combined into a single interval so the result stays sorted and non-overlapping.

For example, given `intervals = [[1, 3], [6, 9]]` and `new_interval = [2, 5]`, the interval `[2, 5]` overlaps `[1, 3]` but not `[6, 9]`, so the result is `[[1, 5], [6, 9]]`.

---

### Tests

<ul>
<li id="test-1"><code>insert_interval([[1, 3], [6, 9]], [2, 5])</code> should return <code>[[1, 5], [6, 9]]</code></li>
<li id="test-2"><code>insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])</code> should return <code>[[1, 2], [3, 10], [12, 16]]</code></li>
<li id="test-3"><code>insert_interval([], [5, 7])</code> should return <code>[[5, 7]]</code></li>
<li id="test-4"><code>insert_interval([[1, 5]], [6, 8])</code> should return <code>[[1, 5], [6, 8]]</code></li>
<li id="test-5"><code>insert_interval([[1, 5]], [2, 3])</code> should return <code>[[1, 5]]</code></li>
<li id="test-6"><code>insert_interval([[3, 5]], [0, 1])</code> should return <code>[[0, 1], [3, 5]]</code></li>
<li id="test-7"><code>insert_interval([[1, 3], [4, 6], [8, 10]], [0, 12])</code> should return <code>[[0, 12]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    start, end = new_interval

    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

Here `n` is `len(intervals)`.

**Brute force:** append `new_interval`, sort the whole list by start, and run the *Merge Intervals* sweep over it. That's correct and `O(n log n)`, so it passes here too.

**Bottleneck:** the list is already sorted. Sorting it again, just to place one interval, throws that work away.

**Optimal idea:** walk the list once, in three phases. First copy every interval that ends before `new_interval` starts. Then absorb every interval that starts before `new_interval` ends, widening `[start, end]` with `min` and `max`. Append the merged interval, then copy everything left.

**Why it's correct:** the intervals are sorted and don't overlap, so their ends are sorted too. The ones with `end < start` sit at the front and can't touch the new interval. Each interval after them ends at or after `start`, so it overlaps the merged interval exactly when it starts at or before `end`. Once one starts after `end`, all the later ones do too. Touching intervals (like `[1, 5]` and `[5, 7]`) count as overlapping because both checks use `<` to skip and `<=` to merge.

**Complexity:** `O(n)` time: each interval is looked at once. `O(n)` space for the result.

**Common mistakes:** using `<=` in the first loop, which leaves an interval ending exactly at `start` unmerged. Forgetting to append `[start, end]` when nothing overlaps, or when the list is empty. Deleting merged intervals from the input with `pop`, which is `O(n)` per call and changes the caller's list.

</details>
