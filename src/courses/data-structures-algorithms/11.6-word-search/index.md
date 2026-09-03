---
lesson_name: Word Search
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

### Word Search

Write a function `word_search(board, word)` that takes a 2D grid of single-character strings and a target word, and returns `True` if the word can be traced out on the grid by moving between horizontally or vertically adjacent cells, and `False` otherwise. Each cell may be used at most once while tracing a single word — you cannot revisit the same grid position twice within one path, though the same letter appearing at a different position is fair game.

For example, given the grid `[["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]]`, the word `"CARE"` can be traced starting at `C` (top-left), moving down to `A`... wait, actually tracing right to `A`, down to `R`, then right to `E`, so `word_search(board, "CARE")` should return `True`. The word `"DOT"` cannot be traced this way, since `D`, `O`, and `T` are not connected through adjacent cells, so it should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>word_search([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "CARE")</code> should return <code>True</code></li>
<li id="test-2"><code>word_search([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "DOT")</code> should return <code>False</code></li>
<li id="test-3"><code>word_search([["A", "B"], ["C", "D"]], "ABDC")</code> should return <code>True</code></li>
<li id="test-4"><code>word_search([["A", "B"], ["C", "D"]], "ABCD")</code> should return <code>False</code></li>
<li id="test-5"><code>word_search([["X"]], "X")</code> should return <code>True</code></li>
<li id="test-6"><code>word_search([["X"]], "XX")</code> should return <code>False</code></li>
<li id="test-7"><code>word_search([["A", "A", "A"], ["A", "A", "A"]], "AAAAA")</code> should return <code>True</code></li>
</ul>
