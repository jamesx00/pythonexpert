---
lesson_name: Meeting Rooms
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

</details>
