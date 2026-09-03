---
lesson_name: Implement Trie (Prefix Tree)
code_editor: True
code_execution: True
adding_file_allowed: False
section: Tries
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

### Implement Trie (Prefix Tree)

Build a class `Trie` that stores a set of lowercase words and can quickly answer two kinds of questions: "is this exact word in the set?" and "does any stored word start with this prefix?"

Implement three methods:
- `insert(word)` — adds `word` to the trie. Inserting the same word twice should not cause problems.
- `search(word)` — returns `True` if `word` was previously inserted exactly, `False` otherwise.
- `starts_with(prefix)` — returns `True` if at least one inserted word begins with `prefix`, `False` otherwise.

For example, after calling `insert("garden")`, `search("garden")` returns `True`, but `search("gard")` returns `False` since `"gard"` was never inserted on its own. `starts_with("gard")` returns `True`, though, because `"garden"` begins with that prefix.

---

### Tests

<ul>
<li id="test-1">insert "cat", then <code>search("cat")</code> should return <code>True</code></li>
<li id="test-2">insert "cat", then <code>search("ca")</code> should return <code>False</code> and <code>starts_with("ca")</code> should return <code>True</code></li>
<li id="test-3">insert "bat" and "bath", then <code>search("bat")</code> should return <code>True</code>, <code>search("bath")</code> should return <code>True</code>, and <code>search("ba")</code> should return <code>False</code></li>
<li id="test-4">with nothing inserted, <code>starts_with("z")</code> should return <code>False</code></li>
<li id="test-5">insert "apple" and "app", then <code>search("app")</code> should return <code>True</code>, <code>starts_with("appl")</code> should return <code>True</code>, and <code>search("appl")</code> should return <code>False</code></li>
<li id="test-6">insert "wolf" twice, then <code>search("wolf")</code> should return <code>True</code> and <code>starts_with("wo")</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

</details>
