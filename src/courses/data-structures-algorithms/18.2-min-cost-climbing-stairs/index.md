---
lesson_name: Min Cost Climbing Stairs
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "To stand on step `i` (or the top), you came from `i - 1` or `i - 2`. What did each of those cost you in total?"
  - "Use the recipe in *1-D Dynamic Programming Basics*: let `dp[i]` be the cheapest cost to *reach* step `i`, with `dp[0] = dp[1] = 0` because you can start on either for free. Then `dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])`. The top is step `n`."
  - "Template: `dp = [0] * (n + 1)`. For `i` from `2` to `n`, apply the recurrence above. Return `dp[n]`."
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

### Min Cost Climbing Stairs

Write a function `min_cost_climbing_stairs(cost)` that takes a list of integers where `cost[i]` is the price to step on stair `i`. From either stair `0` or stair `1` you may start for free, and each move advances you 1 or 2 stairs. The staircase has one extra stair past the last index in `cost`, representing the top, and you're done once you reach or pass it. Return the minimum total cost to reach the top.

For example, given `cost = [10, 15, 20]`, the cheapest route is to start on index `1` (cost `15`) and then take a single 2-step move straight to the top, for a total of `15`.

---

### Tests

<ul>
<li id="test-1"><code>min_cost_climbing_stairs([10, 15, 20])</code> should return <code>15</code></li>
<li id="test-2"><code>min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])</code> should return <code>6</code></li>
<li id="test-3"><code>min_cost_climbing_stairs([0, 0, 0, 0])</code> should return <code>0</code></li>
<li id="test-4"><code>min_cost_climbing_stairs([1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>min_cost_climbing_stairs([5, 3, 4, 2, 6])</code> should return <code>5</code></li>
<li id="test-6"><code>min_cost_climbing_stairs([2, 5])</code> should return <code>2</code></li>
<li id="test-7">Performance: 200 stairs, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
```

**Brute force:** try every path. From each stair, recurse on both moves and take the cheaper one. That's correct, but it's `O(2^n)`: with 200 stairs it never finishes.

**Bottleneck:** the cheapest cost from a given stair is the same no matter how you got there, yet the recursion computes it again for every path that passes through.

**Optimal idea:** let `dp[i]` be the cheapest total cost to *reach* step `i`. You arrive from `i - 1` (paying `cost[i - 1]`) or from `i - 2` (paying `cost[i - 2]`), so take the cheaper. Steps `0` and `1` are free starts, and the top is step `n`.

**Why it's correct:** any route to step `i` ends with one of those two moves. The cheapest route that ends with a given move is the cheapest route to its starting stair plus that stair's cost. Taking the minimum over both covers every route.

**Complexity:** `O(n)` time. `O(n)` space for `dp`. Only `dp[i - 1]` and `dp[i - 2]` are read, so two variables would make it `O(1)`.

**Common mistakes:** returning `dp[n - 1]` and stopping one stair short of the top. Paying for the stair you land on instead of the one you leave, which charges the top (it has no cost). Setting `dp[1] = cost[0]`, which forgets that stair `1` is also a free start.

</details>
