---
lesson_name: Word Search II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(rows * cols * 3^L) for words of length up to L
  space: O(total letters in words)
hints:
  - "Searching the board once per word repeats the same work for words that start the same way. How could one search over the board check every word at once?"
  - "Use the *Grid + trie* tip from *Tries Basics*: walk the trie *while* you DFS the board. Stop a path as soon as the next letter isn't a child of the current trie node."
  - "Template: `dfs(r, c, node)`. If `board[r][c]` isn't in `node.children`, return. Move to that child, and if its `word` is set, add it to a `found` set. Mark the cell `'#'`, recurse into the neighbors that are on the board and not `'#'`, then put the letter back. Call `dfs(r, c, root)` from every cell and return `list(found)`."
rich_test_results: true
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
<li id="test-6">board <code>[["a","b"],["c","d"]]</code>, words <code>["abdc","abcd","acdb","dbac","aba"]</code> &mdash; should return <code>["abdc","acdb","dbac"]</code> (any order)</li>
<li id="test-7">Performance: a 24x24 board and 6,212 words, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
    return root


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

**Brute force:** run the *Word Search* DFS once for each word: try every cell as a start, and backtrack through the neighbors while the letters match. That's `O(W * rows * cols * 3^L)` for `W` words, and words that share a prefix trace the same paths again and again.

**Bottleneck:** each word is searched on its own, so the work done for `"abc"` is thrown away before searching for `"abd"`.

**Optimal idea:** put all the words in a trie and do one DFS over the board for all of them. Walk the trie as you walk the board: a path on the board continues only while its letters spell a prefix of some word. Every trie node that ends a word stores that word, so reaching it means the word was found.

**Why it's correct:** every path the DFS takes uses each cell at most once, because a cell is marked `'#'` while it's on the current path and restored after. The DFS starts from every cell and tries every unused neighbor, so it reaches every path that spells a prefix of some word. A word is on the board exactly when some such path ends at its trie node. Paths that leave the trie can't be the start of any word, so cutting them off loses nothing. The `found` set keeps a word that's reachable in more than one way from being listed twice.

**Complexity:** `O(rows * cols * 3^L)` time in the worst case for words of length up to `L`: each path branches into at most 3 new neighbors after the first step. In practice the trie stops most paths after a few letters. `O(total letters in words)` space for the trie, plus `O(L)` recursion depth.

**Common mistakes:** not marking the current cell, so a path reuses it (`"aaa"` on a board with two `a`s). Forgetting to restore the letter after the recursion, which breaks the search from later cells. Returning a list that can hold a word twice when it's found from two starting cells.

</details>
