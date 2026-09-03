---
lesson_name: House Robber
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

### House Robber

Write a function `rob(houses)` that takes a list of non-negative integers, where each value is the amount of cash stored in that house along a street. Return the maximum total amount you can steal, given that robbing two adjacent houses (indices that differ by 1) trips the alarm, so you may never pick two neighboring houses in the same night.

For example, given `houses = [2, 7, 9, 3, 1]`, the best plan is to rob house `0` (2), house `2` (9), and house `4` (1), for a total of `12`.

---

### Tests

<ul>
<li id="test-1"><code>rob([2, 7, 9, 3, 1])</code> should return <code>12</code></li>
<li id="test-2"><code>rob([1, 2, 3, 1])</code> should return <code>4</code></li>
<li id="test-3"><code>rob([2, 1, 1, 2])</code> should return <code>4</code></li>
<li id="test-4"><code>rob([5])</code> should return <code>5</code></li>
<li id="test-5"><code>rob([5, 1])</code> should return <code>5</code></li>
<li id="test-6"><code>rob([0, 0, 0])</code> should return <code>0</code></li>
<li id="test-7"><code>rob([4, 1, 2, 7, 5, 3, 1])</code> should return <code>14</code></li>
</ul>
