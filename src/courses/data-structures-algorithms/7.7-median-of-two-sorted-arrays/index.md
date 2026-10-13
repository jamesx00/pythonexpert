---
lesson_name: Median of Two Sorted Arrays
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(log(min(m, n)))
  space: O(1)
hints:
  - "The median splits the combined values into a left half and a right half of equal size. If you knew how many values the left half takes from the first list, how many would it take from the second?"
  - "If the left half takes `i` values from `a`, it takes `half - i` from `b`. The split is right when `a[i - 1] <= b[j]` and `b[j - 1] <= a[i]`. Binary search on `i` over the shorter list (see *Binary Search Basics*)."
  - "Template: `i` in `0..m`, `j = (m + n + 1) // 2 - i`. Use `-inf`/`inf` for out-of-range neighbours. If `a[i - 1] > b[j]`, move `i` left, if `b[j - 1] > a[i]`, move it right. Otherwise the median comes from `max(a_left, b_left)` and `min(a_right, b_right)`."
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
<li id="test-8">Performance: 2,000 calls on two 100,000-element lists, within 1 second</li>
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

**Brute force:** merge the two lists (or `sorted(nums1 + nums2)`) and take the middle. That's `O(m + n)` with a merge, or `O((m + n) log(m + n))` with a sort.

**Bottleneck:** the median only depends on where the halves split, but merging builds the whole combined list.

**Optimal idea:** choose how many values `i` the left half takes from the shorter list `a`. The rest of the left half, `j = half - i`, comes from `b`. Binary search `i` until every value on the left is `<=` every value on the right.

**Why it's correct:** both lists are sorted, so the left half is valid exactly when `a[i - 1] <= b[j]` and `b[j - 1] <= a[i]`. If `a[i - 1] > b[j]`, `a` gave too many values to the left, so `i` must shrink, and if `b[j - 1] > a[i]`, `i` must grow. At most one of the two conditions fails at a time, and it says which way to move, so binary search finds the valid split. The median is then the largest left value (odd total) or the average of the largest left and smallest right values (even total).

**Complexity:** `O(log(min(m, n)))` time, because the search runs over the shorter list. `O(1)` extra space.

**Common mistakes:** searching over the longer list, which can make `j` negative. Forgetting the `-inf`/`inf` sentinels when `i` or `j` is at either end. Returning an `int` instead of a `float` for an odd total.

</details>
