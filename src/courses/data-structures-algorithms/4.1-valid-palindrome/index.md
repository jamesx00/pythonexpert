---
lesson_name: Valid Palindrome
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "A palindrome's first character matches its last, its second matches its second-to-last, and so on. Which two characters would you compare first?"
  - "Use opposite-ends pointers (shape 1 in *Two Pointers Basics*): `left` starts at the beginning and `right` at the end. Skip characters that aren't letters or digits (`str.isalnum()`), and compare the rest with `.lower()`."
  - "Template: `while left < right`, move `left` forward past non-alphanumerics, move `right` back past non-alphanumerics, return `False` if the lowercased characters differ, otherwise step both pointers inward. Return `True` after the loop."
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

**Brute force:** build a cleaned, lowercased copy of the string and compare it with its reverse: `cleaned == cleaned[::-1]`. That's `O(n)` time and perfectly fine, but it uses `O(n)` extra space for the copies.

**Bottleneck:** the copies aren't needed. Every comparison only involves one character from each end.

**Optimal idea:** walk two pointers inward from both ends, skipping characters that aren't letters or digits, and compare the characters they land on.

**Why it's correct:** after skipping, `left` and `right` point at the next pair of characters that the cleaned string would compare. If every such pair matches, the cleaned string reads the same both ways. One mismatch is enough to say it doesn't.

**Complexity:** `O(n)` time, because each pointer moves at most `n` steps in total. `O(1)` extra space.

**Common mistakes:** forgetting `left < right` in the inner skip loops, which runs a pointer off the end of a string like `"..,,!!"`. Comparing without `.lower()`, which makes `"A"` and `"a"` differ.

</details>
