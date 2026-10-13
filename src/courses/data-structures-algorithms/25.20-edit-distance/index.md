---
lesson_name: Edit Distance
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * m)
  space: O(n * m)
hints:
  - "Pattern: *2-D Dynamic Programming*."
  - "Compare the last characters of the two strings. If they're equal, do they need any edit? If not, what are the three things the last edit could be?"
  - "Let `dp[i][j]` be the edit distance between `a[:i]` and `b[:j]`. If `a[i - 1] == b[j - 1]`, it's `dp[i - 1][j - 1]`. Otherwise it's `1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])` for delete, insert and replace. `dp[i][0] = i` and `dp[0][j] = j`. *Top-down works too* in *2-D Dynamic Programming Basics* shows the same recurrence written top-down."
  - "Template: an `(n + 1) x (m + 1)` table. Fill row `0` with `0..m` and column `0` with `0..n`. For `i` from `1` to `n`, for `j` from `1` to `m`: apply the rule. Return `dp[n][m]`."
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

### Edit Distance

Given two strings `a` and `b`, write a function `edit_distance(a, b)` that returns the minimum number of single-character insertions, deletions, or substitutions needed to turn `a` into `b`.

For example, turning `"plane"` into `"plant"` only needs one substitution — swap the final `e` for a `t` — so `edit_distance("plane", "plant")` should return `1`.

---

### Tests

<ul>
<li id="test-1"><code>edit_distance("plane", "plant")</code> should return <code>1</code></li>
<li id="test-2"><code>edit_distance("abc", "abc")</code> should return <code>0</code></li>
<li id="test-3"><code>edit_distance("", "abc")</code> should return <code>3</code></li>
<li id="test-4"><code>edit_distance("draft", "crate")</code> should return <code>3</code></li>
<li id="test-5"><code>edit_distance("sunday", "saturday")</code> should return <code>3</code></li>
<li id="test-6"><code>edit_distance("a", "b")</code> should return <code>1</code></li>
<li id="test-7">Performance: two strings of 150 characters, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]
```

**Brute force:** recurse on `(i, j)`: if the characters match, move both on; otherwise try delete, insert and replace and keep the cheapest plus one. Without a memo, every mismatch splits into three calls, so the work grows exponentially. Two 150-character strings never finish.

**Bottleneck:** the cost to fix `a[i:]` into `b[j:]` depends only on `(i, j)`, and there are only `(n + 1) * (m + 1)` pairs. The brute force reaches the same pair along a huge number of edit orders.

**Optimal idea:** let `dp[i][j]` be the fewest edits to turn `a[:i]` into `b[:j]`. Turning a prefix into the empty string takes `i` deletions, and building `b[:j]` from nothing takes `j` insertions. Fill the rest row by row.

**Why it's correct:** look at the last characters. If `a[i - 1] == b[j - 1]`, keeping them costs nothing, and no solution does better than `dp[i - 1][j - 1]`. Otherwise the last edit fixes the end of the string in one of three ways: delete `a[i - 1]` (then solve `a[:i - 1]` to `b[:j]`), insert `b[j - 1]` (then solve `a[:i]` to `b[:j - 1]`), or replace `a[i - 1]` with `b[j - 1]` (then solve `a[:i - 1]` to `b[:j - 1]`). The best is one more than the cheapest of the three.

**Complexity:** `O(n * m)` time and space for strings of length `n` and `m`. Two rows are enough for `O(m)` space.

**Common mistakes:** filling row `0` and column `0` with `0` instead of `j` and `i`. Adding `1` even when the characters match. Mixing up which neighbour is insert and which is delete (it doesn't change the answer, but it confuses the reasoning). Using the `i`, `j` indices on the strings without the `- 1` shift.

</details>
