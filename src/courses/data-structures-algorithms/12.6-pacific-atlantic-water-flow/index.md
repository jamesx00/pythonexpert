---
lesson_name: Pacific Atlantic Water Flow
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

### Pacific Atlantic Water Flow

You are given a grid of elevations, where the Pacific Ocean touches the top row and left column of the grid, and the Atlantic Ocean touches the bottom row and right column. Water at a cell can flow to a horizontally or vertically adjacent cell only if that neighbor's elevation is less than or equal to the current cell's elevation. Write a function `pacific_atlantic(heights)` that returns a list of `[row, col]` coordinates from which water can reach both oceans. The order of the returned coordinates does not matter.

For example, given

```
[[1, 2, 2],
 [3, 2, 3],
 [2, 4, 5]]
```

the cell at row 2, col 2 has the highest elevation in its neighborhood and can drain toward both the bottom-right (Atlantic) and, by flowing through decreasing or equal elevations, toward the top-left (Pacific), so `[2, 2]` is one of the coordinates in the returned list.

---

### Tests

<ul>
<li id="test-1"><code>pacific_atlantic([[1, 2, 2], [3, 2, 3], [2, 4, 5]])</code> should return <code>[[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]</code> (order does not matter)</li>
<li id="test-2"><code>pacific_atlantic([[1]])</code> should return <code>[[0, 0]]</code></li>
<li id="test-3"><code>pacific_atlantic([[3, 3], [3, 3]])</code> should return <code>[[0, 0], [0, 1], [1, 0], [1, 1]]</code> (order does not matter)</li>
<li id="test-4"><code>pacific_atlantic([[1, 2, 3]])</code> should return <code>[[0, 0], [0, 1], [0, 2]]</code> (order does not matter)</li>
<li id="test-5"><code>pacific_atlantic([[3], [2], [1]])</code> should return <code>[[0, 0], [1, 0], [2, 0]]</code> (order does not matter)</li>
<li id="test-6"><code>pacific_atlantic([])</code> should return <code>[]</code></li>
</ul>
