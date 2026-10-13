---
lesson_name: Valid Sudoku
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(1)
  space: O(1)
hints:
  - "A digit breaks the rules if it was already seen in the same row, the same column, or the same 3x3 box. How could you remember what each one has seen?"
  - "Keep one `set` per row, per column and per box: 27 sets in total (the *Seen-set* block in *Arrays & Hashing Basics*, used 27 times). The box for cell `(r, c)` is `(r // 3) * 3 + c // 3`."
  - "Template: scan every cell, skip `\".\"`, return `False` if the digit is already in its row, column or box set, otherwise add it to all three. Return `True` at the end."
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

### Valid Sudoku

Write a function `is_valid_sudoku(board)` that takes a 9x9 board represented as a list of 9 lists, each containing 9 values that are either the string digits `"1"`-`"9"` or the string `"."` for an empty cell. Return `True` if the board is a valid partially-filled Sudoku board, meaning no row, column, or 3x3 sub-box contains the same digit more than once, and `False` otherwise. Empty cells (`"."`) are ignored and do not need to satisfy any rule — you are only checking placement validity, not whether the board is solvable or complete.

For example, a board is invalid if the digit `"5"` shows up twice in the same row, even if every column and sub-box on the board is otherwise fine.

---

### Tests

<ul>
<li id="test-1">a mostly-empty board with <code>"8"</code> placed twice inside the same top-left 3x3 box should return <code>False</code></li>
<li id="test-2">a fully empty 9x9 board (every cell is <code>"."</code>) should return <code>True</code></li>
<li id="test-3">a mostly-empty board with <code>"3"</code> placed twice in the same row should return <code>False</code></li>
<li id="test-4">a mostly-empty board with <code>"7"</code> placed twice in the same column should return <code>False</code></li>
<li id="test-5">a mostly-empty board with the digits <code>"1"</code> through <code>"9"</code> placed once each along the main diagonal should return <code>True</code></li>
<li id="test-6">a mostly-empty board with the digit <code>"5"</code> placed twice, in two cells that don't share a row, column, or 3x3 box, should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            box = (r // 3) * 3 + (c // 3)
            if v in rows[r] or v in cols[c] or v in boxes[box]:
                return False
            rows[r].add(v)
            cols[c].add(v)
            boxes[box].add(v)
    return True
```

**Brute force:** for each filled cell, scan its whole row, column and box for the same digit. That's 81 cells × about 27 checks each.

**Bottleneck:** each cell rescans its row, column and box, although the same rows, columns and boxes are scanned again and again.

**Optimal idea:** one pass over the board, recording each digit in the set for its row, its column and its box. A repeat shows up as a digit that's already in one of those sets.

**Why it's correct:** a board is invalid exactly when some row, column or box contains a digit twice. The second occurrence of that digit finds the first one in the matching set, and no other situation makes a set check fail.

**Complexity:** the board is always 9×9, so both time and space are `O(1)`. For an `n×n` board, it would be `O(n²)` time and space.

**Common mistakes:** getting the box index wrong. `r // 3` picks the band of three rows and `c // 3` picks the stack of three columns, so the box is `(r // 3) * 3 + c // 3`, not `r // 3 + c // 3`, which gives two different boxes the same index.

</details>
