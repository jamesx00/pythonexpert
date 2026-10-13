---
lesson_name: Top K Frequent Elements
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log k)
  space: O(n)
hints:
  - "Before you can pick the most frequent values, what do you need to know about every value?"
  - "Count every value once with a dictionary or `collections.Counter` (the *Counting* block in *Arrays & Hashing Basics*). Then you only need the `k` largest counts."
  - "Template: `Counter(nums).most_common(k)` returns `(value, count)` pairs, most frequent first. Keep just the values."
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

### Top K Frequent Elements

Write a function `top_k_frequent(nums, k)` that takes a list of integers and an integer `k`, and returns a list of the `k` values that occur most often in `nums`. You may assume there is always a unique answer (no ties at the cutoff), and the order of the returned values does not matter.

For example, given `nums = [5, 5, 5, 1, 1, 9]` and `k = 2`, the value `5` appears three times and `1` appears twice, more often than `9`, so `top_k_frequent(nums, k)` should return `[5, 1]` (in either order).

---

### Tests

<ul>
<li id="test-1"><code>top_k_frequent([5, 5, 5, 1, 1, 9], 2)</code> should return <code>[5, 1]</code> (order does not matter)</li>
<li id="test-2"><code>top_k_frequent([1, 2, 2, 3, 3, 3], 1)</code> should return <code>[3]</code></li>
<li id="test-3"><code>top_k_frequent([4], 1)</code> should return <code>[4]</code></li>
<li id="test-4"><code>top_k_frequent([7, 7, 8, 8, 9, 9], 3)</code> should return <code>[7, 8, 9]</code> (order does not matter)</li>
<li id="test-5"><code>top_k_frequent([1, 1, 1, 2, 2, 3], 2)</code> should return <code>[1, 2]</code> (order does not matter)</li>
<li id="test-6"><code>top_k_frequent([-1, -1, 2, 3, 3], 2)</code> should return <code>[-1, 3]</code> (order does not matter)</li>
<li id="test-7">Performance: 100,000 values, 50,000 of them distinct, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    most_common = counts.most_common(k)
    return [n for n, _ in most_common]
```

**Brute force:** for each distinct value, call `nums.count(value)`, then sort by count. Each `count` scans the whole list, so this is `O(n·d)` for `d` distinct values, up to `O(n²)`.

**Bottleneck:** the list is rescanned once per distinct value, although one pass can count everything.

**Optimal idea:** count every value in one pass, then pick the `k` largest counts. `Counter.most_common(k)` does the picking with a heap of size `k`.

**Why it's correct:** after counting, each value's count is exact, and the problem guarantees no ties at the cutoff, so the `k` largest counts identify exactly one answer.

**Complexity:** `O(n)` to count, plus `O(d log k)` to pick the top `k` of `d` distinct values with a heap, so `O(n log k)` overall. `O(n)` space for the counts. Sorting all counts instead is `O(n log n)`. For a strict `O(n)`, use *bucket sort*: make a list of `n + 1` buckets where bucket `c` holds the values that appear `c` times, then read buckets from the highest down until you have `k` values.

**Common mistakes:** returning the counts instead of the values, or returning `(value, count)` pairs straight from `most_common`.

</details>
