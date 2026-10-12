---
lesson_name: Word Search
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(r · c · 3ᴸ)
  space: O(L)
hints:
  - "Starting from a cell that matches `word[0]`, which neighbours could hold `word[1]`? What should stop you from stepping back onto a cell you've used?"
  - "This is grid backtracking from the *Tips & Gotchas* in *Backtracking Basics*: from each cell, run a DFS that matches one letter per step. Mark the cell as used before recursing into its 4 neighbours and unmark it after, and return `False` the moment a letter doesn't match."
  - "Template: `def backtrack(r, c, i)`: if `i == len(word)` return `True`. If `(r, c)` is off the board, already used, or `board[r][c] != word[i]`, return `False`. Mark it, try the 4 neighbours with `i + 1`, unmark it, return whether any worked. Call it from every cell."
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

### Word Search

Write a function `word_search(board, word)` that takes a 2D grid of single-character strings and a target word, and returns `True` if the word can be traced out on the grid by moving between horizontally or vertically adjacent cells, and `False` otherwise. Each cell may be used at most once while tracing a single word — you cannot revisit the same grid position twice within one path, though the same letter appearing at a different position is fair game.

For example, given the grid `[["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]]`, the word `"CARE"` can be traced starting at `C` (top-left), moving right to `A`, down to `R`, then right to `E`, so `word_search(board, "CARE")` should return `True`. The word `"DOT"` can't be traced: `D` and `O` are next to each other on the bottom row, but `T` is in the top-right corner, not next to `O`. So `word_search(board, "DOT")` should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>word_search([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "CARE")</code> should return <code>True</code></li>
<li id="test-2"><code>word_search([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "DOT")</code> should return <code>False</code></li>
<li id="test-3"><code>word_search([["A", "B"], ["C", "D"]], "ABDC")</code> should return <code>True</code></li>
<li id="test-4"><code>word_search([["A", "B"], ["C", "D"]], "ABCD")</code> should return <code>False</code></li>
<li id="test-5"><code>word_search([["X"]], "X")</code> should return <code>True</code></li>
<li id="test-6"><code>word_search([["X"]], "XX")</code> should return <code>False</code></li>
<li id="test-7"><code>word_search([["A", "A", "A"], ["A", "A", "A"]], "AAAAA")</code> should return <code>True</code></li>
<li id="test-8">Performance: a 30x30 board and a 14-letter word that isn't on it, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i, visited):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if (r, c) in visited or board[r][c] != word[i]:
            return False
        visited.add((r, c))
        found = (
            backtrack(r + 1, c, i + 1, visited)
            or backtrack(r - 1, c, i + 1, visited)
            or backtrack(r, c + 1, i + 1, visited)
            or backtrack(r, c - 1, i + 1, visited)
        )
        visited.remove((r, c))
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0, set()):
                return True
    return False
```

Here `r` and `c` are the board's dimensions and `L` the length of the word.

**Brute force:** from every cell, walk every path of `L` cells that doesn't reuse a cell, and compare the letters only at the end. That's up to `r · c · 3ᴸ⁻¹` paths, and almost all of them go wrong at the first or second letter.

**Bottleneck:** paths keep growing long after they stopped matching the word.

**Optimal idea:** match one letter per step and stop a path as soon as a letter is wrong. Keep the cells on the current path in `visited` so the path never reuses a cell, and remove each cell again when backtracking so other paths can use it.

**Why it's correct:** any valid tracing is a path of adjacent, unused cells matching `word[0]`, `word[1]`, and so on. The DFS starts at every cell and tries all 4 neighbours at each step, so it reaches every such path. It only cuts a path when it can't be extended into a match: off the board, a reused cell, or a wrong letter.

**Complexity:** `O(r · c · 3ᴸ)` time in the worst case, such as a board of all `"A"` and a word of `"A"`s ending in `"B"`: each step has at most 3 new directions, since one leads back. On most boards the letter check cuts paths almost at once. `O(L)` extra space for `visited` and the recursion depth.

**Common mistakes:** forgetting to remove the cell from `visited` after the recursive calls, so a failed path blocks cells for later paths. Checking the bounds after reading `board[r][c]`, which raises `IndexError` (or wraps around with negative indexes). Sharing one `visited` set across start cells without cleaning it up.

</details>
