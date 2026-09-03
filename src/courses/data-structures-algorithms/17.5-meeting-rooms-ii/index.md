---
lesson_name: Meeting Rooms II
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

### Meeting Rooms II

Write a function `min_meeting_rooms(intervals)` that takes a list of `[start, end]` meeting time intervals and returns the minimum number of rooms required so that every meeting can happen without two meetings sharing a room at the same time.

For example, given `intervals = [[0, 30], [5, 10], [15, 20]]`, the meeting `[0, 30]` is running the whole time, and `[5, 10]` and `[15, 20]` each need their own room while it's happening, so `2` rooms are required.

---

### Tests

<ul>
<li id="test-1"><code>min_meeting_rooms([[0, 30], [5, 10], [15, 20]])</code> should return <code>2</code></li>
<li id="test-2"><code>min_meeting_rooms([[7, 10], [2, 4]])</code> should return <code>1</code></li>
<li id="test-3"><code>min_meeting_rooms([])</code> should return <code>0</code></li>
<li id="test-4"><code>min_meeting_rooms([[1, 5]])</code> should return <code>1</code></li>
<li id="test-5"><code>min_meeting_rooms([[1, 10], [2, 6], [3, 8], [4, 7]])</code> should return <code>4</code></li>
<li id="test-6"><code>min_meeting_rooms([[1, 5], [5, 8], [2, 4]])</code> should return <code>2</code></li>
<li id="test-7"><code>min_meeting_rooms([[1, 4], [2, 5], [7, 9], [8, 10]])</code> should return <code>2</code></li>
</ul>
