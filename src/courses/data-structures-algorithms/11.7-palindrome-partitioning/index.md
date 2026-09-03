---
lesson_name: Palindrome Partitioning
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

### Palindrome Partitioning

Write a function `partition_palindromes(s)` that takes a string and returns every way to cut it into a sequence of substrings where **each substring on its own is a palindrome**. The pieces of one partitioning must be listed in the order they appear in `s` and, joined back together, must reproduce `s` exactly. The result should be a list of these partitionings (each one a list of substrings); the order in which the different partitionings appear does not matter.

For example, given `"aab"`, one valid way to cut it is `["a", "a", "b"]` (three single-character palindromes), and another is `["aa", "b"]` (since `"aa"` is itself a palindrome). Both belong in the result, so `partition_palindromes("aab")` should return `[["a", "a", "b"], ["aa", "b"]]` in some order.

---

### Tests

<ul>
<li id="test-1"><code>partition_palindromes("aab")</code> should return <code>[["a", "a", "b"], ["aa", "b"]]</code> (any order)</li>
<li id="test-2"><code>partition_palindromes("a")</code> should return <code>[["a"]]</code></li>
<li id="test-3"><code>partition_palindromes("")</code> should return <code>[[]]</code></li>
<li id="test-4"><code>partition_palindromes("aba")</code> should return <code>[["a", "b", "a"], ["aba"]]</code> (any order)</li>
<li id="test-5"><code>partition_palindromes("abc")</code> should return <code>[["a", "b", "c"]]</code></li>
<li id="test-6"><code>partition_palindromes("aa")</code> should return <code>[["a", "a"], ["aa"]]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def partition_palindromes(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(list(path))
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if is_palindrome(piece):
                path.append(piece)
                backtrack(end, path)
                path.pop()

    if s == "":
        return [[]]
    backtrack(0, [])
    return result
```

</details>
