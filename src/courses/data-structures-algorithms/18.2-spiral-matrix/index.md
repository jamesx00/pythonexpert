---
lesson_name: Spiral Matrix
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

### Spiral Matrix

You're given a rectangular grid of integers, `matrix`, which doesn't have to be square. Write a function that walks the grid in spiral order, starting at the top-left cell and moving right, then down, then left, then up, shrinking the boundary each time it wraps around, and returns the values it visits as a flat list.

For example, given
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
the spiral visits `1, 2, 3` across the top, `6, 9` down the right side, `8, 7` back along the bottom, then `4` up the left side, and finally `5` in the center, giving `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

---

### Tests

<ul>
<li id="test-1"><code>spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])</code> should return <code>[1, 2, 3, 6, 9, 8, 7, 4, 5]</code></li>
<li id="test-2"><code>spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])</code> should return <code>[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]</code></li>
<li id="test-3"><code>spiral_order([[1]])</code> should return <code>[1]</code></li>
<li id="test-4"><code>spiral_order([[1, 2], [3, 4]])</code> should return <code>[1, 2, 4, 3]</code></li>
<li id="test-5"><code>spiral_order([[1], [2], [3]])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-6"><code>spiral_order([])</code> should return <code>[]</code></li>
</ul>
