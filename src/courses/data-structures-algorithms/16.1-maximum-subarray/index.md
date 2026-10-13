---
lesson_name: Maximum Subarray
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Think about the best run that *ends* on today. Should it include the run that ended yesterday, or not?"
  - "Use *Running best (Kadane's algorithm)* from *Greedy Basics*: if the best run ending yesterday has a negative sum, it only drags today down, so start fresh at today instead."
  - "Template: `best = nums[0]`, `cur = 0`. For each `n`: `cur = max(n, cur + n)`, `best = max(best, cur)`. Return `best`."
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

### Maximum Subarray

You're given a list of integers `nums` representing the daily change in a shop's revenue over a stretch of days (positive numbers mean the shop made more than the day before, negative numbers mean it made less). Write a function `max_subarray(nums)` that returns the largest possible sum of any contiguous run of days in `nums`.

`nums` always contains at least one number and can include negative values. For example, with `nums = [3, -2, 5, -1, 4]`, the best run is the whole list, giving a sum of `9`; but with `nums = [-3, 1, -8, 4, 6]`, the best run is just `[4, 6]`, giving `10`.

---

### Tests

<ul>
<li id="test-1"><code>max_subarray([3, -2, 5, -1, 4])</code> should return <code>9</code></li>
<li id="test-2"><code>max_subarray([-3, 1, -8, 4, 6])</code> should return <code>10</code></li>
<li id="test-3"><code>max_subarray([-5])</code> should return <code>-5</code></li>
<li id="test-4"><code>max_subarray([1, 2, 3, 4])</code> should return <code>10</code></li>
<li id="test-5"><code>max_subarray([-2, -1, -3, -4])</code> should return <code>-1</code></li>
<li id="test-6"><code>max_subarray([5, 4, -1, 7, 8])</code> should return <code>23</code></li>
<li id="test-7"><code>max_subarray([0, 0, 0, 3, -1])</code> should return <code>3</code></li>
<li id="test-8">Performance: 20,000 numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_subarray(nums):
    best = nums[0]
    cur = 0  # best sum of a run that ends on the current day
    for n in nums:
        cur = max(n, cur + n)  # extend the run, or start fresh at n
        best = max(best, cur)
    return best
```

**Brute force:** try every start `i`, and keep a running sum while you extend the end `j`. That's `O(n^2)` time, `O(1)` space. Too slow for 20,000 numbers.

**Bottleneck:** each start re-adds the same numbers. Most starts are hopeless, but the brute force can't tell.

**Optimal idea:** walk the list once and keep `cur`, the best sum of a run that ends on the current day. For each new number, either extend yesterday's run (`cur + n`) or start a new run at `n`, whichever is bigger. The answer is the best `cur` seen.

**Why it's correct:** any run that ends on day `i` is either `[n]` alone or some run ending on day `i - 1` plus `n`. Among the second kind, the biggest one uses the best run ending on day `i - 1`, which is `cur`. So `max(n, cur + n)` really is the best run ending on day `i`. Put the greedy way: if `cur` is negative, keeping it can only lower today's sum, so dropping it is always safe. Every run ends on some day, so the max over all days is the answer.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** starting `best` at `0`, which returns `0` instead of `-1` when every number is negative. Resetting `cur` to `0` *before* updating `best`, which has the same problem. Looping over `nums[1:]`, which works but copies the list.

</details>
