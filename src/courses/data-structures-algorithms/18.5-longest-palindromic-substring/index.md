---
lesson_name: Longest Palindromic Substring
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n^2)
  space: O(1)
hints:
  - "Every palindrome has a center: one letter (odd length) or the gap between two letters (even length). If you knew the center, how would you find the longest palindrome around it?"
  - "Grow outward from the center while the letters on both sides match. This is *Expand around centres* in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*. There are `2n - 1` centers; keep the longest result."
  - "Template: `expand(l, r)` moves `l` left and `r` right while `s[l] == s[r]`, then returns `l + 1, r - 1`. For each `i`, try `expand(i, i)` and `expand(i, i + 1)` and keep the longest. Return `s[start:end + 1]`."
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
<li id="test-8">Performance: a string of 2,043 characters, within 1 second</li>
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

**Brute force:** check every substring with `sub == sub[::-1]` and keep the longest. There are about `n^2 / 2` substrings and each check costs up to `O(n)`, so it's `O(n^3)`: too slow for 2,000 characters.

**Bottleneck:** checking substrings one at a time throws away what you learned. If `s[l + 1:r]` is a palindrome, `s[l:r + 1]` is one exactly when `s[l] == s[r]`.

**Optimal idea:** build palindromes from the middle out. For each of the `2n - 1` centers (each letter, and each gap between two letters), expand while the ends match. Each step adds two letters to a palindrome you already know.

**Why it's correct:** expanding only ever produces palindromes. The longest palindrome has a center too, and expanding from it gets all the way to its ends, because the letters match in pairs all the way out. So the longest expansion over all centers is the longest palindrome. The even centers `(i, i + 1)` are needed for answers like `"bb"`.

**Complexity:** `O(n^2)` time in the worst case (a string like `"aaaa..."`), and much faster on typical text. `O(1)` extra space apart from the answer. The DP alternative, a table `is_pal[i][j]`, is also `O(n^2)` time but needs `O(n^2)` space.

**Common mistakes:** only trying odd centers, which misses even-length palindromes. Returning `s[l:r]` after the loop: when the loop stops, `l` and `r` are one step past the palindrome. Mixing up start/length and start/end, and returning a string one letter too short or long.

</details>
