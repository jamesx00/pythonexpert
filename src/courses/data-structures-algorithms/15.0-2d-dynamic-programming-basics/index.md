---
lesson_name: 2-D Dynamic Programming Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: 2-D Dynamic Programming
---

## Why This Pattern Matters &#x1F4A1;

Some problems need **two** numbers to describe a subproblem: a position in a grid `(r, c)`, or a position in each of two strings `(i, j)`. The DP recipe is the same as in 1-D (state, recurrence, base cases, order). The only difference is that the table is now 2-D.

## Spotting It &#x1F50D;

- **Grids:** count paths, minimum path sum, longest path.
- **Two strings:** longest common subsequence, edit distance, interleaving, regex matching.
- **One array + a second dimension** like a remaining budget/target (*Coin Change II*, *Target Sum*) or a state flag (*holding a stock or not*).
- **Intervals** `dp[l][r]` over a subarray (*Burst Balloons*).

## Core Building Blocks &#x1F9F1;

### Grid paths

```python
def unique_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]      # first row/col: only 1 way
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]   # from above + from left
    return dp[-1][-1]
```

### Two strings: the `(n+1) × (m+1)` table

`dp[i][j]` describes the prefixes `a[:i]` and `b[:j]`. Row 0 and column 0 stand for the empty string.

```python
def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1           # use both chars
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # drop one
    return dp[-1][-1]
```

Note the `i - 1` / `j - 1` when indexing the strings. The table is shifted by one.

### Top-down works too

```python
from functools import cache

@cache
def edit(i, j):         # cost to turn a[i:] into b[j:]
    if i == len(a): return len(b) - j
    if j == len(b): return len(a) - i
    if a[i] == b[j]: return edit(i + 1, j + 1)
    return 1 + min(edit(i + 1, j), edit(i, j + 1), edit(i + 1, j + 1))
```

## Tips & Gotchas &#x1F4CC;

- **Never build a 2-D list with `[[0] * m] * n`.** All rows are the same list object. Use a comprehension: `[[0] * m for _ in range(n)]`.
- **Draw the table** for a tiny example and fill a few cells by hand. You'll see which neighbours each cell depends on.
- **Loop order follows dependencies.** If `dp[i][j]` needs `dp[i+1][...]`, loop `i` backwards.
- **Row compression:** if a row only depends on the previous row, keep two 1-D arrays (or one, carefully).
- **Counting combinations vs permutations** (*Coin Change II*): looping coins on the outside counts each combination once. Looping amounts on the outside counts orderings.
- **Grid DFS + memo** (*Longest Increasing Path in a Matrix*) needs no visited set when moves must strictly increase, since cycles are impossible.
- Complexity is usually `O(n × m)` time. Space is `O(n × m)`, or `O(m)` with row compression.
