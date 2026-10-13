---
lesson_name: Merge Intervals
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "If the intervals were sorted by start, which interval could the next one possibly overlap?"
  - "After sorting by start, an interval can only overlap the last interval you've built so far: check `start <= last_end` (see *Merge* in *Intervals Basics*)."
  - "Template: sort by start, start the result with a copy of the first interval, then for each `[start, end]`: if `start <= result[-1][1]`, set `result[-1][1] = max(result[-1][1], end)`, else append `[start, end]`."
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

### Merge Intervals

Write a function `merge_intervals(intervals)` that takes a list of `[start, end]` intervals in no particular order and returns a new list where every pair of overlapping (or touching) intervals has been combined into one, sorted by start time.

For example, given `intervals = [[8, 10], [1, 3], [2, 6]]`, the intervals `[1, 3]` and `[2, 6]` overlap and merge into `[1, 6]`, while `[8, 10]` stays separate, so the result is `[[1, 6], [8, 10]]`.

---

### Tests

<ul>
<li id="test-1"><code>merge_intervals([[8, 10], [1, 3], [2, 6]])</code> should return <code>[[1, 6], [8, 10]]</code></li>
<li id="test-2"><code>merge_intervals([[1, 4], [4, 5]])</code> should return <code>[[1, 5]]</code></li>
<li id="test-3"><code>merge_intervals([[1, 4], [0, 4]])</code> should return <code>[[0, 4]]</code></li>
<li id="test-4"><code>merge_intervals([[1, 4], [2, 3]])</code> should return <code>[[1, 4]]</code></li>
<li id="test-5"><code>merge_intervals([[1, 2], [3, 4], [5, 6]])</code> should return <code>[[1, 2], [3, 4], [5, 6]]</code></li>
<li id="test-6"><code>merge_intervals([[5, 7]])</code> should return <code>[[5, 7]]</code></li>
<li id="test-7"><code>merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]])</code> should return <code>[[1, 10]]</code></li>
<li id="test-8">Performance: 100,000 shuffled intervals that merge in pairs into 50,000, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    result = [ordered[0][:]]
    for start, end in ordered[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result
```

**Brute force:** look for any two intervals that overlap, replace them with their union, and start over. Stop when no pair overlaps. Every pass compares pairs, so it's `O(n^2)` per merge and `O(n^3)` in the worst case.

**Bottleneck:** in an unsorted list, any interval might overlap any other, so every pair has to be compared.

**Optimal idea:** sort by start. Then sweep once, keeping the merged intervals in `result`. Each new interval either overlaps the last one in `result` (extend its end) or starts after it (append it).

**Why it's correct:** after sorting, every interval later in the list starts at or after the current one. So if the current interval doesn't reach the last merged interval, nothing earlier in `result` can reach it either, since those end even sooner. Intervals that touch (`[1, 4]` and `[4, 5]`) merge because the check is `<=`.

**Complexity:** `O(n log n)` time for the sort, then `O(n)` for the sweep. `O(n)` space for the sorted copy and the result.

**Common mistakes:** setting the end to `end` instead of `max(result[-1][1], end)`, which shrinks `[1, 10]` when `[2, 3]` comes next. Using `<` instead of `<=`, which leaves touching intervals apart. Appending the input's lists into `result` and then changing them, which changes the caller's intervals: copy them first.

</details>
