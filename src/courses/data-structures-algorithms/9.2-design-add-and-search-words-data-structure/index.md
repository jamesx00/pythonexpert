---
lesson_name: Design Add and Search Words Data Structure
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

### Design Add and Search Words Data Structure

Build a class `WordDictionary` that stores a growing set of lowercase words and can check whether a pattern matches any stored word, where the pattern may contain the wildcard character `.` standing in for exactly one arbitrary letter.

Implement two methods:
- `add_word(word)` — adds `word` to the dictionary.
- `search(pattern)` — returns `True` if `pattern` matches at least one added word of the same length, `False` otherwise. Each `.` in `pattern` may match any single character; every other character must match exactly.

For example, after `add_word("bear")` and `add_word("beat")`, calling `search("bea.")` returns `True` because both stored words fit that pattern, while `search("bean")` returns `False` since neither stored word is `"bean"`.

---

### Tests

<ul>
<li id="test-1">add "dog", then <code>search("dog")</code> should return <code>True</code></li>
<li id="test-2">add "dog", then <code>search("cat")</code> should return <code>False</code></li>
<li id="test-3">add "dog", then <code>search(".og")</code> should return <code>True</code></li>
<li id="test-4">add "dog", then <code>search("d.g")</code> should return <code>True</code> and <code>search("do.")</code> should return <code>True</code></li>
<li id="test-5">add "bear" and "beat", then <code>search("bea.")</code> should return <code>True</code> and <code>search("bean")</code> should return <code>False</code></li>
<li id="test-6">add "a", then <code>search(".")</code> should return <code>True</code> and <code>search("..")</code> should return <code>False</code></li>
<li id="test-7">with nothing added, <code>search("...")</code> should return <code>False</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_word = True

    def search(self, pattern):
        def dfs(node, i):
            if i == len(pattern):
                return node.is_word
            ch = pattern[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self, 0)
```

</details>
