---
lesson_name: Decode Ways
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Look at the first digit (or two). How many ways are there to read the start of the string, and what's left after each?"
  - "Let `dp[i]` be the number of ways to decode `digits[i:]`, with `dp[n] = 1`. A non-zero digit can stand alone (`dp[i + 1]`), and a two-digit group from `10` to `26` adds `dp[i + 2]`. It's the Fibonacci-like shape in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*."
  - "Template: fill `dp` from right to left. If `digits[i] == '0'`, `dp[i] = 0`. Otherwise `dp[i] = dp[i + 1]`, plus `dp[i + 2]` if `10 <= int(digits[i:i + 2]) <= 26`. Return `dp[0]`."
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

### Decode Ways

Write a function `num_decodings(digits)` that takes a string of digits representing an encoded message, where `"1"` maps to `'A'`, `"2"` maps to `'B'`, and so on up to `"26"` mapping to `'Z'`. Return how many distinct ways the string can be decoded back into letters. A leading zero on its own, or as the first digit of a two-digit group, is never valid on its own (a `'0'` must always be paired with the digit before it as part of `"10"` or `"20"`), so a string containing an unpairable `'0'` decodes zero ways.

For example, given `digits = "226"`, the valid decodings are `"2-2-6"` (BBF), `"22-6"` (VF), and `"2-26"` (BZ), for a total of `3` ways.

---

### Tests

<ul>
<li id="test-1"><code>num_decodings("226")</code> should return <code>3</code></li>
<li id="test-2"><code>num_decodings("12")</code> should return <code>2</code></li>
<li id="test-3"><code>num_decodings("06")</code> should return <code>0</code></li>
<li id="test-4"><code>num_decodings("10")</code> should return <code>1</code></li>
<li id="test-5"><code>num_decodings("100")</code> should return <code>0</code></li>
<li id="test-6"><code>num_decodings("11106")</code> should return <code>2</code></li>
<li id="test-7"><code>num_decodings("")</code> should return <code>1</code></li>
<li id="test-8">Performance: a string of 100 <code>"1"</code>s, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def num_decodings(digits):
    n = len(digits)
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[n] = 1
    dp[n - 1] = 1 if digits[n - 1] != '0' else 0
    for i in range(n - 2, -1, -1):
        if digits[i] == '0':
            dp[i] = 0
            continue
        dp[i] = dp[i + 1]
        two = int(digits[i:i + 2])
        if 10 <= two <= 26:
            dp[i] += dp[i + 2]
    return dp[0]
```

**Brute force:** recurse from the front: read one digit, or two if they form `10` to `26`, and count the ways to decode the rest. With no memo, a string of `1`s branches twice almost everywhere, so it's `O(2^n)`. The 100-character test would never finish.

**Bottleneck:** the number of ways to decode a suffix `digits[i:]` doesn't depend on how you got to `i`, but the recursion recomputes it for every path.

**Optimal idea:** let `dp[i]` be the number of ways to decode `digits[i:]`. The empty suffix has one way (`dp[n] = 1`). Fill from right to left: a non-zero digit alone gives `dp[i + 1]` ways, and a valid two-digit group adds `dp[i + 2]` more.

**Why it's correct:** every decoding of `digits[i:]` starts with exactly one first letter, made of one digit or two. The two choices give different decodings, so their counts add. A `'0'` can't start a letter, so `dp[i] = 0` there, and it can only be read as the second digit of `10` or `20`.

**Complexity:** `O(n)` time. `O(n)` space for `dp`. Only `dp[i + 1]` and `dp[i + 2]` are read, so two variables would make it `O(1)`.

**Common mistakes:** treating `"0"` as a letter, or allowing two-digit groups like `"06"`, which `int` turns into `6`. Accepting `27` to `99`. Returning `0` for the empty string instead of `1` (this lesson treats it as one decoding, the empty one).

</details>
