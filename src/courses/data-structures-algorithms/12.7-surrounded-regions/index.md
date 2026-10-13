---
lesson_name: Surrounded Regions
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m * n)
hints:
  - "Instead of asking which `O`s are trapped, ask which ones are safe. Where does every safe group of `O`s have to reach?"
  - "Use *DFS: Go Deep First* from *Graphs Basics* on the grid, starting from the border: run a DFS from every `O` on the edge and mark every `O` it reaches as safe. Any `O` that isn't marked afterwards is surrounded."
  - "Template: `safe = set()`. `dfs(r, c)` returns if `(r, c)` is out of bounds, already safe, or not `\"O\"`; otherwise it adds `(r, c)` to `safe` and calls itself on the 4 neighbours. Call it on every border cell, then turn every `\"O\"` that isn't in `safe` into `\"X\"` and return `board`."
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

### Surrounded Regions

You are given a 2D board where each cell is `X` or `O`. Write a function `surrounded_regions(board)` that flips every `O` into an `X`, unless that `O` is part of a group of vertically/horizontally connected `O`s that touches the edge of the board (such a group can escape "capture" because it isn't fully surrounded). Return the mutated board.

For example, given

```
[["X", "X", "X"],
 ["X", "O", "X"],
 ["X", "X", "X"]]
```

the lone `O` in the center is completely enclosed by `X`s and never touches the border, so it gets captured and flipped, producing a board of all `X`s.

---

### Tests

<ul>
<li id="test-1"><code>surrounded_regions([["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]])</code> should return <code>[["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]</code></li>
<li id="test-2"><code>surrounded_regions([["O", "X"], ["X", "X"]])</code> should return <code>[["O", "X"], ["X", "X"]]</code></li>
<li id="test-3"><code>surrounded_regions([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])</code> should return <code>[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]</code></li>
<li id="test-4"><code>surrounded_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "X"]])</code> should return <code>[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]</code></li>
<li id="test-5"><code>surrounded_regions([["O"]])</code> should return <code>[["O"]]</code></li>
<li id="test-6"><code>surrounded_regions([["X"]])</code> should return <code>[["X"]]</code></li>
<li id="test-7"><code>surrounded_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])</code> should return <code>[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]</code></li>
<li id="test-8"><code>surrounded_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "X", "O", "X"]])</code> should return <code>[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "X", "O", "X"]]</code></li>
<li id="test-9">Performance: a 211x211 board with 100 blocks of 20x20 <code>"O"</code>s, 95 of them surrounded, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def surrounded_regions(board):
    rows, cols = len(board), len(board[0]) if board else 0
    safe = set()

    def dfs(r, c):
        if (r, c) in safe or r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return
        safe.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r, c) not in safe:
                board[r][c] = 'X'
    return board
```

Here `m` and `n` are the number of rows and columns.

**Brute force:** for every `O`, search its group to see whether it reaches the edge, and flip it if it doesn't. A group of `k` cells is searched `k` times, so big groups cost `O((m * n)²)`. Test 9 has 95 surrounded blocks of 400 cells each.

**Bottleneck:** every cell of a group repeats the same search.

**Optimal idea:** a group escapes exactly when it touches the edge. So search once from every `O` on the edge, and mark everything those searches reach as safe. Every other `O` is surrounded and flips.

**Why it's correct:** an `O` is safe exactly when a path of `O`s connects it to an `O` on the edge. The DFS from the edge follows those paths in the other direction, so it marks exactly the safe `O`s. Every unmarked `O` has no such path, so it's surrounded.

**Complexity:** `O(m * n)` time and extra space.

**Common mistakes:** flipping cells while still searching, which can cut a safe group in two. Treating diagonal `O`s as connected. Starting from the first and last rows but forgetting the first and last columns. Test 8 is a group that reaches the edge through a single `O`, so the whole group stays.

</details>
