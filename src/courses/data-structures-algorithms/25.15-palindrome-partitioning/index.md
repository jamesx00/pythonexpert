---
lesson_name: Palindrome Partitioning
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(2ⁿ · n)
  space: O(n)
hints:
  - "Pattern: *Backtracking*."
  - "Whatever the partitioning is, its first piece is `s[0:end]` for some `end`. Which values of `end` are worth exploring?"
  - "Use *The Template* from *Backtracking Basics* where the choice is where the next piece ends: from `start`, try every `end`, and only recurse when `s[start:end]` is a palindrome. When `start == len(s)`, record a copy of the path."
  - "Template: `def backtrack(start)`: if `start == len(s)`, record `path[:]`. For `end` in `range(start + 1, len(s) + 1)`: `piece = s[start:end]`, and if `piece == piece[::-1]`, append it, `backtrack(end)`, pop."
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
<li id="test-7">Performance: a 24-character string with only 2 partitionings, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def partition_palindromes(s):
    result = []
    path = []

    def backtrack(start):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                path.append(piece)
                backtrack(end)
                path.pop()

    backtrack(0)
    return result
```

**Brute force:** a string of length `n` has `n - 1` gaps, and each gap is either cut or not, so there are `2ⁿ⁻¹` ways to cut it. Try every one and keep the ones where every piece is a palindrome. That's `O(2ⁿ · n)` even when almost nothing is a palindrome: a 24-letter string with only 2 answers still takes about 8 million tries.

**Bottleneck:** cuts that make a non-palindromic first piece are extended anyway.

**Optimal idea:** choose the pieces from left to right. From `start`, try each possible end of the next piece, and only recurse when that piece is a palindrome. A wrong first piece cuts off its whole branch at once.

**Why it's correct:** every valid partitioning has a first piece `s[0:end]` that is a palindrome, followed by a valid partitioning of `s[end:]`. The loop tries every `end` and the recursion handles the rest, so every partitioning is found once. Pieces are added in order, so joining them gives back `s`. For `s = ""`, `start == len(s)` right away and the result is `[[]]`.

**Complexity:** `O(2ⁿ · n)` time in the worst case, such as a string of one repeated letter, where every cut is valid. Each palindrome check costs `O(n)`. Precomputing a table of which `s[i:j]` are palindromes avoids repeated checks, but doesn't change the worst case, since the output itself can be that big. `O(n)` extra space for the path and recursion, not counting the output.

**Common mistakes:** looping `end` up to `len(s)` instead of `len(s) + 1`, which never takes the last character as part of a piece. Recording `path` instead of a copy. Returning `[]` for the empty string: it has one partitioning, with no pieces.

</details>
