---
lesson_name: Maximum Product Subarray
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "With sums, a bad prefix is just dropped. With products, a very negative running product can become the best one after another negative. What do you need to remember besides the largest product?"
  - "Track both the largest and the smallest product of a subarray ending at the current position (the *Track min and max* shape in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*). The new value is one of `n`, `cur_max * n` or `cur_min * n`."
  - "Template: start `res = cur_max = cur_min = nums[0]`. For each later `n`: `candidates = (n, cur_max * n, cur_min * n)`, `cur_max = max(candidates)`, `cur_min = min(candidates)`, `res = max(res, cur_max)`."
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

### Maximum Product Subarray

Write a function `max_product_subarray(nums)` that takes a non-empty list of integers and returns the largest product achievable by multiplying together every element of some contiguous subarray (a run of at least one adjacent element). Negative numbers may flip a very negative running product into the largest one, so track that possibility.

For example, given `nums = [2, 3, -2, 4]`, the best contiguous run is `[2, 3]`, whose product is `6`; including the `-2` or the `4` only lowers the result.

---

### Tests

<ul>
<li id="test-1"><code>max_product_subarray([2, 3, -2, 4])</code> should return <code>6</code></li>
<li id="test-2"><code>max_product_subarray([-2, 0, -1])</code> should return <code>0</code></li>
<li id="test-3"><code>max_product_subarray([-2, 3, -4])</code> should return <code>24</code></li>
<li id="test-4"><code>max_product_subarray([5])</code> should return <code>5</code></li>
<li id="test-5"><code>max_product_subarray([-3])</code> should return <code>-3</code></li>
<li id="test-6"><code>max_product_subarray([2, -5, -2, -4, 3])</code> should return <code>24</code></li>
<li id="test-7"><code>max_product_subarray([0, 2, -3, 4, -1, 0])</code> should return <code>24</code></li>
<li id="test-8">Performance: 10,000 numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_product_subarray(nums):
    res = nums[0]
    cur_max = cur_min = nums[0]
    for n in nums[1:]:
        candidates = (n, cur_max * n, cur_min * n)
        cur_max = max(candidates)
        cur_min = min(candidates)
        res = max(res, cur_max)
    return res
```

**Brute force:** for each start `i`, multiply forward to every end `j` and keep the largest product. That's `O(n^2)`: 50 million steps for 10,000 numbers.

**Bottleneck:** the products of subarrays ending at `j` can be built from those ending at `j - 1`, but only if you know the right ones to extend.

**Optimal idea:** for each position, keep the largest and the smallest product of a subarray ending there. A new number `n` either starts fresh, extends the largest, or extends the smallest. When `n` is negative, the smallest (most negative) product times `n` becomes the largest.

**Why it's correct:** a subarray ending at `j` is either `[nums[j]]` or a subarray ending at `j - 1` extended by `nums[j]`. Multiplying by `nums[j]` keeps the order of products when it's positive and reverses it when it's negative. So the best and worst products ending at `j` always come from the best or worst ending at `j - 1`, or from `nums[j]` alone. A `0` resets both to `0`, and the next number starts fresh.

**Complexity:** `O(n)` time. `O(1)` extra space.

**Common mistakes:** tracking only the maximum, which fails on `[-2, 3, -4]` (the answer `24` needs the `-6`). Updating `cur_max` first and then using the *new* value to compute `cur_min`: compute the candidates once. Starting `res` at `0`, which is wrong for `[-3]`.

</details>
