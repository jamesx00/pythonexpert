---
lesson_name: Group Anagrams
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

</details>
