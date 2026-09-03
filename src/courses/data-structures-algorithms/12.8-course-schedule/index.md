---
lesson_name: Course Schedule
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

### Course Schedule

You must take `num_courses` courses, numbered `0` to `num_courses - 1`. You are given a list of prerequisite pairs `[course, prereq]`, meaning `course` cannot be taken until `prereq` is completed. Write a function `can_finish(num_courses, prerequisites)` that returns `True` if it is possible to take every course, and `False` if the prerequisites form a cycle that makes it impossible.

For example, with `num_courses = 2` and `prerequisites = [[1, 0]]`, course `1` requires course `0` first, which has no prerequisites of its own, so every course can be completed and the function should return `True`. If instead `prerequisites = [[1, 0], [0, 1]]`, the two courses each require the other, so nothing can ever be scheduled first, and the function should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>can_finish(2, [[1, 0]])</code> should return <code>True</code></li>
<li id="test-2"><code>can_finish(2, [[1, 0], [0, 1]])</code> should return <code>False</code></li>
<li id="test-3"><code>can_finish(4, [[1, 0], [2, 1], [3, 2]])</code> should return <code>True</code></li>
<li id="test-4"><code>can_finish(3, [[0, 1], [1, 2], [2, 0]])</code> should return <code>False</code></li>
<li id="test-5"><code>can_finish(1, [])</code> should return <code>True</code></li>
<li id="test-6"><code>can_finish(5, [[1, 0], [2, 0], [3, 1], [3, 2]])</code> should return <code>True</code></li>
<li id="test-7"><code>can_finish(2, [])</code> should return <code>True</code></li>
</ul>
