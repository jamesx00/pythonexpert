---
lesson_name: Implement Trie (Prefix Tree)
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(L) per operation, for a word of length L
  space: O(total letters inserted)
hints:
  - "`search` and `starts_with` both read the word one letter at a time. What could each node store so that words with the same prefix share the same path?"
  - "Use *Node + insert + search* from *Tries Basics*: each node has a `children` dict and an `is_word` flag. `search` and `starts_with` walk the same way. Only `search` checks `is_word` at the end."
  - "Template: `insert` walks the word, creating `children[ch]` when it's missing, then sets `is_word = True` on the last node. `search` and `starts_with` walk the same way and return `False` as soon as a letter is missing. At the end, `search` returns `node.is_word` and `starts_with` returns `True`."
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
<li id="test-7">insert "car", then <code>search("cart")</code> should return <code>False</code>, <code>starts_with("cart")</code> should return <code>False</code>, and <code>starts_with("car")</code> should return <code>True</code></li>
<li id="test-8">Performance: 10,000 words inserted, then 40,000 <code>search</code> and <code>starts_with</code> calls, within 1 second</li>
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

**Brute force:** keep the words in a set. `search` is a set lookup, but `starts_with` has to check `w.startswith(prefix)` for every stored word. That's `O(N * L)` per `starts_with` call for `N` words.

**Bottleneck:** a set can only answer "is this exact word here?". It has no idea which words share a prefix, so a prefix query looks at every word.

**Optimal idea:** store the words letter by letter in a tree. Each node maps a letter to the next node, so words with the same prefix share the same path. A prefix query just walks that path.

**Why it's correct:** after inserting a word, there is a path from the root that spells it, and its last node has `is_word = True`. So a walk that finds every letter has found a prefix of some inserted word, which is what `starts_with` asks. `search` needs more: the walk must end on a node where a word ended. That's why `"appl"` is a prefix of `"apple"` but not a word. Inserting a word twice follows the same path and sets the same flag again, so nothing breaks.

**Complexity:** `O(L)` time per call for a word or prefix of length `L`, one dict lookup per letter, no matter how many words are stored. `O(total letters inserted)` space for the nodes, less when words share prefixes.

**Common mistakes:** returning `True` from `search` without checking `is_word`, so `search("app")` is `True` after inserting only `"apple"`. Sharing one `children` dict between all nodes, for example a mutable default argument like `def __init__(self, children={})`.

</details>
