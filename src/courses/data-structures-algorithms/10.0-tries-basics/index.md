---
lesson_name: Tries Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Tries
---

## Why This Pattern Matters &#x1F4A1;

A trie (prefix tree) stores strings character by character, so words that share a prefix share a path. Checking whether any stored word starts with `"app"` takes `O(len("app"))` no matter how many words are stored.

```
root
 └─ a
     └─ p
         └─ p  (end: "app")
             └─ l
                 └─ e  (end: "apple")
```

## Spotting It &#x1F50D;

- **Prefix** queries: autocomplete, "starts with", search suggestions.
- Searching for **many words at once** in the same text or grid (*Word Search II*), where one trie replaces a separate search per word.
- **Wildcard** matching where `.` can be any character.

## Core Building Blocks &#x1F9F1;

### Node + insert + search

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end = False     # does a word end here?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._walk(prefix) is not None
```

The only difference between `search` and `starts_with` is the `is_end` check.

### Wildcards = DFS over children

```python
def search_with_dots(node, word, i=0):
    if i == len(word):
        return node.is_end
    ch = word[i]
    if ch == ".":
        return any(search_with_dots(child, word, i + 1)
                   for child in node.children.values())
    if ch not in node.children:
        return False
    return search_with_dots(node.children[ch], word, i + 1)
```

## Tips & Gotchas &#x1F4CC;

- **Don't forget `is_end`.** Without it, inserting `"apple"` makes `search("app")` wrongly return `True`.
- **`dict` vs `[None] * 26` children:** a dict is simpler and handles any character; a fixed array is slightly faster for lowercase-only input.
- **Store the whole word at its end node** (`node.word = word`) when you'll need it during a DFS, so you don't rebuild it from the path.
- **Grid + trie:** walk the trie *while* you DFS the grid. Stop as soon as the current prefix isn't in the trie. This pruning is what makes *Word Search II* fast.
- **Avoid duplicate results** by clearing `node.word = None` after finding it, and optionally prune empty child nodes.
- Complexity: insert/search are `O(L)` for a word of length `L`; space is `O(total characters stored)`.
