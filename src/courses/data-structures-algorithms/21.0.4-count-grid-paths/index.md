---
lesson_name: "Warm-up: Count Grid Paths"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(rows · cols)
  space: O(rows · cols)
hints:
  - "Your last move into the bottom-right cell came either from the cell above or from the cell to the left. How do the path counts to those two cells add up?"
  - "Start from `count_paths` in *Recursion Basics* (*Branch into several calls*). It's correct but recomputes the same `(rows, cols)` over and over. Store each answer in a dictionary keyed by `(rows, cols)` and return the stored answer when you see the same arguments again (or decorate the function with `@functools.cache`)."
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

### Warm-up: Count Grid Paths

A robot starts in the top-left cell of a grid with `rows` rows and `cols` columns. It can only move **right** or **down**, one cell at a time. Write a function `count_paths(rows, cols)` that returns how many different paths take it to the bottom-right cell.

For example, a 2 × 3 grid has 3 paths: right-right-down, right-down-right and down-right-right. A grid with a single row or a single column has exactly 1 path.

Both `rows` and `cols` are at least `1`. The last test uses a 17 × 17 grid, where the plain recursive version makes over a billion calls, so you'll need to avoid recomputing the same sub-grid.

---

### Tests

<ul>
<li id="test-1"><code>count_paths(1, 1)</code> should return <code>1</code></li>
<li id="test-2"><code>count_paths(1, 5)</code> should return <code>1</code></li>
<li id="test-3"><code>count_paths(2, 2)</code> should return <code>2</code></li>
<li id="test-4"><code>count_paths(3, 3)</code> should return <code>6</code></li>
<li id="test-5"><code>count_paths(3, 7)</code> should return <code>28</code></li>
<li id="test-6"><code>count_paths(5, 4)</code> should return <code>35</code></li>
<li id="test-7">Performance: <code>count_paths(17, 17)</code> should return <code>601080390</code> within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_paths(rows, cols, memo=None):
    if memo is None:
        memo = {}
    if rows == 1 or cols == 1:
        return 1
    if (rows, cols) not in memo:
        memo[(rows, cols)] = count_paths(rows - 1, cols, memo) + count_paths(rows, cols - 1, memo)
    return memo[(rows, cols)]
```

**Brute force:** plain recursion, `count_paths(rows - 1, cols) + count_paths(rows, cols - 1)`. Each call branches in two, and the recursion is up to `rows + cols` levels deep, so it makes exponentially many calls: over a billion for a 17 × 17 grid.

**Bottleneck:** the same sub-grid is solved again and again. `count_paths(3, 3)` calls `(2, 3)` and `(3, 2)`, and both of those call `(2, 2)`. Lower down, the repeats multiply.

**Optimal idea:** memoization. The answer depends only on `(rows, cols)`, so store each answer the first time it's computed and look it up after that.

**Why it's correct:** every path's last move comes either from the cell above (a path through a grid with one fewer row) or from the cell to the left (one fewer column), and those two groups don't overlap. So the count is the sum of the two smaller counts. A grid with one row or one column has exactly one path. Memoization doesn't change any answer, it only skips recomputing one.

**Complexity:** there are at most `rows · cols` different argument pairs, and each is computed once with `O(1)` work, so `O(rows · cols)` time. The memo holds up to `rows · cols` entries and the stack is at most `rows + cols` deep, so `O(rows · cols)` space. (The answer is also the binomial coefficient `C(rows + cols - 2, rows - 1)`, which `math.comb` computes directly. Here the point is the recursion.)

**Common mistakes:** using `memo={}` as a default argument. It's created once and shared by every call to the function, which happens to give correct answers here but surprises you in other problems. Use `None` and create the dictionary inside, or use `@functools.cache`. Checking the memo *after* recursing, which saves nothing. A base case of only `rows == 1 and cols == 1`, which then recurses into grids with `0` rows.

</details>
