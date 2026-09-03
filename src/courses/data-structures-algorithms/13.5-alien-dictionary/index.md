---
lesson_name: Alien Dictionary
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

### Alien Dictionary

An alien language uses the same alphabet as English, but the letters may be ordered differently. Write a function `alien_order(words)` that takes a list of words which is already sorted according to that unknown alien ordering, and returns one valid ordering of the alphabet's letters (as a string containing each letter that appears in `words` exactly once) that is consistent with how the words were sorted. If no valid ordering exists — the given sequence of words could not have come from any consistent letter ordering — return an empty string `""`.

For example, given `words = ["ac", "ab", "zc", "zb"]`, comparing consecutive words tells us `c` must come before `b`, and `a` must come before `z`, so one valid alien alphabet order is `"acbz"` (any order consistent with those constraints is acceptable), and `alien_order(words)` should return that ordering. If instead the input were `["ab", "aa"]`, no ordering could make `"ab"` sort before `"aa"`, so `alien_order(words)` should return `""`.

---

### Tests

<ul>
<li id="test-1"><code>alien_order(["z", "x"])</code> should return <code>"zx"</code>, the only ordering consistent with <code>z</code> coming before <code>x</code></li>
<li id="test-2"><code>alien_order(["z", "x", "z"])</code> should return <code>""</code>, since the words imply both <code>z</code> before <code>x</code> and <code>x</code> before <code>z</code></li>
<li id="test-3"><code>alien_order(["abc", "ab"])</code> should return <code>""</code>, since a longer word cannot come before its own prefix</li>
<li id="test-4"><code>alien_order(["ac", "ab", "zc", "zb"])</code> should return a valid ordering of <code>{a, b, c, z}</code> that keeps <code>c</code> before <code>b</code> and <code>a</code> before <code>z</code></li>
<li id="test-5"><code>alien_order(["wrt", "wrf", "er", "ett", "rftt"])</code> should return a valid ordering of <code>{w, e, r, t, f}</code> consistent with the given word order</li>
<li id="test-6"><code>alien_order(["abc", "abd", "abe"])</code> should return a valid ordering of <code>{a, b, c, d, e}</code> that keeps <code>c</code> before <code>d</code> and <code>d</code> before <code>e</code></li>
</ul>
