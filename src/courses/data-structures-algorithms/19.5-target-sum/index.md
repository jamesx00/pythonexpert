---
lesson_name: Target Sum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * sum)
  space: O(n * sum)
hints:
  - "After choosing signs for the first `i` numbers, what's the only thing that matters for the rest? How many different values can that take?"
  - "Only the running total matters. Let `dp(i, total)` be the number of ways to finish from index `i` with the current `total`: `dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])`, and at the end `1` if `total == target` else `0`. A budget like this is the second dimension; memoize it as in *Top-down works too* in *2-D Dynamic Programming Basics*."
  - "Template: inside `count_target_sums`, define `dp(i, total)` decorated with `@functools.cache`. Base case: `i == len(nums)`. Otherwise return the sum of the two recursive calls. Return `dp(0, 0)`."
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

### Target Sum

You are given a list of non-negative integers `nums` and an integer `target`. In front of each number you must place either a `+` or a `-` sign, then sum the whole expression. Write a function `count_target_sums(nums, target)` that returns how many different ways of assigning `+`/`-` signs make the expression evaluate to exactly `target`.

For example, with `nums = [1, 1, 1, 1, 1]` and `target = 3`, one valid assignment is `+1+1+1+1-1 = 3`; counting every sign combination that sums to `3` gives `count_target_sums([1, 1, 1, 1, 1], 3)` a return value of `5`.

---

### Tests

<ul>
<li id="test-1"><code>count_target_sums([1, 1, 1, 1, 1], 3)</code> should return <code>5</code></li>
<li id="test-2"><code>count_target_sums([1], 1)</code> should return <code>1</code></li>
<li id="test-3"><code>count_target_sums([1], 0)</code> should return <code>0</code></li>
<li id="test-4"><code>count_target_sums([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)</code> should return <code>256</code></li>
<li id="test-5"><code>count_target_sums([2, 3, 1, 4], 2)</code> should return <code>2</code></li>
<li id="test-6"><code>count_target_sums([1, 2, 1], 0)</code> should return <code>2</code></li>
<li id="test-7">Performance: 40 numbers and target 10, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from functools import lru_cache


def count_target_sums(nums, target):
    n = len(nums)

    @lru_cache(maxsize=None)
    def dp(i, total):
        if i == n:
            return 1 if total == target else 0
        return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

    result = dp(0, 0)
    dp.cache_clear()
    return result
```

**Brute force:** try every sign pattern. Each number gets `+` or `-`, so there are `2^n` patterns. With 40 numbers that's about a trillion, which never finishes.

**Bottleneck:** many different sign choices for the first `i` numbers give the same running total, and from there the rest behaves exactly the same. The brute force keeps them apart.

**Optimal idea:** the state is `(i, total)`: the next index and the sum so far. The running total always lies between `-s` and `s`, where `s = sum(nums)`, so there are at most `(n + 1) * (2s + 1)` states. Memoize the recursion over them.

**Why it's correct:** every sign pattern goes through exactly one state at each index, so counting the ways out of each state and adding the two choices counts every pattern once. Two prefixes that reach the same `(i, total)` have the same number of ways to finish, so sharing that answer changes nothing.

**Complexity:** `O(n * sum)` time and space, where `sum` is `sum(nums)`: each state is computed once with constant work. There's also a neat rewrite: if `P` is the sum of the `+` numbers, then `P = (sum + target) / 2`, so the question becomes "how many subsets sum to `P`", a 1-D counting table like *Coin Change II* with each number used once.

**Common mistakes:** caching on `i` alone instead of `(i, total)`. Passing `nums` itself to a `@cache` function: lists can't be hashed, so it raises `TypeError`; keep `nums` outside, as here. Skipping zeros: a `0` can take either sign, so it doubles the count (test 4 has eight zeros, so the answer is `2^8 = 256`).

</details>
