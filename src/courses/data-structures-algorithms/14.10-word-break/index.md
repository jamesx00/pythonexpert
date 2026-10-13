---
lesson_name: Word Break
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n^3)
  space: O(n)
hints:
  - "If you already knew which prefixes of `s` can be split into words, how would you decide for a longer prefix?"
  - "Let `dp[i]` mean \"`s[:i]` can be split\", with `dp[0] = True` for the empty prefix. Then `dp[i]` is true if some `j < i` has `dp[j]` true and `s[j:i]` in the dictionary. It's the unbounded-choices shape in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*."
  - "Template: `words = set(word_dict)`, `dp = [True] + [False] * n`. For `i` from `1` to `n`, for `j` from `0` to `i - 1`: if `dp[j] and s[j:i] in words`, set `dp[i] = True` and break. Return `dp[n]`."
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

### Word Break

Write a function `word_break(s, word_dict)` that takes a string `s` and a list of dictionary words `word_dict`, and returns `True` if `s` can be split into a sequence of one or more dictionary words placed back to back with nothing left over, or `False` otherwise. Each dictionary word may be reused as many times as needed.

For example, given `s = "pineapplepen"` and `word_dict = ["pine", "apple", "pen"]`, the string can be split as `"pine" + "apple" + "pen"`, so the function should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>word_break("pineapplepen", ["pine", "apple", "pen"])</code> should return <code>True</code></li>
<li id="test-2"><code>word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])</code> should return <code>False</code></li>
<li id="test-3"><code>word_break("leetcode", ["leet", "code"])</code> should return <code>True</code></li>
<li id="test-4"><code>word_break("applepenapple", ["apple", "pen"])</code> should return <code>True</code></li>
<li id="test-5"><code>word_break("aaaaaaa", ["aaaa", "aaa"])</code> should return <code>True</code></li>
<li id="test-6"><code>word_break("aaaaaaab", ["aaaa", "aaa"])</code> should return <code>False</code></li>
<li id="test-7"><code>word_break("", ["a"])</code> should return <code>True</code></li>
<li id="test-8">Performance: 100 <code>"a"</code>s followed by a <code>"b"</code>, with the words <code>"a"</code> to <code>"aaaaa"</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def word_break(s, word_dict):
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
```

**Brute force:** try every word that `s` starts with, and recurse on the rest. With no memo, a string like `"aaaa...ab"` has an exponential number of ways to split the `a`s, and every one of them fails at the `b`, so the search tries them all.

**Bottleneck:** whether the suffix from position `i` can be split doesn't depend on how you reached `i`, but the recursion asks again for every path that reaches it.

**Optimal idea:** let `dp[i]` say whether the prefix `s[:i]` can be split. The empty prefix can. A longer prefix can if it ends with a dictionary word `s[j:i]` whose start `j` is itself a split point.

**Why it's correct:** any split of `s[:i]` has a last word `s[j:i]`, and the words before it are a split of `s[:j]`. So `dp[i]` is true exactly when some `j` works. Filling `dp` left to right means `dp[j]` is final when it's read.

**Complexity:** `O(n^3)` time in the worst case, where `n = len(s)`: there are `O(n^2)` pairs `(j, i)`, and slicing and hashing `s[j:i]` costs up to `O(n)`. The `break` and the `dp[j]` check skip most of that in practice, and only trying `j` within the longest word's length of `i` makes it faster still. `O(n)` space for `dp`, plus the set of words.

**Common mistakes:** checking `word in list` instead of a `set`, which makes every lookup slow. Greedy matching (always the longest or shortest word), which fails on inputs like `"aaaaaaa"` with `["aaaa", "aaa"]`. Forgetting `dp[0] = True`, so nothing can ever be split.

</details>
