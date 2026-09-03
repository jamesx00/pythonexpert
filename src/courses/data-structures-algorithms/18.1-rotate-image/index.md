---
lesson_name: Rotate Image
code_editor: True
code_execution: True
adding_file_allowed: False
section: Math & Geometry
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

### Rotate Image

You're given a square grid of integers, `matrix`, representing an image. Write a function that rotates the image 90 degrees clockwise and returns the rotated grid. The rotation must be done in place, overwriting `matrix` itself rather than building a brand new grid, and your function should return that same mutated `matrix` object.

For example, given
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
the top row `1, 2, 3` becomes the rightmost column read top to bottom, producing
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

### Tests

<ul>
<li id="test-1"><code>rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])</code> should return <code>[[7, 4, 1], [8, 5, 2], [9, 6, 3]]</code></li>
<li id="test-2"><code>rotate([[1, 2], [3, 4]])</code> should return <code>[[3, 1], [4, 2]]</code></li>
<li id="test-3"><code>rotate([[5]])</code> should return <code>[[5]]</code></li>
<li id="test-4"><code>rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])</code> should return <code>[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]</code></li>
<li id="test-5"><code>rotate([[1, -2], [-3, 4]])</code> should return <code>[[-3, 1], [4, -2]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
```

</details>
