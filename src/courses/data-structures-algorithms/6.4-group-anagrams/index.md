---
lesson_name: Group Anagrams
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n·k log k)
  space: O(n·k)
hints:
  - "Anagrams look different but share something. What could you compute from a word that is the same for every anagram of it?"
  - "Sorting a word's letters gives the same string for all its anagrams: `\"eat\"`, `\"tea\"` and `\"ate\"` all become `\"aet\"`. Use that as a dictionary key. This is the *Grouping by a key* block in *Arrays & Hashing Basics*."
  - "Template: `groups.setdefault(key, []).append(word)` for each word, with `key = \"\".join(sorted(word))`. Return `list(groups.values())`."
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

### Group Anagrams

Write a function `group_anagrams(words)` that takes a list of lowercase strings and groups the words that are anagrams of each other, returning a list of groups. Every input word must appear in exactly one group, and the order of the groups and the order of words within a group do not matter.

For example, given `["bat", "tab", "eat", "tea", "owl"]`, the words `"bat"` and `"tab"` are anagrams of each other, as are `"eat"` and `"tea"`, while `"owl"` shares no group with anything else. A valid return value would be `[["bat", "tab"], ["eat", "tea"], ["owl"]]`.

---

### Tests

<ul>
<li id="test-1"><code>group_anagrams(["bat", "tab", "eat", "tea", "owl"])</code> should return <code>[["bat", "tab"], ["eat", "tea"], ["owl"]]</code> (grouping may differ in order)</li>
<li id="test-2"><code>group_anagrams([])</code> should return <code>[]</code></li>
<li id="test-3"><code>group_anagrams([""])</code> should return <code>[[""]]</code></li>
<li id="test-4"><code>group_anagrams(["abc", "cba", "bca", "xyz"])</code> should return <code>[["abc", "cba", "bca"], ["xyz"]]</code> (grouping may differ in order)</li>
<li id="test-5"><code>group_anagrams(["a", "a", "a"])</code> should return <code>[["a", "a", "a"]]</code></li>
<li id="test-6"><code>group_anagrams(["cat", "dog"])</code> should return <code>[["cat"], ["dog"]]</code> (grouping may differ in order)</li>
<li id="test-7">Performance: 20,000 words in 10,000 groups, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

Here `n` is the number of words and `k` is the length of the longest word.

**Brute force:** keep a list of groups. For each word, compare it with the first word of every existing group and add it to the group it matches. With many groups this is `O(n²)` comparisons.

**Bottleneck:** every new word is compared against every group to find the one it belongs to.

**Optimal idea:** give each word a key that's identical for all its anagrams, the word's letters in sorted order. A dictionary from key to group then finds the right group in one `O(1)` lookup.

**Why it's correct:** two words are anagrams exactly when their sorted letters are equal, so two words share a key exactly when they belong in the same group.

**Complexity:** `O(n·k log k)` time: one `O(k log k)` sort per word. `O(n·k)` space to store every word and key. A 26-letter count tuple, `tuple(counts)`, is also a valid key and brings the time down to `O(n·k)`.

**Common mistakes:** using `sorted(word)` directly as the key. It's a list, and lists can't be dictionary keys, so join it into a string or convert it to a tuple.

</details>
