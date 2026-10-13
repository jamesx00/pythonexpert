---
lesson_name: Best Time to Buy and Sell Stock with Cooldown
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "At the end of each day you're in one of three situations: holding a share, having just sold today, or resting with no share. Which of these can each situation turn into the next day?"
  - "Keep the best profit for each state on each day. `hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])` (keep holding, or buy after resting). `sold[i] = hold[i - 1] + prices[i]`. `rest[i] = max(rest[i - 1], sold[i - 1])`, since the day after a sale is a forced rest. The state flag is the second dimension, as in *Spotting It* in *2-D Dynamic Programming Basics*."
  - "Template: return `0` for an empty list. Set `hold = -prices[0]`, `sold = rest = 0`. For each later price `p`: compute the three new values from the old ones at the same time. Return `max(sold, rest)`."
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

### Best Time to Buy and Sell Stock with Cooldown

You are given a list `prices` where `prices[i]` is the price of a stock on day `i`. You may complete as many buy/sell transactions as you like, one share at a time, but after selling you must wait one full day (a cooldown) before you can buy again, and you cannot hold more than one share at once. Write a function `max_profit(prices)` that returns the maximum total profit achievable.

For example, with `prices = [1, 2, 3, 0, 2]` the best plan is to buy on day 0 at `1` and sell on day 1 at `2`, rest on day 2 (the cooldown), then buy on day 3 at `0` and sell on day 4 at `2`. That's a profit of `1 + 2 = 3`, so `max_profit([1, 2, 3, 0, 2])` returns `3`. Selling on day 2 at `3` instead would put the cooldown on day 3, the cheapest day.

---

### Tests

<ul>
<li id="test-1"><code>max_profit([1, 3, 2, 8, 4, 9])</code> should return <code>8</code></li>
<li id="test-2"><code>max_profit([1, 2, 3, 0, 2])</code> should return <code>3</code></li>
<li id="test-3"><code>max_profit([1])</code> should return <code>0</code></li>
<li id="test-4"><code>max_profit([])</code> should return <code>0</code></li>
<li id="test-5"><code>max_profit([5, 4, 3, 2, 1])</code> should return <code>0</code></li>
<li id="test-6"><code>max_profit([2, 1, 4, 5, 2, 9, 7])</code> should return <code>10</code></li>
<li id="test-7">Performance: 250 days of prices, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_profit(prices):
    if not prices:
        return 0
    n = len(prices)
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n
    hold[0] = -prices[0]
    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])
    return max(sold[-1], rest[-1])
```

**Brute force:** recurse over the days, carrying whether you hold a share. Each day you either do nothing or make the one allowed move (buy, or sell and skip the next day). Without a memo that's two choices per day, so about `2^n` plans. 250 days never finish.

**Bottleneck:** the future only depends on the day and on whether you hold a share, not on how you got there. The brute force solves the same `(day, holding)` question many times.

**Optimal idea:** track three states at the end of each day: `hold` (you own a share), `sold` (you sold today) and `rest` (no share, free to buy tomorrow). Keep the best profit for each state, day by day. That's a table with `n` rows and 3 columns.

**Why it's correct:** the transitions list every legal move. You end a day holding if you held yesterday, or rested yesterday and buy today; you can't buy the day after selling, because `sold` doesn't lead to `hold`. You've sold today only if you held yesterday. You rest if you rested or sold yesterday. Taking the best of each option keeps the best profit for every state. At the end, holding a share is never best, so the answer is `max(sold, rest)`.

**Complexity:** `O(n)` time: constant work per day. `O(n)` space for the three lists, or `O(1)` with three variables, since each day only reads the day before.

**Common mistakes:** letting `hold` come from `sold[i - 1]`, which buys the day after a sale. Updating three variables one at a time so a new value is read by the next line; compute all three from the old ones. Forgetting the empty list. Starting `hold` at `0` instead of `-prices[0]`.

</details>
