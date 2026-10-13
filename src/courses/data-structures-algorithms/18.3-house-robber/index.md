---
lesson_name: House Robber
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Look at the last house. You either rob it or you don't. What's the best total in each case?"
  - "Skip it: the best for the houses before it. Rob it: its cash plus the best for the houses two back. So `dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])`, the example in *The Recipe* in *1-D Dynamic Programming Basics*."
  - "Template: `prev, curr = 0, 0`. For each `h`: `prev, curr = curr, max(curr, prev + h)`. Return `curr`."
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

### House Robber

Write a function `rob(houses)` that takes a list of non-negative integers, where each value is the amount of cash stored in that house along a street. Return the maximum total amount you can steal, given that robbing two adjacent houses (indices that differ by 1) trips the alarm, so you may never pick two neighboring houses in the same night.

For example, given `houses = [2, 7, 9, 3, 1]`, the best plan is to rob house `0` (2), house `2` (9), and house `4` (1), for a total of `12`.

---

### Tests

<ul>
<li id="test-1"><code>rob([2, 7, 9, 3, 1])</code> should return <code>12</code></li>
<li id="test-2"><code>rob([1, 2, 3, 1])</code> should return <code>4</code></li>
<li id="test-3"><code>rob([2, 1, 1, 2])</code> should return <code>4</code></li>
<li id="test-4"><code>rob([5])</code> should return <code>5</code></li>
<li id="test-5"><code>rob([5, 1])</code> should return <code>5</code></li>
<li id="test-6"><code>rob([0, 0, 0])</code> should return <code>0</code></li>
<li id="test-7"><code>rob([4, 1, 2, 7, 5, 3, 1])</code> should return <code>14</code></li>
<li id="test-8">Performance: 200 houses, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def rob(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr
```

**Brute force:** for each house, try both robbing it (and skipping the next) and skipping it, and keep the better total. That's `O(2^n)` with no memo, far too slow for 200 houses.

**Bottleneck:** "the best total from house `i` onward" is asked again and again by different paths through the recursion.

**Optimal idea:** scan left to right. `curr` is the best total for the houses seen so far, and `prev` the best one house earlier. For a new house `h`, either skip it (`curr`) or rob it (`prev + h`, since the house before must be skipped).

**Why it's correct:** any plan for the first `i` houses either leaves house `i` alone, so it's a plan for the first `i - 1` houses, or robs it, so house `i - 1` is skipped and the rest is a plan for the first `i - 2` houses. The best of those two options is the best plan overall.

**Complexity:** `O(n)` time. `O(1)` extra space.

**Common mistakes:** summing the even-indexed or odd-indexed houses: `[2, 1, 1, 2]` is best robbed at both ends, `4`. Updating `prev` and `curr` on two separate lines so one uses the other's new value. Special-casing a list of length 1 or 2 when the loop already handles them.

</details>
