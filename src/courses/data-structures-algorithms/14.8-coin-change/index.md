---
lesson_name: Coin Change
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
</ul>
