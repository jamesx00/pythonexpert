---
lesson_name: Longest Common Subsequence
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * m)
  space: O(n * m)
hints:
  - "Look at the last characters of `a` and `b`. If they're equal, can you always use them? If they're different, which one can't be part of the answer?"
  - "Let `dp[i][j]` be the LCS length of `a[:i]` and `b[:j]`. If `a[i - 1] == b[j - 1]`, it's `dp[i - 1][j - 1] + 1`. Otherwise drop one character: `max(dp[i - 1][j], dp[i][j - 1])`. Row `0` and column `0` (an empty string) are all `0`. That's *Two strings: the `(n+1) × (m+1)` table* in *2-D Dynamic Programming Basics*."
  - "Template: `dp = [[0] * (m + 1) for _ in range(n + 1)]`. For `i` from `1` to `n`, for `j` from `1` to `m`: apply the rule above. Return `dp[n][m]`."
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

### Longest Common Subsequence

Given two strings `a` and `b`, write a function `longest_common_subsequence(a, b)` that returns the length of their longest common subsequence — the longest sequence of characters that appears in both strings in the same relative order, though not necessarily contiguously.

For example, with `a = "abcde"` and `b = "ace"`, the subsequence `"ace"` appears in both in order, so `longest_common_subsequence("abcde", "ace")` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>longest_common_subsequence("abcde", "ace")</code> should return <code>3</code></li>
<li id="test-2"><code>longest_common_subsequence("abc", "abc")</code> should return <code>3</code></li>
<li id="test-3"><code>longest_common_subsequence("abc", "def")</code> should return <code>0</code></li>
<li id="test-4"><code>longest_common_subsequence("", "abc")</code> should return <code>0</code></li>
<li id="test-5"><code>longest_common_subsequence("bsbininm", "jmjkbkjkv")</code> should return <code>1</code></li>
<li id="test-6"><code>longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy")</code> should return <code>2</code></li>
<li id="test-7">Performance: two strings of 150 characters, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def longest_common_subsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
```

**Brute force:** recurse on the first characters: if they match, take both and move on; otherwise try skipping one character of `a` and, separately, one of `b`, and keep the better. Without a memo, each mismatch splits into two calls, so the work grows exponentially. Two 150-character strings never finish.

**Bottleneck:** the recursion only ever asks about suffix pairs `(a[i:], b[j:])`. There are just `(n + 1) * (m + 1)` of them, but each is solved again and again.

**Optimal idea:** store one answer per pair of prefixes. Let `dp[i][j]` be the LCS length of `a[:i]` and `b[:j]`. Row `0` and column `0` stand for an empty string, so they're `0`. Fill the table row by row.

**Why it's correct:** if `a[i - 1] == b[j - 1]`, some longest common subsequence ends by matching these two characters, so the answer is one more than for the shorter prefixes. If they differ, they can't both be the last matched pair, so at least one of them is unused. Dropping it leaves `dp[i - 1][j]` or `dp[i][j - 1]`, and the better of the two is the answer.

**Complexity:** `O(n * m)` time for strings of length `n` and `m`: each cell takes constant work. `O(n * m)` space, or `O(m)` if you keep only the previous row.

**Common mistakes:** indexing the strings with `i` and `j` instead of `i - 1` and `j - 1`; the table is shifted by one. Building rows with `[[0] * (m + 1)] * (n + 1)`, so all rows are the same list. Treating it as longest common substring, which needs the characters to be next to each other.

</details>
