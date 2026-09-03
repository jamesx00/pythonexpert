---
lesson_name: Trapping Rain Water
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

### Trapping Rain Water

You're given a list of non-negative integers representing the height of a bumpy floor, one unit wide per position. After rain, water settles into the dips between higher ground on either side. Write a function that returns the total number of water units the floor can trap.

For example, with heights `[0, 1, 0, 2, 1, 0, 3, 1, 0, 2]`, water collects above the low spots between the taller bars, trapping `8` units total in this case.

---

### Tests

<ul>
<li id="test-1"><code>trap_rain_water([0, 1, 0, 2, 1, 0, 3, 1, 0, 2])</code> should return <code>8</code></li>
<li id="test-2"><code>trap_rain_water([4, 2, 3])</code> should return <code>1</code></li>
<li id="test-3"><code>trap_rain_water([1, 1, 1])</code> should return <code>0</code></li>
<li id="test-4"><code>trap_rain_water([5, 4, 1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>trap_rain_water([])</code> should return <code>0</code></li>
<li id="test-6"><code>trap_rain_water([3, 0, 0, 2, 0, 4])</code> should return <code>10</code></li>
</ul>
