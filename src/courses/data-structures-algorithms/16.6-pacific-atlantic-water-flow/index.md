---
lesson_name: Pacific Atlantic Water Flow
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "Following the water downhill from every cell repeats a lot of work. What if you walked backwards instead, from each ocean inland?"
  - "Reverse the flow and use *DFS: Go Deep First* from *Graphs Basics*: start a DFS from every Pacific edge cell and only move to neighbours that are at least as high. That marks every cell whose water reaches the Pacific. Do the same from the Atlantic edge, and return the cells that are in both sets."
  - "Template: `dfs(r, c, visited, prev)` returns if `(r, c)` is out of bounds, already in `visited`, or `heights[r][c] < prev`; otherwise it adds `(r, c)` and calls itself on the 4 neighbours with `heights[r][c]`. Run it from the top row and left column into `pac`, and from the bottom row and right column into `atl`. Return the cells in `pac & atl` as lists."
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
<li id="test-7"><code>pacific_atlantic([[1, 1, 1], [1, 0, 1], [1, 1, 1]])</code> should return <code>[[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]</code> (order does not matter)</li>
<li id="test-8">Performance: a 100x100 grid where cell <code>(r, c)</code> has height <code>r + c</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def pacific_atlantic(heights):
    if not heights or not heights[0]:
        return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols
                or heights[r][c] < prev_height):
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows - 1, c, atl, heights[rows - 1][c])
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols - 1])

    return [list(x) for x in (pac & atl)]
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** from every cell, search downhill to see whether its water reaches both oceans. Each search can cover the whole grid, so that's `O((m * n)²)`. In test 8, water from cell `(r, c)` can reach every cell above and to the left of it, so most of the searches are large.

**Bottleneck:** neighbouring cells repeat almost the same search.

**Optimal idea:** turn the question around. Water flows from a cell to a neighbour that is not higher. So walking backwards from the ocean, you may step to a neighbour that is **at least as high**. One search from all the Pacific edge cells marks every cell that drains into the Pacific, and one from the Atlantic edge does the same for the Atlantic. The answer is the cells in both sets.

**Why it's correct:** water from a cell reaches the Pacific exactly when there's a path from that cell to a Pacific edge cell where each step goes to a cell that's not higher. Read backwards, that's a path from the edge cell where each step goes to a cell that's not lower, which is what the reverse DFS follows. So `pac` holds exactly the cells that drain into the Pacific, and `atl` the ones that drain into the Atlantic.

**Complexity:** `O(m * n)` time: each cell is added to each set at most once. `O(m * n)` extra space for the sets and the call stack.

**Common mistakes:** using the downhill comparison in the reverse walk: going inland, the next cell must be *higher or equal*. Forgetting that the top-right and bottom-left corners touch both oceans. On a big flat grid the recursive DFS can pass Python's recursion limit; an explicit stack avoids that.

</details>
