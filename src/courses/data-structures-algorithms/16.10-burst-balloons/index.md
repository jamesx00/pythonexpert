---
lesson_name: Burst Balloons
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n^3)
  space: O(n^2)
hints:
  - "Choosing which balloon to burst first is messy, because its neighbours keep changing. What if you instead choose which balloon in a range is burst *last*? Who are its neighbours then?"
  - "Pad the row with a `1` at each end. Let `dp[l][r]` be the best coins from bursting every balloon strictly between `l` and `r`. If `k` is the last one burst in that range, its neighbours are `l` and `r`, so `dp[l][r] = max(b[l] * b[k] * b[r] + dp[l][k] + dp[k][r])`. That's the interval shape `dp[l][r]` from *Spotting It* in *2-D Dynamic Programming Basics*."
  - "Template: `b = [1] + nums + [1]`, `n = len(b)`, `dp` an `n x n` table of `0`. For `length` from `2` to `n - 1`, for each `left` with `right = left + length`, try every `k` between them. Return `dp[0][n - 1]`."
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

### Burst Balloons

You are given a row of balloons, `nums[i]` holding the number written on the `i`-th balloon. Bursting a balloon at index `i` earns coins equal to `left * nums[i] * right`, where `left` and `right` are the numbers on the balloons currently adjacent to it (treat a boundary past either end as the number `1`). Once burst, a balloon is removed and its former neighbors become adjacent to each other. Write a function `max_coins(nums)` that returns the maximum total coins obtainable by bursting all the balloons in some order.

For example, with `nums = [1, 5]`, bursting the `1` first (its neighbors are the left boundary `1` and the balloon `5`) earns `1*1*5 = 5`; bursting the remaining `5` (now flanked by boundaries on both sides) earns `1*5*1 = 5`, for a total of `10`. Trying the other order earns less, so the best achievable total gives `max_coins([1, 5])` a return value of `10`.

---

### Tests

<ul>
<li id="test-1"><code>max_coins([4, 2, 6, 9])</code> should return <code>309</code></li>
<li id="test-2"><code>max_coins([1, 5])</code> should return <code>10</code></li>
<li id="test-3"><code>max_coins([7])</code> should return <code>7</code></li>
<li id="test-4"><code>max_coins([3, 3])</code> should return <code>12</code></li>
<li id="test-5"><code>max_coins([2, 4, 3])</code> should return <code>33</code></li>
<li id="test-6">Performance: 100 balloons, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_coins(nums):
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            best = 0
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right] + dp[left][k] + dp[k][right]
                best = max(best, coins)
            dp[left][right] = best
    return dp[0][n - 1]
```

**Brute force:** try every order. Burst each balloon first, recurse on the rest, and keep the best. That's `n!` orders: 10 balloons are already 3.6 million, and 100 never finish.

**Bottleneck:** "burst first" doesn't split the problem: after a burst, the two sides become neighbours and still affect each other. The brute force has no small set of subproblems to reuse.

**Optimal idea:** choose the balloon that is burst *last* in a range. Pad the row with a `1` at each end, giving `b`. Let `dp[l][r]` be the most coins from bursting every balloon strictly between `l` and `r`, while `l` and `r` are still there. If `k` goes last, everything between `l` and `k` and between `k` and `r` is already gone, so `k` earns `b[l] * b[k] * b[r]`. The two sides never touch each other because `k` stands between them until the end.

**Why it's correct:** every order has some last balloon `k` in the range. Before `k` bursts, the balloons left of `k` only ever have neighbours from `l` to `k`, and the right side only from `k` to `r`, so the two sides are independent subproblems with best values `dp[l][k]` and `dp[k][r]`. Trying every `k` and filling ranges from short to long covers all orders and only reads finished cells.

**Complexity:** `O(n^3)` time: `O(n^2)` ranges, each trying up to `n` choices of `k`. `O(n^2)` space for the table.

**Common mistakes:** choosing the balloon burst *first*, which leads to the wrong recurrence. Forgetting the padding `1`s. Filling the table by `left` and `right` in plain order, so a longer range reads a shorter one that isn't computed yet; loop by length, or loop `left` downward. Including `l` and `r` themselves in the range.

</details>
