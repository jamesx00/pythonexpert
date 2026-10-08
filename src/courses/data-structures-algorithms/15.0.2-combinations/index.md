---
lesson_name: "Warm-up: Combinations"
code_editor: True
code_execution: True
adding_file_allowed: False
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

**Hint:** pass a `start` number into your backtracking function so each call only picks numbers **larger** than the last one. That's what stops `[2, 1]` from appearing as a duplicate of `[1, 2]`. When you record a finished combination, append a **copy** (`path[:]`).

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

`backtrack(num + 1)` moves the start forward, so numbers only ever increase along a path and every combination is generated once. Appending `path[:]` matters: `path` itself is emptied again by later `pop()` calls, so appending it directly would leave you with a list of empty lists.

An optional pruning step: if there aren't enough numbers left to fill the path (`n - num + 1 < k - len(path)`), stop the loop early.

</details>
