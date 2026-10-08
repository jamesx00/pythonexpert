---
lesson_name: "Warm-up: Max Sum Subarray of Size K"
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

### Warm-up: Max Sum Subarray of Size K

Write a function `max_sum_k(nums, k)` that returns the largest sum of any **contiguous** run of exactly `k` numbers in `nums`. You can assume `1 <= k <= len(nums)`.

For example, `max_sum_k([2, 1, 5, 1, 3, 2], 3)` returns `9`, from `[5, 1, 3]`.

**Hint:** this is the fixed-size sliding window. Compute the sum of the first `k` numbers once. Then, each time the window slides one step right, add the number that enters and subtract the number that leaves, instead of re-summing the whole window.

---

### Tests

<ul>
<li id="test-1"><code>max_sum_k([2, 1, 5, 1, 3, 2], 3)</code> should return <code>9</code></li>
<li id="test-2"><code>max_sum_k([1, 2, 3], 3)</code> should return <code>6</code></li>
<li id="test-3"><code>max_sum_k([5], 1)</code> should return <code>5</code></li>
<li id="test-4"><code>max_sum_k([-1, -2, -3, -4], 2)</code> should return <code>-3</code></li>
<li id="test-5"><code>max_sum_k([1, 9, -1, -2, 7, 3, -1, 2], 4)</code> should return <code>13</code></li>
<li id="test-6"><code>max_sum_k([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3)</code> should return <code>16</code></li>
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

When `right` enters the window, `nums[right - k]` is the element that just fell out the left side. Updating the running sum costs `O(1)`, so the whole scan is `O(n)` instead of `O(n·k)`.

</details>
