---
lesson_name: Islands and Treasure (Walls and Gates)
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

### Islands and Treasure (Walls and Gates)

You are given a 2D grid representing an island where each cell is one of three things: `0` marks a chest of treasure, `-1` marks an impassable rock, and `2147483647` (a stand-in for infinity) marks open ground with no treasure yet. Write a function `islands_and_treasure(grid)` that replaces every open-ground cell with the number of steps to the nearest treasure chest, moving only up/down/left/right through open ground. Cells that can never reach a chest keep the infinity value. Return the mutated grid.

For example, given

```
[[2147483647, -1, 0],
 [2147483647, 2147483647, 2147483647],
 [0, -1, 2147483647]]
```

the cell at row 0, col 0 is 2 steps from the nearest chest, so after processing it becomes `2`, and every reachable open cell is similarly replaced with its shortest distance to a chest.

---

### Tests

<ul>
<li id="test-1"><code>islands_and_treasure([[2147483647, -1, 0], [2147483647, 2147483647, 2147483647], [0, -1, 2147483647]])</code> should return <code>[[2, -1, 0], [1, 2, 1], [0, -1, 2]]</code></li>
<li id="test-2"><code>islands_and_treasure([[0]])</code> should return <code>[[0]]</code></li>
<li id="test-3"><code>islands_and_treasure([[-1]])</code> should return <code>[[-1]]</code></li>
<li id="test-4"><code>islands_and_treasure([[2147483647]])</code> should return <code>[[2147483647]]</code></li>
<li id="test-5"><code>islands_and_treasure([[0, 2147483647, 2147483647]])</code> should return <code>[[0, 1, 2]]</code></li>
<li id="test-6"><code>islands_and_treasure([[0, -1, 2147483647]])</code> should return <code>[[0, -1, 2147483647]]</code></li>
</ul>
