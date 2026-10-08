---
lesson_name: Backtracking Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Backtracking
---

## Why This Pattern Matters &#x1F4A1;

Backtracking builds candidate solutions one choice at a time. When a path can't lead to a valid answer, it **undoes the last choice** and tries the next one. It's a depth-first search over a tree of decisions. It's exponential by nature, but it's the standard way to **generate all** subsets, permutations, combinations, or placements.

## Spotting It &#x1F50D;

- "Return **all** possible ___" (subsets, permutations, combinations, partitions).
- Constraint puzzles: N-Queens, Sudoku, word search in a grid.
- Small input sizes (n ≤ ~15–20) are a strong hint that exponential is expected.

## The Template &#x1F9F1;

```python
def backtrack_template(candidates):
    result = []
    path = []

    def backtrack(start):
        if is_complete(path):              # 1. record a solution
            result.append(path[:])         #    COPY the path
            return
        for i in range(start, len(candidates)):
            if not is_valid(candidates[i]):
                continue                   # 2. prune
            path.append(candidates[i])     # 3. choose
            backtrack(i + 1)               # 4. explore
            path.pop()                     # 5. un-choose

    backtrack(0)
    return result
```

**Choose → explore → un-choose.** Every `append` needs a matching `pop`.

### How the variants differ

| Problem | Recurse with | Why |
| --- | --- | --- |
| Subsets / combinations | `backtrack(i + 1)` | each element used once, order doesn't matter |
| Combination Sum (reuse allowed) | `backtrack(i)` | same element can be picked again |
| Permutations | loop from `0`, skip used | order matters |
| Subsets II (duplicates in input) | sort + skip `nums[i] == nums[i-1]` when `i > start` | avoid duplicate results |

### Include / exclude form

For subsets, you can also make a binary choice at each index:

```python
def subsets(nums):
    result, path = [], []
    def dfs(i):
        if i == len(nums):
            result.append(path[:])
            return
        path.append(nums[i]); dfs(i + 1); path.pop()   # include
        dfs(i + 1)                                     # exclude
    dfs(0)
    return result
```

## Tips & Gotchas &#x1F4CC;

- **Append a copy (`path[:]`).** Appending `path` itself stores a reference that later gets emptied, so your results become `[[], [], []]`.
- **Prune early.** If the input is sorted and the running sum already exceeds the target, `break` out of the loop. Every later candidate is larger.
- **Duplicate handling** needs a sorted input and `if i > start and nums[i] == nums[i - 1]: continue`.
- **Grid backtracking:** mark a cell visited (e.g., set it to `"#"`), recurse into the 4 neighbours, then restore the original value.
- **Track constraints in sets** for O(1) checks. In N-Queens, use `cols`, `diag = r - c`, and `anti_diag = r + c`.
- Complexity is roughly *(number of results) × (cost to build each)*: `O(2ⁿ · n)` for subsets, `O(n! · n)` for permutations.
