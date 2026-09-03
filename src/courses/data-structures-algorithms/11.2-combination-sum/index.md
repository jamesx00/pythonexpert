---
lesson_name: Combination Sum
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

### Combination Sum

Write a function `combination_sum(candidates, target)` that takes a list of distinct positive integers and a target value, and returns every unique combination of numbers from `candidates` that adds up exactly to `target`. A number may be reused as many times as needed within a single combination, but the same multiset of numbers must not appear twice in the result. Both the order of the combinations and the order of numbers within each combination are unimportant.

For example, with `candidates = [2, 3, 5]` and `target = 8`, valid combinations include `[2, 2, 2, 2]`, `[2, 3, 3]`, and `[3, 5]`, so the function should return exactly those three combinations (in any order).

---

### Tests

<ul>
<li id="test-1"><code>combination_sum([2, 3, 5], 8)</code> should return <code>[[2, 2, 2, 2], [2, 3, 3], [3, 5]]</code> (any order)</li>
<li id="test-2"><code>combination_sum([2], 1)</code> should return <code>[]</code></li>
<li id="test-3"><code>combination_sum([1], 3)</code> should return <code>[[1, 1, 1]]</code></li>
<li id="test-4"><code>combination_sum([3, 4, 6], 12)</code> should return <code>[[3, 3, 3, 3], [3, 3, 6], [4, 4, 4], [6, 6]]</code> (any order)</li>
<li id="test-5"><code>combination_sum([7, 11], 5)</code> should return <code>[]</code></li>
<li id="test-6"><code>combination_sum([2, 4], 8)</code> should return <code>[[2, 2, 2, 2], [2, 2, 4], [4, 4]]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def combination_sum(candidates, target):
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result
```

</details>
