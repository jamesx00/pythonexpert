---
lesson_name: Rotting Oranges
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "Pattern: *Graphs*."
  - "All the rotten oranges spread at the same time, one step per minute. Which traversal moves outward one ring at a time, and where should it start?"
  - "Use multi-source BFS from *BFS: Go Wide First* in *Graphs Basics*: queue every rotten orange with time `0`, and count the fresh ones. Each time the BFS rots a fresh neighbour, it gets the time plus one, and the fresh count goes down."
  - "Template: queue `(r, c, 0)` for every `2` and count the `1`s as `fresh`. Pop `(r, c, t)` and set `minutes = max(minutes, t)`. For each fresh neighbour, set it to `2`, subtract `1` from `fresh`, and queue it with `t + 1`. Return `-1` if `fresh > 0`, else `minutes`."
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

### Rotting Oranges

You are given a 2D grid of crates, where each cell holds `0` (empty), `1` (a fresh orange), or `2` (a rotten orange). Every minute, any fresh orange that is horizontally or vertically adjacent to a rotten orange also becomes rotten. Write a function `oranges_rotting(grid)` that returns the number of minutes that must pass until no fresh orange remains, or `-1` if some fresh orange can never rot because it is unreachable from any rotten orange.

For example, given

```
[[2, 1, 0],
 [1, 1, 0],
 [0, 1, 2]]
```

the rot spreads outward one ring at a time from each `2`, and every fresh orange ends up rotten after `2` minutes, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>oranges_rotting([[2, 1, 0], [1, 1, 0], [0, 1, 2]])</code> should return <code>2</code></li>
<li id="test-2"><code>oranges_rotting([[0, 2]])</code> should return <code>0</code></li>
<li id="test-3"><code>oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])</code> should return <code>-1</code></li>
<li id="test-4"><code>oranges_rotting([[0, 0, 0]])</code> should return <code>0</code></li>
<li id="test-5"><code>oranges_rotting([[1]])</code> should return <code>-1</code></li>
<li id="test-6"><code>oranges_rotting([[2]])</code> should return <code>0</code></li>
<li id="test-7"><code>oranges_rotting([[2, 1, 1, 1, 1]])</code> should return <code>4</code></li>
<li id="test-8"><code>oranges_rotting([[2, 1, 1, 1, 2]])</code> should return <code>2</code></li>
<li id="test-9">Performance: a 101x100 grid where the fresh oranges form one winding path 5,150 cells long, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q:
        r, c, t = q.popleft()
        minutes = max(minutes, t)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
    return -1 if fresh > 0 else minutes
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** simulate minute by minute: scan the whole grid, rot every fresh orange next to a rotten one, and repeat until nothing changes. Each minute costs `O(m * n)`, and a long winding path of oranges takes thousands of minutes (5,149 in test 9), so the worst case is `O((m * n)²)`.

**Bottleneck:** each minute rescans the whole grid, though only the oranges at the edge of the rot can change.

**Optimal idea:** multi-source BFS. Start with every rotten orange in the queue at time `0`. Each orange the BFS rots gets the time of the orange that rotted it plus one, which is the minute it really rots. The answer is the largest time, as long as no fresh orange is left.

**Why it's correct:** the minute an orange rots is its distance, through oranges, to the nearest orange that was rotten at the start. A BFS that starts from all rotten oranges at once finds exactly that distance for every orange it reaches. Oranges it never reaches stay fresh forever, so `fresh > 0` means `-1`.

**Complexity:** `O(m * n)` time and space.

**Common mistakes:** starting the BFS from only the first rotten orange, which counts the minutes as if all the rot came from one place (test 8 rots from both ends). Returning `-1` when there are no fresh oranges at all: the answer is `0`. Adding an extra minute after the last ring, when nothing new rotted.

</details>
