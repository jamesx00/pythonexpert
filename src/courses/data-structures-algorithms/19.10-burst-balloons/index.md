---
lesson_name: Burst Balloons
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

</details>
