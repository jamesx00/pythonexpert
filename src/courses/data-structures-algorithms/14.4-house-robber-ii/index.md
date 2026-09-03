---
lesson_name: House Robber II
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

### House Robber II

Write a function `rob_circular(houses)` that solves the same problem as House Robber, except this time the houses are arranged in a circle, so the first house and the last house are also considered neighbors. As before you may never rob two adjacent houses, and you must return the maximum total amount stealable.

For example, given `houses = [2, 3, 2]`, robbing house `0` and house `2` is not allowed since they are adjacent in the circle, so the best you can do is rob house `1` alone for a total of `3`.

---

### Tests

<ul>
<li id="test-1"><code>rob_circular([2, 3, 2])</code> should return <code>3</code></li>
<li id="test-2"><code>rob_circular([1, 2, 3, 1])</code> should return <code>4</code></li>
<li id="test-3"><code>rob_circular([1, 2, 3])</code> should return <code>3</code></li>
<li id="test-4"><code>rob_circular([5])</code> should return <code>5</code></li>
<li id="test-5"><code>rob_circular([5, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>rob_circular([0, 0, 0, 0])</code> should return <code>0</code></li>
<li id="test-7"><code>rob_circular([6, 7, 1, 3, 8, 2, 4])</code> should return <code>19</code></li>
</ul>
