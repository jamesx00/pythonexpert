---
lesson_name: Redundant Connection
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

### Redundant Connection

A tree with `n` nodes labeled `1` to `n` should have exactly `n - 1` edges. You are given a list of `n` edges `[a, b]` describing a graph that started as a valid tree and then had one extra edge added, creating exactly one cycle. Write a function `find_redundant_connection(edges)` that returns the one edge that can be removed to turn the graph back into a tree. If several edges could be removed to break the cycle, return the one that appears last in the input list.

For example, given `[[1, 2], [1, 3], [2, 3]]`, the edges `[1, 2]` and `[1, 3]` already connect all three nodes into a tree, so the extra edge `[2, 3]` is the one that creates the cycle, and the function should return `[2, 3]`.

---

### Tests

<ul>
<li id="test-1"><code>find_redundant_connection([[1, 2], [1, 3], [2, 3]])</code> should return <code>[2, 3]</code></li>
<li id="test-2"><code>find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])</code> should return <code>[1, 4]</code></li>
<li id="test-3"><code>find_redundant_connection([[1, 2], [1, 3], [1, 4], [3, 4]])</code> should return <code>[3, 4]</code></li>
<li id="test-4"><code>find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2]])</code> should return <code>[1, 3]</code></li>
<li id="test-5"><code>find_redundant_connection([[1, 2], [2, 3], [1, 3]])</code> should return <code>[1, 3]</code></li>
</ul>
