---
lesson_name: "Warm-up: K Smallest Numbers"
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

### Warm-up: K Smallest Numbers

Write a function `k_smallest(nums, k)` that returns the `k` smallest numbers in `nums` as a list sorted in **ascending** order. You can assume `0 <= k <= len(nums)`.

For example, `k_smallest([5, 1, 4, 2, 3], 2)` returns `[1, 2]`.

Use the `heapq` module and practise the core operations: `heapify` turns the list into a min-heap in `O(n)`, and each `heappop` removes and returns the current smallest in `O(log n)`.

**Hint:** copy the list, `heapify` it, then pop `k` times.

---

### Tests

<ul>
<li id="test-1"><code>k_smallest([5, 1, 4, 2, 3], 2)</code> should return <code>[1, 2]</code></li>
<li id="test-2"><code>k_smallest([7, 7, 7], 2)</code> should return <code>[7, 7]</code></li>
<li id="test-3"><code>k_smallest([3, -1, 2], 3)</code> should return <code>[-1, 2, 3]</code></li>
<li id="test-4"><code>k_smallest([1, 2, 3], 0)</code> should return <code>[]</code></li>
<li id="test-5"><code>k_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4)</code> should return <code>[1, 2, 3, 4]</code></li>
<li id="test-6"><code>k_smallest([4], 1)</code> should return <code>[4]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq

def k_smallest(nums, k):
    heap = list(nums)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(k)]
```

`heapify` costs `O(n)` and each of the `k` pops costs `O(log n)`, for `O(n + k log n)` total. Copying first (`list(nums)`) avoids scrambling the caller's list, because `heapify` works in place. When the input is a stream too big to hold, use the other approach from the basics lesson instead: a size-`k` **max**-heap (negated values).

</details>
