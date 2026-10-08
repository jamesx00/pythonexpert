---
lesson_name: Longest Palindromic Substring
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

### Longest Palindromic Substring

Write a function `longest_palindrome(s)` that takes a string `s` and returns the longest contiguous substring of `s` that reads the same forwards and backwards. If more than one substring achieves the maximum length, returning any one of them is acceptable.

For example, given `s = "babad"`, both `"bab"` and `"aba"` are valid answers since they're both palindromes of length 3, the maximum possible for this input.

---

### Tests

<ul>
<li id="test-1"><code>longest_palindrome("babad")</code> should return a length-3 palindrome that is a substring of <code>"babad"</code></li>
<li id="test-2"><code>longest_palindrome("cbbd")</code> should return <code>"bb"</code></li>
<li id="test-3"><code>longest_palindrome("a")</code> should return <code>"a"</code></li>
<li id="test-4"><code>longest_palindrome("forgeeksskeegfor")</code> should return <code>"geeksskeeg"</code></li>
<li id="test-5"><code>longest_palindrome("abcde")</code> should return a length-1 palindrome that is a substring of <code>"abcde"</code></li>
<li id="test-6"><code>longest_palindrome("racecarxyz")</code> should return <code>"racecar"</code></li>
<li id="test-7"><code>longest_palindrome("")</code> should return <code>""</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def longest_palindrome(s):
    if not s:
        return ""
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]
```

</details>
