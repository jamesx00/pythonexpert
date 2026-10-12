---
lesson_name: Design Add and Search Words Data Structure
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(L) per add_word and per search without dots
  space: O(total letters added)
hints:
  - "Pattern: *Tries*."
  - "Without dots, `search` is a normal trie lookup. When you reach a `.`, which children could the rest of the pattern continue from?"
  - "Use *Wildcards = DFS over children* from *Tries Basics*: on a letter, follow that one child. On a `.`, try every child and return `True` as soon as one of them matches the rest of the pattern."
  - "Template: `dfs(node, i)`. If `i == len(pattern)`, return `node.is_word`. If `pattern[i] == '.'`, return `True` if `dfs(child, i + 1)` is `True` for any child. Otherwise return `False` if the letter isn't in `node.children`, else `dfs(node.children[pattern[i]], i + 1)`. Start with `dfs(root, 0)`."
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
<li id="test-8">add "card", then <code>search("car")</code> should return <code>False</code>, <code>search("car.")</code> should return <code>True</code>, and <code>search("...")</code> should return <code>False</code></li>
<li id="test-9">add "ab" and "cd", then <code>search("a.")</code> should return <code>True</code>, <code>search(".d")</code> should return <code>True</code>, and <code>search("c.d")</code> should return <code>False</code></li>
<li id="test-10">Performance: 10,000 words added, then 4,000 searches with two dots each, within 1 second</li>
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

**Brute force:** keep the words in a list. `search` compares the pattern with every word of the same length, letter by letter, treating `.` as a match. That's `O(N * L)` per search for `N` words.

**Bottleneck:** most words fail on the first or second letter, but the list makes you look at each one anyway. Words with the same prefix are compared again and again.

**Optimal idea:** store the words in a trie. A letter in the pattern follows exactly one child. A `.` tries every child, so the search becomes a DFS over the trie that only goes down paths that still match.

**Why it's correct:** a stored word matches the pattern exactly when each pattern letter is either `.` or the word's letter at that position, and the lengths are equal. The DFS follows every path whose letters fit the pattern so far, and a path stops as soon as a letter can't be matched. When the pattern runs out, `node.is_word` tells whether a word ends there, which also handles the length check: `".."` doesn't match `"a"` because there's no node two levels down.

**Complexity:** `O(L)` time for `add_word`, and for a `search` without dots. Each `.` can fan out to up to 26 children, so a search with `d` dots visits up to `O(26^d * L)` nodes, but it never visits more nodes than the trie has. `O(total letters added)` space, plus `O(L)` recursion depth.

**Common mistakes:** returning the result of the first child on a `.` instead of trying the others when it's `False`. Returning `True` when the pattern runs out without checking `is_word`, so `"car"` matches after adding only `"card"`.

</details>
