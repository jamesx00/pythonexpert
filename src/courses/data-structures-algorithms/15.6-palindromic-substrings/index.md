---
lesson_name: Palindromic Substrings
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n^2)
  space: O(1)
hints:
  - "Every palindrome has a center. If you expand outward from one center, how many palindromes do you pass?"
  - "Each successful expansion step is one more palindrome. Use *Expand around centres* from *Common 1-D Shapes* in *1-D Dynamic Programming Basics* over all `2n - 1` centers (letters and gaps), and add up the steps."
  - "Template: `expand(l, r)` counts steps while `l >= 0`, `r < n` and `s[l] == s[r]`, moving `l` left and `r` right. The answer is the sum of `expand(i, i) + expand(i, i + 1)` over all `i`."
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
<li id="test-8">Performance: a string of 2,000 characters, within 1 second</li>
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

**Brute force:** test every substring with `s[i:j] == s[i:j][::-1]` and count the hits. That's `O(n^2)` substrings at up to `O(n)` each, so `O(n^3)`: too slow for 2,000 characters.

**Bottleneck:** each substring is checked from scratch, even though `s[l:r + 1]` is a palindrome exactly when `s[l] == s[r]` and the inside `s[l + 1:r]` is one.

**Optimal idea:** expand around each of the `2n - 1` centers. Every step that keeps the ends equal finds one new palindrome, so count the steps.

**Why it's correct:** every palindrome has exactly one center: its middle letter, or the gap between its two middle letters. Expanding from that center reaches it after a fixed number of steps, and it stops at the first mismatch, after which no longer palindrome shares that center. So each palindrome is counted once.

**Complexity:** `O(n^2)` time in the worst case (`"aaaa..."` has `n(n + 1) / 2` palindromes), and close to `O(n)` on text with few long palindromes. `O(1)` extra space. A table `is_pal[i][j]` gives the same count in `O(n^2)` time and space.

**Common mistakes:** skipping the even centers (`"abba"` has `"bb"` and `"abba"`). Counting distinct strings instead of positions: `"aaa"` has `6`, not `3`. Returning `-1` or failing on the empty string, which has `0`.

</details>
