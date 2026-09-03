---
lesson_name: Palindromic Substrings
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

### Palindromic Substrings

Write a function `count_palindromic_substrings(s)` that takes a string `s` and returns how many of its contiguous substrings are palindromes. Substrings that are equal in characters but occur at different positions each count separately, and every single character counts as a palindrome of length 1.

For example, given `s = "aaa"`, the palindromic substrings are `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, and `"aaa"`, for a total count of `6`.

---

### Tests

<ul>
<li id="test-1"><code>count_palindromic_substrings("aaa")</code> should return <code>6</code></li>
<li id="test-2"><code>count_palindromic_substrings("abc")</code> should return <code>3</code></li>
<li id="test-3"><code>count_palindromic_substrings("")</code> should return <code>0</code></li>
<li id="test-4"><code>count_palindromic_substrings("aba")</code> should return <code>4</code></li>
<li id="test-5"><code>count_palindromic_substrings("abba")</code> should return <code>6</code></li>
<li id="test-6"><code>count_palindromic_substrings("racecar")</code> should return <code>10</code></li>
<li id="test-7"><code>count_palindromic_substrings("z")</code> should return <code>1</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_palindromic_substrings(s):
    n = len(s)
    count = 0

    def expand(l, r):
        c = 0
        while l >= 0 and r < n and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    for i in range(n):
        count += expand(i, i)
        count += expand(i, i + 1)
    return count
```

</details>
