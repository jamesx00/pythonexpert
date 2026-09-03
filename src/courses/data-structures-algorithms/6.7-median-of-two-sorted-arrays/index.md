---
lesson_name: Median of Two Sorted Arrays
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

### Median of Two Sorted Arrays

You're given two lists of integers, each already sorted in ascending order, possibly of different lengths. Write a function that returns the median of all the values from both lists combined, as a `float`. If you merged the two lists into one sorted list of length `n`, the median is the middle element when `n` is odd, or the average of the two middle elements when `n` is even.

Merging both lists and sorting takes `O((m + n) log(m + n))` time — this problem asks for an `O(log(min(m, n)))` solution, found by binary searching over how the shorter array should be split.

For example, with `[1, 3]` and `[2]`, the merged order is `[1, 2, 3]`, so the median is `2.0`. With `[1, 2]` and `[3, 4]`, the merged order is `[1, 2, 3, 4]`, so the median is the average of `2` and `3`, which is `2.5`.

---

### Tests

<ul>
<li id="test-1"><code>find_median_sorted_arrays([1, 3], [2])</code> should return <code>2.0</code></li>
<li id="test-2"><code>find_median_sorted_arrays([1, 2], [3, 4])</code> should return <code>2.5</code></li>
<li id="test-3"><code>find_median_sorted_arrays([], [1])</code> should return <code>1.0</code></li>
<li id="test-4"><code>find_median_sorted_arrays([2], [])</code> should return <code>2.0</code></li>
<li id="test-5"><code>find_median_sorted_arrays([1, 2, 3], [4, 5, 6, 7])</code> should return <code>4.0</code></li>
<li id="test-6"><code>find_median_sorted_arrays([-5, -3, -1], [-4, -2])</code> should return <code>-3.0</code></li>
<li id="test-7"><code>find_median_sorted_arrays([1, 1, 1], [1, 1])</code> should return <code>1.0</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_median_sorted_arrays(nums1, nums2):
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    lo, hi = 0, m
    half = (m + n + 1) // 2
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
```

</details>
