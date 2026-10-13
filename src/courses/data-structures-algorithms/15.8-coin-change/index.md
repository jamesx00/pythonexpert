---
lesson_name: Coin Change
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * amount)
  space: O(amount)
hints:
  - "If you knew the fewest coins for every smaller amount, what would the last coin of the best answer for `amount` be?"
  - "Try each coin `c` as the last one: `dp[a] = min(dp[a - c] + 1)` over coins with `c <= a`, and `dp[0] = 0`. That's the unbounded-choices shape in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*. Use `float(\"inf\")` for amounts that can't be made."
  - "Template: `dp = [0] + [inf] * amount`. For `a` from `1` to `amount`, for each coin `c <= a`: `dp[a] = min(dp[a], dp[a - c] + 1)`. Return `dp[amount]`, or `-1` if it's still `inf`."
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

### Coin Change

Write a function `coin_change(coins, amount)` that takes a list of distinct coin denominations and a target `amount`, and returns the fewest number of coins needed to make exactly `amount` using an unlimited supply of each denomination. If `amount` cannot be made exactly with the given coins, return `-1`.

For example, given `coins = [1, 3, 4]` and `amount = 6`, the fewest coins needed is `2`, using one `3` coin plus one more `3` coin.

---

### Tests

<ul>
<li id="test-1"><code>coin_change([1, 3, 4], 6)</code> should return <code>2</code></li>
<li id="test-2"><code>coin_change([2, 5], 3)</code> should return <code>-1</code></li>
<li id="test-3"><code>coin_change([1], 0)</code> should return <code>0</code></li>
<li id="test-4"><code>coin_change([1, 2, 5], 11)</code> should return <code>3</code></li>
<li id="test-5"><code>coin_change([2], 3)</code> should return <code>-1</code></li>
<li id="test-6"><code>coin_change([1, 5, 10, 25], 30)</code> should return <code>2</code></li>
<li id="test-7"><code>coin_change([5, 7], 3)</code> should return <code>-1</code></li>
<li id="test-8">Performance: coins <code>[7, 11, 13]</code> and amount 500, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Brute force:** recurse on the last coin: try each coin, solve the smaller amount, and keep the fewest. With no memo, the same amounts are solved over and over and the work grows exponentially with `amount`. Greedy (largest coin first) is fast but wrong: for `[1, 3, 4]` and `6` it uses `4 + 1 + 1`, three coins, instead of `3 + 3`.

**Bottleneck:** there are only `amount + 1` different questions ("fewest coins for `a`"), but the recursion asks each one many times.

**Optimal idea:** let `dp[a]` be the fewest coins that make `a`. Fill it from `0` up. For each `a`, try every coin as the last one: `dp[a - c] + 1`. Amounts that can't be made stay at infinity.

**Why it's correct:** an optimal way to make `a` ends with some coin `c`. The coins before it make `a - c`, and they must be an optimal way to make `a - c`, or swapping in a better one would improve the answer. Trying every `c` therefore finds the optimum. Since `dp` is filled in increasing order, `dp[a - c]` is final when it's read.

**Complexity:** `O(n * amount)` time, where `n` is the number of coins. `O(amount)` space for `dp`.

**Common mistakes:** using greedy. Returning `inf` instead of `-1`. Initialising `dp` with `0`s instead of infinity, so impossible amounts look free. Forgetting `dp[0] = 0`, which every answer is built from.

</details>
