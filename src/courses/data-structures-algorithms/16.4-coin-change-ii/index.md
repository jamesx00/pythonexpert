---
lesson_name: Coin Change II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * amount)
  space: O(amount)
hints:
  - "If you let every coin be the 'next' coin at every step, `1+2` and `2+1` are counted separately. How can you make sure each combination is built in only one order?"
  - "Decide coin by coin. Let `dp[a]` be the number of ways to make `a` with the coins handled so far, with `dp[0] = 1`. Adding coin `c` gives `dp[a] += dp[a - c]` for every `a` from `c` up. Loop over coins on the outside, as *Tips & Gotchas* in *2-D Dynamic Programming Basics* explains: that counts combinations, not orderings."
  - "Template: `dp = [1] + [0] * amount`. For each `c` in `coins`: for `a` from `c` to `amount`: `dp[a] += dp[a - c]`. Return `dp[amount]`."
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

### Coin Change II

You have an unlimited supply of coins in the denominations given by the list `coins`, and a target `amount`. Write a function `count_ways(amount, coins)` that returns how many distinct combinations of coins add up to exactly `amount`. Two combinations that use the same coin values with different counts are different, but the order the coins are picked in does not matter (using one `1` then one `2` is the same combination as one `2` then one `1`).

For example, with `amount = 5` and `coins = [1, 2, 5]`, the valid combinations are `5`, `1+2+2`, `1+1+1+2`, and `1+1+1+1+1`, so `count_ways(5, [1, 2, 5])` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>count_ways(5, [1, 2, 5])</code> should return <code>4</code></li>
<li id="test-2"><code>count_ways(3, [2])</code> should return <code>0</code></li>
<li id="test-3"><code>count_ways(10, [10])</code> should return <code>1</code></li>
<li id="test-4"><code>count_ways(0, [1, 2, 3])</code> should return <code>1</code></li>
<li id="test-5"><code>count_ways(7, [2, 3, 5])</code> should return <code>2</code></li>
<li id="test-6"><code>count_ways(4, [1, 2, 3])</code> should return <code>4</code></li>
<li id="test-7">Performance: amount 300 with coins <code>[2, 3, 4, 5, 6, 7, 8, 9, 10]</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_ways(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

**Brute force:** recurse on `(coin index, amount left)`: either use the current coin once more, or move on to the next coin. That counts each combination once, but without a memo it visits every combination one by one. Amount `300` with coins `2` to `10` has 886,046,688 of them.

**Bottleneck:** the recursion only asks "how many ways to make `a` with coins `i` onwards". There are `n * (amount + 1)` such questions, and each is answered many times.

**Optimal idea:** handle one coin at a time. Let `dp[a]` be the number of ways to make `a` with the coins handled so far. Start with `dp[0] = 1` (use nothing) and `0` elsewhere. Adding coin `c`, the ways to make `a` are the old ways (no `c`) plus the ways to make `a - c` that may already use `c`: `dp[a] += dp[a - c]`, with `a` going up.

**Why it's correct:** every combination is counted in exactly one order: all coins of the first kind, then the second kind, and so on. Looping `a` upward makes `dp[a - c]` already include the coin `c`, so `c` can be used any number of times. Looping amounts on the outside and coins on the inside would count `1+2` and `2+1` as different, which is the number of orderings instead.

**Complexity:** `O(n * amount)` time for `n` coins. `O(amount)` space for the one list.

**Common mistakes:** swapping the loops, which counts permutations (`count_ways(5, [1, 2, 5])` would give `9`). Looping `a` downward, which allows each coin at most once. Starting with `dp[0] = 0`, which makes every count `0`. Returning `-1` for "impossible" out of habit from *Coin Change*; here it's `0`.

</details>
