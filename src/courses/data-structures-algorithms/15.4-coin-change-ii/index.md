---
lesson_name: Coin Change II
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
</ul>
