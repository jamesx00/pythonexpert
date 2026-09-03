---
lesson_name: Number of Islands
section: Graphs
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

### Number of Islands

Write a function `num_islands(grid)` that takes a 2D grid of `1`s (land) and `0`s (water) and returns the number of islands. An island is a group of `1`s connected horizontally or vertically (not diagonally), surrounded by water or the edge of the grid.

For example, given

```
[[1, 1, 0],
 [1, 0, 0],
 [0, 0, 1]]
```

the top-left `1`s form one connected island, and the lone `1` in the bottom-right corner forms a second, separate island, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>num_islands([[1, 1, 0], [1, 0, 0], [0, 0, 1]])</code> should return <code>2</code></li>
<li id="test-2"><code>num_islands([[0, 0, 0], [0, 0, 0]])</code> should return <code>0</code></li>
<li id="test-3"><code>num_islands([[1, 1, 1], [1, 1, 1]])</code> should return <code>1</code></li>
<li id="test-4"><code>num_islands([[1, 0, 1, 0, 1]])</code> should return <code>3</code></li>
<li id="test-5"><code>num_islands([[1]])</code> should return <code>1</code></li>
<li id="test-6"><code>num_islands([[0]])</code> should return <code>0</code></li>
<li id="test-7"><code>num_islands([[1, 0], [0, 1], [1, 0]])</code> should return <code>3</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    visited = set()
    count = 0

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        while queue:
            row, col = queue.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                count += 1
    return count
```

</details>
