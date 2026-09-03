---
lesson_name: Detect Squares
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

### Detect Squares

Design a class, `DetectSquares`, that tracks points added on a 2D plane and can report how many axis-aligned squares can be formed using a given point as one corner and three previously-added points as the other three corners.

The class needs two methods: `add(point)` records a new point (given as a two-element `[x, y]` list), and points may be added more than once at the same coordinates. `count(point)` takes a query point and returns the number of ways to pick three already-added points that, together with the query point, form a square whose sides are parallel to the x and y axes (i.e. each side is either purely horizontal or purely vertical). If the same three points could combine with the query point in more than one valid way (because of duplicates), each valid combination counts separately.

For example, after adding `[3, 10]`, `[11, 2]`, and `[3, 2]`, calling `count([11, 10])` returns `1`, because those three points plus `[11, 10]` form a square with side length `8`.

---

### Tests

<ul>
<li id="test-1">adding <code>[3, 10]</code>, <code>[11, 2]</code>, <code>[3, 2]</code> then calling <code>count([11, 10])</code> should return <code>1</code></li>
<li id="test-2">continuing from test 1, calling <code>count([14, 8])</code> should return <code>0</code></li>
<li id="test-3">continuing from test 1, adding <code>[11, 10]</code> then calling <code>count([13, 6])</code> should return <code>0</code></li>
<li id="test-4">a fresh instance: adding <code>[0, 0]</code>, <code>[0, 2]</code>, <code>[2, 0]</code>, <code>[2, 2]</code> then calling <code>count([0, 0])</code> should return <code>1</code></li>
<li id="test-5">continuing from test 4, adding <code>[0, 0]</code> again then calling <code>count([0, 0])</code> should return <code>2</code></li>
<li id="test-6">a fresh instance: calling <code>count([5, 5])</code> with no points added should return <code>0</code></li>
</ul>
