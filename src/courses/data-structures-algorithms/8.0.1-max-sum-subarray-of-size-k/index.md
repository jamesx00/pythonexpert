---
lesson_name: "Warm-up: Max Sum Subarray of Size K"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "When the window slides one step right, how many numbers actually change?"
  - "Use a fixed-size window (the *Fixed size `k`* block in *Sliding Window Basics*): sum the first `k` numbers once, then for each step add the number entering on the right and subtract the one leaving on the left."
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

### Warm-up: Max Sum Subarray of Size K

Write a function `max_sum_k(nums, k)` that returns the largest sum of any **contiguous** run of exactly `k` numbers in `nums`. You can assume `1 <= k <= len(nums)`.

For example, `max_sum_k([2, 1, 5, 1, 3, 2], 3)` returns `9`, from `[5, 1, 3]`.

---

### Tests

<ul>
<li id="test-1"><code>max_sum_k([2, 1, 5, 1, 3, 2], 3)</code> should return <code>9</code></li>
<li id="test-2"><code>max_sum_k([1, 2, 3], 3)</code> should return <code>6</code></li>
<li id="test-3"><code>max_sum_k([5], 1)</code> should return <code>5</code></li>
<li id="test-4"><code>max_sum_k([-1, -2, -3, -4], 2)</code> should return <code>-3</code></li>
<li id="test-5"><code>max_sum_k([1, 9, -1, -2, 7, 3, -1, 2], 4)</code> should return <code>13</code></li>
<li id="test-6"><code>max_sum_k([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3)</code> should return <code>16</code></li>
<li id="test-7">Performance: 100,000 values with <code>k = 50,000</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best
```

**Brute force:** sum every window with `sum(nums[i:i + k])`. There are `n - k + 1` windows of `k` numbers each, so this is `O(n·k)`, which is `O(n²)` when `k` is about `n / 2`.

**Bottleneck:** neighbouring windows share `k - 1` numbers, but each sum starts from scratch.

**Optimal idea:** keep a running window sum. Each slide adds `nums[right]` and subtracts `nums[right - k]`.

**Why it's correct:** the window ending at `right` is the previous window plus `nums[right]` minus `nums[right - k]`, so the running sum always equals the current window's sum, and every window is compared with `best`.

**Complexity:** `O(n)` time: `O(k)` for the first sum and `O(1)` per slide. `O(1)` extra space.

**Common mistakes:** starting `best` at `0`, which is wrong when every number is negative, as in `[-1, -2, -3, -4]`. Start it at the first window's sum.

</details>
