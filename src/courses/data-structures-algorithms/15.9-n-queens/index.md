---
lesson_name: N-Queens
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n!)
  space: O(n)
hints:
  - "Every row must hold exactly one queen. If you place them row by row, what do you need to remember to check a new queen in `O(1)`?"
  - "Use the N-Queens tip in *Tips & Gotchas* from *Backtracking Basics*: place one queen per row, and keep the used columns, `row - col` diagonals and `row + col` anti-diagonals in three sets. Skip any column whose column or diagonal is taken."
  - "Template: `def backtrack(row)`: if `row == n`, count one solution. For each `col`: if `col`, `row - col` or `row + col` is in its set, skip. Add all three, `backtrack(row + 1)`, then remove all three."
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

### N-Queens

Write a function `n_queens(n)` that takes a board size `n` and returns **the number of distinct ways** to place `n` queens on an `n x n` chessboard so that no two queens attack each other — meaning no two queens may share a row, a column, or a diagonal. Rather than returning the actual board layouts, just return how many valid arrangements exist, as an integer.

For example, on a `4 x 4` board there are exactly 2 ways to place 4 non-attacking queens, so `n_queens(4)` should return `2`. On a `1 x 1` board a single queen trivially doesn't attack itself, so `n_queens(1)` should return `1`, while a `2 x 2` or `3 x 3` board has no valid arrangement at all.

---

### Tests

<ul>
<li id="test-1"><code>n_queens(4)</code> should return <code>2</code></li>
<li id="test-2"><code>n_queens(1)</code> should return <code>1</code></li>
<li id="test-3"><code>n_queens(2)</code> should return <code>0</code></li>
<li id="test-4"><code>n_queens(3)</code> should return <code>0</code></li>
<li id="test-5"><code>n_queens(5)</code> should return <code>10</code></li>
<li id="test-6"><code>n_queens(6)</code> should return <code>4</code></li>
<li id="test-7">Performance: a 10x10 board (724 solutions), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def n_queens(n):
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count
```

**Brute force:** one queen per row and column means a placement is a permutation of the columns. Try all `n!` of them and check every pair of queens for a shared diagonal. That's `O(n! · n²)`: for `n = 10`, about 3.6 million permutations.

**Bottleneck:** a permutation is checked only when it's complete, so a clash between the first two queens is found again in every permutation that starts the same way.

**Optimal idea:** place queens row by row and check each new queen against the ones already placed. If it clashes, don't go deeper. Store the used columns and both diagonals in sets so each check is `O(1)`. All squares on one diagonal share `row - col`, and all squares on one anti-diagonal share `row + col`.

**Why it's correct:** every valid board has one queen per row, so it's a sequence of one column choice per row, and the search tries every column for every row. A branch is cut only when the new queen shares a column or diagonal with an earlier one, and such a board can never become valid. Removing the three entries after the recursive call restores the sets for the next column.

**Complexity:** `O(n!)` time as a loose bound: row `k` has at most `n - k` free columns. Pruning by diagonals makes it much smaller in practice. `O(n)` extra space for the three sets and the recursion depth.

**Common mistakes:** forgetting to remove one of the three entries after the call, which blocks squares for later branches. Mixing up the diagonals: `row - col` for one direction, `row + col` for the other. Using `abs(row - col)`, which merges two different diagonals.

</details>
