---
lesson_name: Kth Largest Element in a Stream
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log k) per add
  space: O(k)
hints:
  - "To know the k-th largest, which values do you need to keep, and which can you throw away for good?"
  - "Keep only the `k` largest values seen so far in a **min**-heap (*Top-k with a size-k heap* in *Heap / Priority Queue Basics*). Its root is the smallest of the top `k`, which is the k-th largest."
  - "Template: in `__init__`, `heapify` a copy of `nums` and pop while its size is over `k`. In `add`, `heappush(val)`, pop once if the size is over `k`, and return `heap[0]`."
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

### Kth Largest Element in a Stream

Design a class `KthLargest` that keeps track of the k-th largest value seen so far in a stream of integers. The constructor `KthLargest(k, nums)` is given the fixed size `k` and a starting list `nums` of values already seen. Each call to `add(val)` appends `val` to the stream and must return the current k-th largest value among everything added so far (including the starting `nums`).

For example, with `k = 2` and starting values `[3, 8]`, calling `add(5)` makes the stream `[3, 8, 5]`, whose 2nd largest value is `5`. A following `add(1)` leaves the 2nd largest unchanged at `5`, since `1` is too small to matter.

You can assume the stream holds at least `k` values whenever `add` returns.

---

### Tests

<ul>
<li id="test-1">KthLargest(2, [3, 8]), add(5) &mdash; should return <code>5</code></li>
<li id="test-2">KthLargest(2, [3, 8]), add(5), add(1) &mdash; should return <code>5</code>, then <code>5</code></li>
<li id="test-3">KthLargest(2, [3, 8]), add(5), add(10) &mdash; should return <code>5</code>, then <code>8</code></li>
<li id="test-4">KthLargest(1, []), add(4), add(2), add(9) &mdash; should return <code>4</code>, then <code>4</code>, then <code>9</code></li>
<li id="test-5">KthLargest(3, [4, 5, 8, 2]), add(3), add(10) &mdash; should return <code>4</code>, then <code>5</code></li>
<li id="test-6">KthLargest(2, [-1]), add(-1), add(-2) &mdash; should return <code>-1</code>, then <code>-1</code></li>
<li id="test-7">Performance: k = 1,000, 50,000 starting values, then 50,000 <code>add</code> calls, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

**Brute force:** keep every value in a list. On each `add`, append and return `sorted(values, reverse=True)[k - 1]`. Each call sorts the whole stream, so it's `O(n log n)` per call.

**Bottleneck:** values below the current k-th largest can never matter again, because the k-th largest only goes up. Sorting keeps them anyway.

**Optimal idea:** keep only the `k` largest values, in a min-heap. The root is the smallest of them, which is the answer. A new value goes in, and if the heap grows past `k`, the smallest is popped.

**Why it's correct:** after each `add`, the heap holds exactly the `k` largest values seen so far. A popped value had at least `k` values greater than or equal to it, so it can't be the k-th largest now or later. The root, the smallest of the top `k`, is the k-th largest.

**Complexity:** `O(log k)` per `add`: one push and at most one pop on a heap of size `k + 1`. The constructor is `O(n + (n - k) log n)`. `O(k)` space.

**Common mistakes:** using a max-heap of all values, which then needs `k` pops per call. Returning `heap[0]` before trimming the heap back to `k` values. Forgetting to trim in `__init__` when `nums` already has more than `k` values.

</details>
