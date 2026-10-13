---
lesson_name: Interleaving String
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * m)
  space: O(n * m)
hints:
  - "Suppose you've used the first `i` characters of `s1` and the first `j` of `s2`. Which character of `s3` must come next, and where can it come from?"
  - "Let `dp[i][j]` mean `s1[:i]` and `s2[:j]` can interleave into `s3[:i + j]`. It's true if `dp[i - 1][j]` is true and `s1[i - 1] == s3[i + j - 1]`, or if `dp[i][j - 1]` is true and `s2[j - 1] == s3[i + j - 1]`. It's the two-strings table from *2-D Dynamic Programming Basics*, with `dp[0][0] = True`."
  - "Template: if `len(s1) + len(s2) != len(s3)`, return `False`. Build an `(n + 1) x (m + 1)` table of `False`, set `dp[0][0] = True`, fill every other cell with the rule above in row order, and return `dp[n][m]`."
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

### Interleaving String

Given three strings `s1`, `s2`, and `s3`, write a function `is_interleave(s1, s2, s3)` that returns `True` if `s3` can be formed by interleaving the characters of `s1` and `s2` while preserving each string's own internal character order, and `False` otherwise. `s3` must use every character of `s1` and `s2` exactly once and be the same length as `s1` and `s2` combined.

For example, `s1 = "abc"` and `s2 = "def"` can interleave into `s3 = "adbcef"` (take `a` from `s1`, `d` from `s2`, `b` from `s1`, `c` from `s1`, `e` from `s2`, `f` from `s2`), so `is_interleave("abc", "def", "adbcef")` should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>is_interleave("abc", "def", "adbcef")</code> should return <code>True</code></li>
<li id="test-2"><code>is_interleave("abc", "def", "abdecf")</code> should return <code>True</code></li>
<li id="test-3"><code>is_interleave("", "", "")</code> should return <code>True</code></li>
<li id="test-4"><code>is_interleave("abc", "", "abc")</code> should return <code>True</code></li>
<li id="test-5"><code>is_interleave("aabcc", "dbbca", "aadbbbaccc")</code> should return <code>False</code></li>
<li id="test-6"><code>is_interleave("ab", "bc", "babc")</code> should return <code>True</code></li>
<li id="test-7"><code>is_interleave("ab", "ac", "acab")</code> should return <code>True</code></li>
<li id="test-8">Performance: two strings of 100 <code>"a"</code>s against 199 <code>"a"</code>s and a <code>"b"</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_interleave(s1, s2, s3):
    n, m = len(s1), len(s2)
    if n + m != len(s3):
        return False
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            ok = False
            if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                ok = True
            if not ok and j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                ok = True
            dp[i][j] = ok
    return dp[n][m]
```

**Brute force:** walk along `s3`. At each character, try taking it from `s1` if it matches there, and from `s2` if it matches there, and recurse. When both strings start with the same letter, each step branches in two. For `"a" * 100` and `"a" * 100` against 199 `"a"`s and a `"b"`, every one of the huge number of orders fails only at the end, so it never finishes.

**Bottleneck:** the position in `s3` is always `i + j`, so the state is just `(i, j)`. Many different orders reach the same `(i, j)`, and the brute force redoes the rest of the work for each.

**Optimal idea:** fill a table with one cell per `(i, j)`. `dp[i][j]` says whether `s1[:i]` and `s2[:j]` can interleave into `s3[:i + j]`. `dp[0][0]` is true (three empty strings). Each other cell checks its two possible last moves.

**Why it's correct:** in any valid interleaving of `s1[:i]` and `s2[:j]`, the last character of `s3[:i + j]` is either `s1[i - 1]` or `s2[j - 1]`. If it's `s1[i - 1]`, the rest must be a valid interleaving of `s1[:i - 1]` and `s2[:j]`, which is `dp[i - 1][j]`. The other case is the same with `s2`. So the cell is true exactly when one of the two cases works.

**Complexity:** `O(n * m)` time and space for `s1` and `s2` of lengths `n` and `m`. One row is enough for `O(m)` space.

**Common mistakes:** skipping the length check, so a too-short `s3` is accepted or the indexing runs off the end. Using `s3[i + j]` instead of `s3[i + j - 1]` with the shifted table. A greedy two-pointer scan that always takes from `s1` first: it fails on `("ab", "ac", "acab")`, where the first `a` must come from `s2`.

</details>
