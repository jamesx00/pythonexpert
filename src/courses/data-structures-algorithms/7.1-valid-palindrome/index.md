---
lesson_name: Valid Palindrome
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

### Valid Palindrome

Write a function that takes a string and decides whether it reads the same forwards and backwards, once you ignore anything that isn't a letter or digit and ignore letter case. An empty string, or a string with no letters or digits at all, counts as a palindrome.

For example, `"A man, a plan, a canal, Panama"` should be treated as `"amanaplanacanalpanama"` after stripping punctuation and spaces and lowercasing everything, which reads the same in both directions, so it's a palindrome. `"Not a palindrome!"` is not.

---

### Tests

<ul>
<li id="test-1"><code>is_palindrome("A man, a plan, a canal, Panama")</code> should return <code>True</code></li>
<li id="test-2"><code>is_palindrome("Not a palindrome!")</code> should return <code>False</code></li>
<li id="test-3"><code>is_palindrome("")</code> should return <code>True</code></li>
<li id="test-4"><code>is_palindrome("..,,!!")</code> should return <code>True</code></li>
<li id="test-5"><code>is_palindrome("Was it a car or a cat I saw?")</code> should return <code>True</code></li>
<li id="test-6"><code>is_palindrome("race a car")</code> should return <code>False</code></li>
<li id="test-7"><code>is_palindrome("12321")</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

</details>
