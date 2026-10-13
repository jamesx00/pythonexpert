---
lesson_name: Meeting Rooms
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "If the meetings were sorted by start time, which pairs would you actually need to compare?"
  - "After sorting by start, two meetings can only clash if they're next to each other, so compare each meeting's start with the previous meeting's end (see *The One Check to Memorise* in *Intervals Basics*)."
  - "Template: sort by start, then `return False` if `ordered[i][0] < ordered[i - 1][1]` for any `i`, else `return True`."
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

### Meeting Rooms

Write a function `can_attend_all_meetings(intervals)` that takes a list of `[start, end]` meeting time intervals and returns `True` if a single person could attend every meeting without any two overlapping, or `False` otherwise.

For example, given `intervals = [[0, 30], [5, 10], [15, 20]]`, the meeting `[0, 30]` overlaps both `[5, 10]` and `[15, 20]`, so the answer is `False`. Given `intervals = [[7, 10], [2, 4]]`, neither meeting overlaps the other, so the answer is `True`.

---

### Tests

<ul>
<li id="test-1"><code>can_attend_all_meetings([[0, 30], [5, 10], [15, 20]])</code> should return <code>False</code></li>
<li id="test-2"><code>can_attend_all_meetings([[7, 10], [2, 4]])</code> should return <code>True</code></li>
<li id="test-3"><code>can_attend_all_meetings([])</code> should return <code>True</code></li>
<li id="test-4"><code>can_attend_all_meetings([[1, 5]])</code> should return <code>True</code></li>
<li id="test-5"><code>can_attend_all_meetings([[1, 5], [5, 8]])</code> should return <code>True</code></li>
<li id="test-6"><code>can_attend_all_meetings([[1, 5], [4, 8]])</code> should return <code>False</code></li>
<li id="test-7"><code>can_attend_all_meetings([[3, 6], [9, 12], [1, 2]])</code> should return <code>True</code></li>
<li id="test-8">Performance: 100,000 shuffled meetings that don't overlap, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def can_attend_all_meetings(intervals):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True
```

**Brute force:** compare every pair of meetings and return `False` if any two overlap. That's `O(n^2)`, and when nothing overlaps it has to check every pair.

**Bottleneck:** most of those pairs are far apart in time and can't possibly clash.

**Optimal idea:** sort by start time. Then a clash, if there is one, shows up between two neighbours: a meeting that starts before the previous one ends.

**Why it's correct:** suppose meetings `a` and `c` overlap and `b` sits between them in sorted order. Then `b` starts after `a` and before `c`, which starts before `a` ends. So `b` starts before `a` ends, and the neighbours `a` and `b` overlap. A meeting that starts exactly when another ends is fine, so the check is `<`.

**Complexity:** `O(n log n)` time for the sort, `O(n)` for the scan. `O(n)` space for the sorted copy.

**Common mistakes:** using `<=`, which says `[1, 5]` and `[5, 8]` clash. Comparing neighbours without sorting first. Starting the loop at `0`, so `ordered[-1]` (the last meeting) is compared with the first one.

</details>
