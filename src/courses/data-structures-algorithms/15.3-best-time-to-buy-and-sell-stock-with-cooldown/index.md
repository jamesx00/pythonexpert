---
lesson_name: Best Time to Buy and Sell Stock with Cooldown
code_editor: True
code_execution: True
adding_file_allowed: False
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

For example, with `prices = [1, 2, 3, 0, 2]` the best plan is to buy on day 0 at `1`, sell on day 2 at `3` for a profit of `2`, then (after skipping the cooldown day) buy again on day 3 at `0` and sell on day 4 at `2` for a profit of `2` — but the second buy is only legal one day after the first sale, so the actual best achievable total is `3`, meaning `max_profit([1, 2, 3, 0, 2])` returns `3`.

---

### Tests

<ul>
<li id="test-1"><code>max_profit([1, 3, 2, 8, 4, 9])</code> should return <code>8</code></li>
<li id="test-2"><code>max_profit([1, 2, 3, 0, 2])</code> should return <code>3</code></li>
<li id="test-3"><code>max_profit([1])</code> should return <code>0</code></li>
<li id="test-4"><code>max_profit([])</code> should return <code>0</code></li>
<li id="test-5"><code>max_profit([5, 4, 3, 2, 1])</code> should return <code>0</code></li>
<li id="test-6"><code>max_profit([2, 1, 4, 5, 2, 9, 7])</code> should return <code>10</code></li>
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

</details>
