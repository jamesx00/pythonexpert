---
lesson_name: Word Search II
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

### Word Search II

You're given a `board`, a rectangular grid of single lowercase letters (a list of lists of single-character strings), and a list of candidate `words`. Write a function `find_words(board, words)` that returns every word from `words` that can be traced out on the board.

A word can be traced starting from any cell, moving to horizontally or vertically adjacent cells one step at a time, and never reusing the same cell twice within that one word's path. The returned list may be in any order and should contain no duplicates.

For example, given the 2x2 board `[["o","a"],["e","t"]]` and candidates `["oa", "eat", "ate"]`: `"oa"` is traceable (`o` at row 0 col 0 to `a` at row 0 col 1), `"eat"` is not (there's no path from `e` through an adjacent `a`), and `"ate"` is traceable (`a` → `t` → `e`, each step moving to an adjacent cell). So `find_words` would return `["oa", "ate"]` (in either order).

A `TrieNode` class and a `build_trie(words)` helper are already provided in the starter file — `build_trie` returns the root of a trie built from `words`, where each node ending a word has its `word` attribute set to that full word (and `None` otherwise). Use this trie to prune your search as you backtrack across the board, rather than checking each word independently.

---

### Tests

<ul>
<li id="test-1">board <code>[["a","b","c"],["e","f","g"],["i","j","k"]]</code>, words <code>["abc","abfe","beg","aei","xyz"]</code> &mdash; should return <code>["abc","abfe","aei"]</code> (any order)</li>
<li id="test-2">board <code>[["a"]]</code>, words <code>["a","b"]</code> &mdash; should return <code>["a"]</code></li>
<li id="test-3">board <code>[["a","a"]]</code>, words <code>["aa","aaa"]</code> &mdash; should return <code>["aa"]</code>, since there's no third <code>a</code> cell left to extend the path</li>
<li id="test-4">board <code>[["x","y"],["y","x"]]</code>, words <code>["ab","cd"]</code> &mdash; should return <code>[]</code></li>
<li id="test-5">board <code>[["o","a"],["e","t"]]</code>, words <code>["oa","oe","eat","ate"]</code> &mdash; should return <code>["oa","oe","ate"]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_words(board, words):
    if not board or not board[0]:
        return []

    root = build_trie(words)
    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:
            return
        nxt = node.children[ch]
        if nxt.word is not None:
            found.add(nxt.word)

        board[r][c] = '#'
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return list(found)
```

</details>
