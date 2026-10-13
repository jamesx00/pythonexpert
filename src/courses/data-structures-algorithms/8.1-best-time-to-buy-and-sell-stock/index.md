---
lesson_name: Best Time to Buy and Sell Stock
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If you had to sell on a particular day, which earlier day would you want to have bought on?"
  - "The best buy day for a sale on day `i` is the cheapest price *before* `i`. Keep that running minimum as you scan, which works like a window whose left edge jumps to each new low (see *Sliding Window Basics*)."
  - "Template: track `min_price` and `best`. For each price, update `best` with `price - min_price`, then update `min_price` if this price is lower."
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

### Best Time to Buy and Sell Stock

You're given a list of integers `prices`, where `prices[i]` is the price of a
single share of a stock on day `i`. You may buy the share on exactly one day
and sell it on a later day, and you're only allowed to hold one share at a
time — so you must buy before you sell. Write `max_profit(prices)` that
returns the largest profit you could have made, or `0` if no profitable
trade was possible.

For example, given `[9, 2, 7, 1, 5, 3]`, buying on the day priced `2` and
selling on the day priced `7` gives a profit of `5`, which is the best you
can do. Buying at the lowest price, `1`, only leads to a profit of `4`. Given a list that only ever decreases, like `[8, 6, 4, 2]`, the
answer is `0` since no trade makes money.

---

### Tests

<ul>
<li id="test-1"><code>max_profit([9, 2, 7, 1, 5, 3])</code> should return <code>5</code></li>
<li id="test-2"><code>max_profit([8, 6, 4, 2])</code> should return <code>0</code></li>
<li id="test-3"><code>max_profit([1, 2, 3, 4, 5])</code> should return <code>4</code></li>
<li id="test-4"><code>max_profit([5])</code> should return <code>0</code></li>
<li id="test-5"><code>max_profit([3, 3, 3, 3])</code> should return <code>0</code></li>
<li id="test-6"><code>max_profit([2, 4, 1, 7])</code> should return <code>6</code></li>
<li id="test-7"><code>max_profit([7, 1, 5, 3, 6, 4])</code> should return <code>5</code></li>
<li id="test-8">Performance: 100,000 falling prices, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for p in prices[1:]:
        if p - min_price > best:
            best = p - min_price
        if p < min_price:
            min_price = p
    return best
```

**Brute force:** try every buy day with every later sell day. That's `O(n²)` time.

**Bottleneck:** for each sell day, the inner loop searches all earlier days for the cheapest price, although that minimum only changes when a new low appears.

**Optimal idea:** scan once, keeping the lowest price seen so far. Each day's best profit is today's price minus that minimum.

**Why it's correct:** the best trade that sells on day `i` buys at the lowest price before day `i`, which is exactly `min_price` when day `i` is processed. Taking the maximum over every sell day covers every possible trade. `best` starts at `0`, so a falling market returns `0`.

**Complexity:** `O(n)` time for one pass. `O(1)` extra space.

**Common mistakes:** buying at the overall lowest price. In `[9, 2, 7, 1, 5, 3]` the lowest price is `1`, but the best trade is buying at `2` and selling at `7`. Updating `min_price` before computing the profit is fine, since it only allows a profit of `0`.

</details>
