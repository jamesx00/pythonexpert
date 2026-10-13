---
lesson_name: Spiral Matrix
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(1)
hints:
  - "After you walk the whole top row, that row is done. What changes about the part of the grid that's left?"
  - "Keep four boundaries, `top`, `bottom`, `left` and `right`, and move one inward after walking each side. See *Spiral order with shrinking boundaries* in *Math & Geometry Basics*."
  - "Template: while `top <= bottom and left <= right`: walk the top row, `top += 1`; walk the right column, `right -= 1`; if `top <= bottom`, walk the bottom row backwards, `bottom -= 1`; if `left <= right`, walk the left column upwards, `left += 1`."
rich_test_results: true
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
<li id="test-7"><code>spiral_order([[1, 2, 3]])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-8"><code>spiral_order([[1, 2], [3, 4], [5, 6], [7, 8]])</code> should return <code>[1, 2, 4, 6, 8, 7, 5, 3]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** simulate a walker. Keep a direction and a `visited` grid, and turn right whenever the next cell is off the grid or already visited. That's also `O(m * n)` time, but it needs `O(m * n)` extra space for `visited`.

**Bottleneck:** the `visited` grid only tells you where the unvisited part ends, and four numbers can track that.

**Optimal idea:** the cells left to visit always form a rectangle. Keep its edges in `top`, `bottom`, `left` and `right`. Walk the top row, then the right column, then the bottom row backwards, then the left column upwards, and move each edge inward right after walking it.

**Why it's correct:** each side walk takes exactly the outer cells on that side of the remaining rectangle, then removes them from it. So every cell is taken once, in spiral order. The two `if` checks matter when the rectangle has shrunk to a single row or column: after the top row and right column are walked, the bottom row or left column may be the same cells again.

**Complexity:** `O(m * n)` time, each cell is appended once. `O(1)` extra space, not counting the output list.

**Common mistakes:** dropping the `top <= bottom` and `left <= right` checks, which visits the middle row twice in `[[1, 2, 3]]` (test 7) or a middle column twice in a tall grid (test 8). Crashing on `[]` by reading `matrix[0]` before checking that the grid has rows.

</details>
