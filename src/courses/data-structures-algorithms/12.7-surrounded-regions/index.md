---
lesson_name: Surrounded Regions
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

### Surrounded Regions

You are given a 2D board where each cell is `X` or `O`. Write a function `surrounded_regions(board)` that flips every `O` into an `X`, unless that `O` is part of a group of vertically/horizontally connected `O`s that touches the edge of the board (such a group can escape "capture" because it isn't fully surrounded). Return the mutated board.

For example, given

```
[["X", "X", "X"],
 ["X", "O", "X"],
 ["X", "X", "X"]]
```

the lone `O` in the center is completely enclosed by `X`s and never touches the border, so it gets captured and flipped, producing a board of all `X`s.

---

### Tests

<ul>
<li id="test-1"><code>surrounded_regions([["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]])</code> should return <code>[["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]</code></li>
<li id="test-2"><code>surrounded_regions([["O", "X"], ["X", "X"]])</code> should return <code>[["O", "X"], ["X", "X"]]</code></li>
<li id="test-3"><code>surrounded_regions([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])</code> should return <code>[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]</code></li>
<li id="test-4"><code>surrounded_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "X"]])</code> should return <code>[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]</code></li>
<li id="test-5"><code>surrounded_regions([["O"]])</code> should return <code>[["O"]]</code></li>
<li id="test-6"><code>surrounded_regions([["X"]])</code> should return <code>[["X"]]</code></li>
</ul>
