---
lesson_name: Merge Triplets to Form Target Triplet
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

### Merge Triplets to Form Target Triplet

You're given a list of triplets `triplets`, where each triplet is `[x, y, z]`, and a `target` triplet `[a, b, c]`. Starting from a running result of `[0, 0, 0]`, you may repeatedly pick any triplet from the list and merge it in by taking the elementwise maximum (merging `[2, 5, 3]` into `[0, 0, 0]` gives `[2, 5, 3]`). Write a function `merge_triplets(triplets, target)` that returns `True` if some choice and order of merges can make the running result exactly equal `target`, and `False` otherwise.

For example, `triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]` and `target = [2, 7, 5]` can reach the target by merging only the first and last triplets, so the answer is `True`. But `triplets = [[3, 4, 5], [4, 5, 6]]` and `target = [3, 2, 5]` can never bring the middle value down to `2` once it's been merged up, so the answer is `False`.

---

### Tests

<ul>
<li id="test-1"><code>merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])</code> should return <code>True</code></li>
<li id="test-2"><code>merge_triplets([[5, 2, 3]], [5, 2, 3])</code> should return <code>True</code></li>
<li id="test-3"><code>merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])</code> should return <code>True</code></li>
<li id="test-4"><code>merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5])</code> should return <code>False</code></li>
<li id="test-5"><code>merge_triplets([[1, 1, 1]], [2, 2, 2])</code> should return <code>False</code></li>
<li id="test-6"><code>merge_triplets([[2, 2, 2], [1, 1, 1], [3, 3, 3]], [3, 3, 3])</code> should return <code>True</code></li>
</ul>
