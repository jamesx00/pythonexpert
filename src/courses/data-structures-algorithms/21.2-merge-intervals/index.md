---
lesson_name: Merge Intervals
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

</details>
