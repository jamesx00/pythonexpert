---
lesson_name: Sliding Window Maximum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(k)
hints:
  - "If a newer value is at least as big as an older one in the window, can the older one ever be the maximum again?"
  - "Keep a deque of indices whose values decrease from front to back. The front is the current maximum. This is a fixed-size window (see *Sliding Window Basics*) plus a *monotonic deque*."
  - "Template: for each `i`, pop from the back while `nums[back] <= nums[i]`, append `i`, pop the front if it's left the window (`<= i - k`), and once `i >= k - 1` record `nums[front]`."
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

### Sliding Window Maximum

Given a list of integers `nums` and a window size `k`, write
`window_max(nums, k)` that slides a window of width `k` across `nums`, one
step at a time from left to right, and returns a list of the maximum value
inside the window at each position.

For example, with `nums = [4, 2, 9, 1, 6, 3]` and `k = 3`, the window starts
at `[4, 2, 9]` (max `9`), then slides to `[2, 9, 1]` (max `9`), then
`[9, 1, 6]` (max `9`), then `[1, 6, 3]` (max `6`) — so the result is
`[9, 9, 9, 6]`. You can assume `k` is at least `1` and no larger than the
length of `nums`.

---

### Tests

<ul>
<li id="test-1"><code>window_max([4, 2, 9, 1, 6, 3], 3)</code> should return <code>[9, 9, 9, 6]</code></li>
<li id="test-2"><code>window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)</code> should return <code>[3, 3, 5, 5, 6, 7]</code></li>
<li id="test-3"><code>window_max([5], 1)</code> should return <code>[5]</code></li>
<li id="test-4"><code>window_max([9, 8, 7, 6], 2)</code> should return <code>[9, 8, 7]</code></li>
<li id="test-5"><code>window_max([1, 1, 1, 1], 2)</code> should return <code>[1, 1, 1]</code></li>
<li id="test-6"><code>window_max([2, 4, 6, 8, 10], 5)</code> should return <code>[10]</code></li>
<li id="test-7"><code>window_max([-1, -3, -2, -5], 2)</code> should return <code>[-1, -2, -2]</code></li>
<li id="test-8">Performance: 100,000 values with <code>k = 50,000</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def window_max(nums, k):
    dq = deque()
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

**Brute force:** take `max(nums[i:i + k])` for every window. That's `O(n·k)`, which is `O(n²)` when `k` is about `n / 2`.

**Bottleneck:** neighbouring windows share `k - 1` values, but each maximum is recomputed from scratch.

**Optimal idea:** keep a deque of indices that could still become a window maximum. Their values decrease from front to back, so the front is always the current maximum.

**Why it's correct:** when `nums[i]` arrives, any older value that's `<=` it can never be a maximum again: `nums[i]` is at least as big and stays in the window longer. Popping those keeps the deque decreasing. The front is dropped once it falls out of the window, so it's always the largest value still inside.

**Complexity:** `O(n)` time. Each index is appended once and popped at most once. `O(k)` space for the deque.

**Common mistakes:** storing values instead of indices, which makes it impossible to tell when the front has left the window. Using a list with `pop(0)`, which is `O(k)` per pop.

</details>
