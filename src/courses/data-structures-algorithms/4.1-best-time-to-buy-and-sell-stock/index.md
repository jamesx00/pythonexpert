---
lesson_name: Best Time to Buy and Sell Stock
code_editor: True
code_execution: True
adding_file_allowed: False
section: Sliding Window
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

For example, given `[9, 2, 7, 1, 5, 3]`, buying on the day priced `1` and
selling on the day priced `5` gives a profit of `4`, which is the best you
can do. Given a list that only ever decreases, like `[8, 6, 4, 2]`, the
answer is `0` since no trade makes money.

---

### Tests

<ul>
<li id="test-1"><code>max_profit([9, 2, 7, 1, 5, 3])</code> should return <code>4</code></li>
<li id="test-2"><code>max_profit([8, 6, 4, 2])</code> should return <code>0</code></li>
<li id="test-3"><code>max_profit([1, 2, 3, 4, 5])</code> should return <code>4</code></li>
<li id="test-4"><code>max_profit([5])</code> should return <code>0</code></li>
<li id="test-5"><code>max_profit([3, 3, 3, 3])</code> should return <code>0</code></li>
<li id="test-6"><code>max_profit([2, 4, 1, 7])</code> should return <code>6</code></li>
<li id="test-7"><code>max_profit([7, 1, 5, 3, 6, 4])</code> should return <code>5</code></li>
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

</details>
