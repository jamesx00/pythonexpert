---
lesson_name: Combination Sum II
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

### Combination Sum II

Write a function `combination_sum2(candidates, target)` that takes a list of positive integers (which may contain duplicate values) and a target value, and returns every unique combination of numbers from `candidates` that adds up exactly to `target`. Unlike a plain combination-sum search, each element of `candidates` may be used **at most once per combination** — but because the list can contain duplicate values, the same value may still appear more than once in a combination if it was listed more than once in `candidates`. No two combinations in the result should contain the same multiset of numbers, and the order of the combinations and the order of numbers within each combination do not matter.

For example, with `candidates = [2, 5, 2, 1, 2]` and `target = 5`, the valid combinations are `[1, 2, 2]` and `[5]` — note that `[2, 2, 1]` is the same combination as `[1, 2, 2]` and must not be listed twice.

---

### Tests

<ul>
<li id="test-1"><code>combination_sum2([2, 5, 2, 1, 2], 5)</code> should return <code>[[1, 2, 2], [5]]</code> (any order)</li>
<li id="test-2"><code>combination_sum2([2], 1)</code> should return <code>[]</code></li>
<li id="test-3"><code>combination_sum2([1, 1, 1], 2)</code> should return <code>[[1, 1]]</code></li>
<li id="test-4"><code>combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)</code> should return <code>[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]</code> (any order)</li>
<li id="test-5"><code>combination_sum2([3, 3, 3], 9)</code> should return <code>[[3, 3, 3]]</code></li>
<li id="test-6"><code>combination_sum2([4, 8], 20)</code> should return <code>[]</code></li>
</ul>
