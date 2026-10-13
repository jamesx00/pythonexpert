---
lesson_name: Distinct Subsequences
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n * m)
  space: O(n * m)
hints:
  - "Look at the last character of `s`. Every way of forming `t` either doesn't use it, or uses it as the last character of `t`. How many ways are there in each case?"
  - "Let `dp[i][j]` be the number of ways to form `t[:j]` from `s[:i]`. Always `dp[i][j] = dp[i - 1][j]` (skip `s[i - 1]`), plus `dp[i - 1][j - 1]` when `s[i - 1] == t[j - 1]` (use it). `dp[i][0] = 1`: the empty `t` can be formed one way. It's the two-strings table in *2-D Dynamic Programming Basics*."
  - "Template: an `(n + 1) x (m + 1)` table of `0`, with column `0` set to `1`. For `i` from `1` to `n`, for `j` from `1` to `m`: apply the rule. Return `dp[n][m]`."
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

### Distinct Subsequences

Given two strings `s` and `t`, write a function `num_distinct(s, t)` that returns the number of distinct ways `t` can be formed by deleting zero or more characters from `s` (keeping the remaining characters in their original order). Deletions at different positions that happen to remove the same characters still count as separate ways.

For example, with `s = "xcaxcxaxxc"` and `t = "xc"`, you can pick any `x` that comes before any later `c`; counting every such `(x, c)` pair gives `num_distinct("xcaxcxaxxc", "xc")` a return value of `8`.

---

### Tests

<ul>
<li id="test-1"><code>num_distinct("xcaxcxaxxc", "xc")</code> should return <code>8</code></li>
<li id="test-2"><code>num_distinct("mississippi", "mis")</code> should return <code>6</code></li>
<li id="test-3"><code>num_distinct("abc", "abc")</code> should return <code>1</code></li>
<li id="test-4"><code>num_distinct("abc", "abcd")</code> should return <code>0</code></li>
<li id="test-5"><code>num_distinct("aaaa", "aa")</code> should return <code>6</code></li>
<li id="test-6"><code>num_distinct("", "a")</code> should return <code>0</code></li>
<li id="test-7">Performance: <code>s</code> of 200 <code>"a"</code>s and <code>t</code> of 10 <code>"a"</code>s, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def num_distinct(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[n][m]
```

**Brute force:** recurse on positions `(i, j)`: skip `s[i]`, and if `s[i] == t[j]` also try using it, and add the two counts. Without a memo, every way is found one at a time, so the work is at least the answer. For 200 `"a"`s and 10 `"a"`s the answer is "200 choose 10", about `2 * 10^16`.

**Bottleneck:** the count of ways to form `t[j:]` from `s[i:]` is the same however you reached `(i, j)`. There are only `(n + 1) * (m + 1)` such pairs.

**Optimal idea:** let `dp[i][j]` be the number of ways to form `t[:j]` from `s[:i]`. Forming the empty `t` takes one way (delete everything), so column `0` is `1`. Forming a non-empty `t` from an empty `s` takes none, so the rest of row `0` is `0`.

**Why it's correct:** split the ways to form `t[:j]` from `s[:i]` by whether they use `s[i - 1]`. Those that don't are the ways to form `t[:j]` from `s[:i - 1]`. Those that do must match it with `t[j - 1]`, the last character of `t[:j]`, so this needs `s[i - 1] == t[j - 1]`, and the rest forms `t[:j - 1]` from `s[:i - 1]`. The two groups don't overlap, so the count is their sum.

**Complexity:** `O(n * m)` time and space for `s` of length `n` and `t` of length `m`. One row is enough (loop `j` downward) for `O(m)` space.

**Common mistakes:** setting `dp[0][0]` but not the rest of column `0`. Taking only the "use it" branch when the characters match, and forgetting that skipping is still allowed. Counting distinct resulting strings instead of distinct sets of positions: here every way is a different choice of positions, even when the letters look the same.

</details>
