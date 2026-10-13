---
lesson_name: Max Area of Island
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "If you can find all the cells of one island, how do you get its area? And which islands do you need to measure?"
  - "This is *Number of Islands* with a counter. Use the component-counting tip from *Tips & Gotchas* in *Graphs Basics*: loop over every cell, and from each unvisited land cell run a traversal that marks the island and counts the cells it pops. Keep the largest count."
  - "Template: `best = 0`. For each unvisited land cell, mark it, push it on a stack and set `area = 0`. While the stack isn't empty, pop a cell, add `1` to `area`, and mark and push its unvisited land neighbours. Then `best = max(best, area)`. Return `best`."
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

### Max Area of Island

Write a function `max_area_of_island(grid)` that takes a 2D grid of `1`s (land) and `0`s (water) and returns the size of the largest island, where an island is a group of `1`s connected horizontally or vertically. If the grid has no land at all, return `0`.

For example, given

```
[[0, 1, 1],
 [0, 1, 0],
 [1, 0, 0]]
```

the three connected `1`s in the top area form an island of size `3`, while the lone `1` in the bottom-left corner forms an island of size `1`, so the largest island has area `3`.

---

### Tests

<ul>
<li id="test-1"><code>max_area_of_island([[0, 1, 1], [0, 1, 0], [1, 0, 0]])</code> should return <code>3</code></li>
<li id="test-2"><code>max_area_of_island([[0, 0], [0, 0]])</code> should return <code>0</code></li>
<li id="test-3"><code>max_area_of_island([[1, 1], [1, 1]])</code> should return <code>4</code></li>
<li id="test-4"><code>max_area_of_island([[1, 0, 1, 1, 1]])</code> should return <code>3</code></li>
<li id="test-5"><code>max_area_of_island([[1]])</code> should return <code>1</code></li>
<li id="test-6"><code>max_area_of_island([[0]])</code> should return <code>0</code></li>
<li id="test-7"><code>max_area_of_island([[1, 0], [0, 1], [1, 1]])</code> should return <code>3</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    visited = set()
    best = 0

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        area = 0
        while queue:
            row, col = queue.pop()
            area += 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                best = max(best, bfs(r, c))
    return best
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** for every land cell, run a fresh traversal of its island and record the size. An island of size `k` is traversed `k` times, so one big island costs `O((m * n)²)`.

**Bottleneck:** the same island is measured again from each of its cells.

**Optimal idea:** measure each island once. Share one `visited` set across the whole scan, and only start a traversal from land that isn't visited yet.

**Why it's correct:** each traversal starts at an unvisited land cell and pops every cell of that island exactly once, so `area` is the island's size. Every island gets exactly one traversal, so the largest `area` is the largest island. A grid with no land starts no traversal and returns `0`.

**Complexity:** `O(m * n)` time, `O(m * n)` extra space.

**Common mistakes:** counting a cell both when it's pushed and when it's popped. Starting a new `visited` set for each traversal, which brings back the brute force. Returning `-1` or `None` when there's no land: the answer is `0`.

</details>
