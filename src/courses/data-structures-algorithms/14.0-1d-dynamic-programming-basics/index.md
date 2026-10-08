---
lesson_name: 1-D Dynamic Programming Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: 1-D Dynamic Programming
---

## Why This Pattern Matters &#x1F4A1;

Dynamic programming (DP) is recursion that **remembers** results. If solving a problem means solving the same smaller problems over and over, store each answer the first time and reuse it. That often turns exponential time into linear.

Fibonacci shows the idea. The naive version recomputes `fib(3)` many times:

```python
def fib(n):            # O(2^n) — every call branches twice
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

## Spotting It &#x1F50D;

- "**How many ways** to ___?", "**minimum/maximum** cost to ___?", "**can** you reach ___?"
- Each choice affects what choices remain (take this house → can't take the next one).
- A brute-force recursion exists, but its calls overlap.

## The Recipe &#x1F9EA;

1. **Define the state.** What does `dp[i]` mean, in one sentence? *"`dp[i]` = the most money robbing houses `0..i`."*
2. **Write the recurrence.** How does `dp[i]` depend on smaller states? *`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.*
3. **Set the base cases.** *`dp[0] = nums[0]`.*
4. **Pick the order** (or let memoization handle it) and **return** the right cell.

## Two Ways to Implement &#x1F9F1;

### Top-down: recursion + memo

Write the brute-force recursion, then cache it:

```python
from functools import cache

def climb_stairs(n):
    @cache
    def ways(i):
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)
    return ways(n)
```

`@cache` (or `@lru_cache(None)`) stores results by argument. A hand-written version uses a dict: check `if i in memo` first, store before returning.

### Bottom-up: fill a table

```python
def climb_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### Space optimisation

If `dp[i]` only needs the last two values, keep two variables:

```python
a, b = 1, 1
for _ in range(n - 1):
    a, b = b, a + b
```

## Common 1-D Shapes &#x1F4D0;

| Shape | Recurrence idea | Examples |
| --- | --- | --- |
| Fibonacci-like | `dp[i]` from `dp[i-1]`, `dp[i-2]` | Climbing Stairs, House Robber, Decode Ways |
| Unbounded choices | `dp[a] = min(dp[a - c] + 1 for c in coins)` | Coin Change, Word Break |
| Look at all earlier `j` | `dp[i] = max(dp[j] + 1 for j < i if ...)` | Longest Increasing Subsequence |
| Track min **and** max | negatives flip signs | Maximum Product Subarray |
| Expand around centres | not a table, but reuses overlap | Palindromic Substrings |

## Tips & Gotchas &#x1F4CC;

- **Start top-down.** It's closer to how you think about the problem. Convert to bottom-up later if needed.
- **Say the state out loud.** Most DP bugs come from a vague definition of `dp[i]`.
- **Size the table `n + 1`** when `dp[0]` means "empty prefix". It removes many edge cases.
- **Use `float("inf")` as "impossible"** for minimum problems, and check for it at the end (return `-1`).
- **Circular arrays** (*House Robber II*): run the linear solution twice, once without the first element and once without the last.
- **Memo keys must be hashable.** Pass indices, not lists or slices.
- Complexity = *(number of states) × (work per state)*.
