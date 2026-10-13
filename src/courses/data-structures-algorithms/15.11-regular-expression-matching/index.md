---
lesson_name: Regular Expression Matching
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n * m)
  space: O(n * m)
hints:
  - "Match from the front. If the next pattern character is followed by `*`, what are the two things that `x*` can do right now?"
  - "Let `dp(i, j)` mean `s[i:]` matches `p[j:]`. Let `first` be whether `s[i]` matches `p[j]` (equal, or `p[j]` is `.`). If `p[j + 1] == '*'`: `dp(i, j + 2)` (use `x*` zero times) or `first and dp(i + 1, j)` (use it once more). Otherwise: `first and dp(i + 1, j + 1)`. Memoize it, as in *Top-down works too* in *2-D Dynamic Programming Basics*."
  - "Template: inside `is_match`, `@functools.cache def dp(i, j)`. If `j == len(p)`, return `i == len(s)`. Compute `first = i < len(s) and p[j] in (s[i], '.')`, then apply the two cases. Return `dp(0, 0)`."
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

### Regular Expression Matching

Write a function `is_match(s, p)` that returns `True` if the pattern `p` matches the entire string `s`, or `False` otherwise. The pattern supports two special symbols: `.` matches any single character, and `*` means the character immediately before it may repeat zero or more times. The match must cover the whole of `s`, not just a prefix.

For example, the pattern `"z*a*b"` matches `"zzab"` because `z*` can absorb both leading `z`s, `a*` absorbs the single `a`, and the final `b` matches literally, so `is_match("zzab", "z*a*b")` should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>is_match("zzab", "z*a*b")</code> should return <code>True</code></li>
<li id="test-2"><code>is_match("greengrass", "gre*n.*s")</code> should return <code>True</code></li>
<li id="test-3"><code>is_match("abc", "abc")</code> should return <code>True</code></li>
<li id="test-4"><code>is_match("", "a*")</code> should return <code>True</code></li>
<li id="test-5"><code>is_match("ab", ".*")</code> should return <code>True</code></li>
<li id="test-6"><code>is_match("abcd", "abc")</code> should return <code>False</code></li>
<li id="test-7"><code>is_match("ab", ".*c")</code> should return <code>False</code></li>
<li id="test-8"><code>is_match("aab", "c*a*b")</code> should return <code>True</code></li>
<li id="test-9">Performance: <code>s</code> of 100 <code>"a"</code>s and pattern <code>"a*"</code> 50 times then <code>"b"</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from functools import lru_cache


def is_match(s, p):
    n, m = len(s), len(p)

    @lru_cache(maxsize=None)
    def dp(i, j):
        if j == m:
            return i == n
        first = i < n and (p[j] == s[i] or p[j] == '.')
        if j + 1 < m and p[j + 1] == '*':
            return dp(i, j + 2) or (first and dp(i + 1, j))
        return first and dp(i + 1, j + 1)

    result = dp(0, 0)
    dp.cache_clear()
    return result
```

**Brute force:** the same recursion without a memo. Each `x*` can stop now or eat one more character, so it branches at every step. With 100 `"a"`s and `"a*"` 50 times then `"b"`, it tries every way of sharing the `"a"`s among the 50 stars before failing on the `"b"`, which never finishes.

**Bottleneck:** whatever choices came before, the rest of the question is only "does `s[i:]` match `p[j:]`?". There are `(n + 1) * (m + 1)` such pairs, and the brute force answers each many times.

**Optimal idea:** memoize `dp(i, j)`. The pattern is read from the front. A character followed by `*` is handled as a unit: either skip `x*` entirely (`j + 2`), or, if `s[i]` matches `x`, consume `s[i]` and stay on `x*` (`i + 1`, same `j`). Any other character must match `s[i]` and both move on.

**Why it's correct:** `x*` matches zero or more `x`s. Zero is `dp(i, j + 2)`. One or more means the first character matches `x` and the rest of `s` still matches `x*` followed by the rest of the pattern, which is `dp(i + 1, j)`. These two cases cover every way `x*` can match. A plain character or `.` matches exactly one character. When the pattern runs out, the match succeeds only if `s` has run out too.

**Complexity:** `O(n * m)` time and space for `s` of length `n` and `p` of length `m`: each `(i, j)` is computed once with constant work. A bottom-up table filled from the ends works the same way.

**Common mistakes:** treating `*` on its own instead of together with the character before it. Checking `first` before the `*` case, which wrongly fails `x*` when `s` is empty or doesn't start with `x`. Returning `True` when the pattern ends but `s` doesn't (the match must cover all of `s`). Using `re.fullmatch`, which works but skips the exercise.

</details>
