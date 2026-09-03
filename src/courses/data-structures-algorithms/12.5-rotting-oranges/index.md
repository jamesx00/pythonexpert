---
lesson_name: Rotting Oranges
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

### Rotting Oranges

You are given a 2D grid of crates, where each cell holds `0` (empty), `1` (a fresh orange), or `2` (a rotten orange). Every minute, any fresh orange that is horizontally or vertically adjacent to a rotten orange also becomes rotten. Write a function `oranges_rotting(grid)` that returns the number of minutes that must pass until no fresh orange remains, or `-1` if some fresh orange can never rot because it is unreachable from any rotten orange.

For example, given

```
[[2, 1, 0],
 [1, 1, 0],
 [0, 1, 2]]
```

the rot spreads outward one ring at a time from each `2`, and every fresh orange ends up rotten after `2` minutes, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>oranges_rotting([[2, 1, 0], [1, 1, 0], [0, 1, 2]])</code> should return <code>2</code></li>
<li id="test-2"><code>oranges_rotting([[0, 2]])</code> should return <code>0</code></li>
<li id="test-3"><code>oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])</code> should return <code>-1</code></li>
<li id="test-4"><code>oranges_rotting([[0, 0, 0]])</code> should return <code>0</code></li>
<li id="test-5"><code>oranges_rotting([[1]])</code> should return <code>-1</code></li>
<li id="test-6"><code>oranges_rotting([[2]])</code> should return <code>0</code></li>
<li id="test-7"><code>oranges_rotting([[2, 1, 1, 1, 1]])</code> should return <code>4</code></li>
</ul>
