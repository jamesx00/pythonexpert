---
lesson_name: Permutations
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

### Permutations

Write a function `permute(nums)` that takes a list of distinct integers and returns every possible ordering of those integers. The result should be a list of lists, one for each permutation, and the order in which the permutations appear does not matter.

For example, given `[1, 2, 3]`, the function should return all 6 orderings: `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`, in any order.

---

### Tests

<ul>
<li id="test-1"><code>permute([1, 2, 3])</code> should return all 6 permutations of <code>[1, 2, 3]</code> (any order)</li>
<li id="test-2"><code>permute([0])</code> should return <code>[[0]]</code></li>
<li id="test-3"><code>permute([])</code> should return <code>[[]]</code></li>
<li id="test-4"><code>permute([4, 5])</code> should return <code>[[4, 5], [5, 4]]</code> (any order)</li>
<li id="test-5"><code>permute([1, -1])</code> should return <code>[[1, -1], [-1, 1]]</code> (any order)</li>
<li id="test-6"><code>permute([1, 2, 3, 4])</code> should return all 24 permutations of <code>[1, 2, 3, 4]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(list(path))
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result
```

</details>
