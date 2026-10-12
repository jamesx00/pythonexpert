---
lesson_name: "Warm-up: Combinations"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(C(n, k) · k)
  space: O(k)
hints:
  - "`[1, 2]` and `[2, 1]` are the same combination. How can you make sure you only ever build it in one order?"
  - "Use *The Template* from *Backtracking Basics* with a `start` argument: loop `num` from `start` to `n`, append it, recurse with `backtrack(num + 1)`, then pop. When `len(path) == k`, record a copy, `path[:]`."
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

### Warm-up: Combinations

Write a function `combine(n, k)` that returns every way to choose `k` distinct numbers from `1` to `n`. Each combination should be a list in ascending order, and the combinations themselves should be in ascending (lexicographic) order.

For example, `combine(4, 2)` returns `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]`.

---

### Tests

<ul>
<li id="test-1"><code>combine(4, 2)</code> should return <code>[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]</code></li>
<li id="test-2"><code>combine(1, 1)</code> should return <code>[[1]]</code></li>
<li id="test-3"><code>combine(3, 3)</code> should return <code>[[1, 2, 3]]</code></li>
<li id="test-4"><code>combine(5, 1)</code> should return <code>[[1], [2], [3], [4], [5]]</code></li>
<li id="test-5"><code>combine(5, 3)</code> should return <code>[[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]</code></li>
<li id="test-6"><code>combine(3, 0)</code> should return <code>[[]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def combine(n, k):
    result = []
    path = []

    def backtrack(start):
        if len(path) == k:
            result.append(path[:])
            return
        for num in range(start, n + 1):
            path.append(num)
            backtrack(num + 1)
            path.pop()

    backtrack(1)
    return result
```

**Brute force:** generate all `2ⁿ` subsets of `1..n` and keep the ones of size `k`. It works, but for `combine(20, 2)` it builds about a million subsets to find 190 answers.

**Bottleneck:** most subsets have the wrong size, and building them is wasted work.

**Optimal idea:** build each combination in ascending order. After picking `num`, the next pick must come from `num + 1` to `n`. Stop as soon as the path has `k` numbers.

**Why it's correct:** every combination has exactly one ascending order, and the `start` argument only allows ascending paths, so each combination is built exactly once. Trying smaller numbers first at every position gives lexicographic order.

**Complexity:** `O(C(n, k) · k)` time for the `C(n, k)` results, each copied in `O(k)`. `O(k)` extra space for `path` and the recursion, not counting the output.

**Common mistakes:** appending `path` instead of `path[:]`, so every result is the same list, emptied by the time you return. Recursing with `backtrack(start + 1)` instead of `backtrack(num + 1)`, which allows numbers to repeat and go backwards.

</details>
