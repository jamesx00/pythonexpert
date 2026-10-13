---
lesson_name: Missing Number
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If every value `0..n` were present, you could pair each value with an index. Which one has no partner?"
  - "Use *XOR cancels pairs* from *Bit Manipulation Basics*: XOR together all the indices `0..n` and all the values in `nums`. Every present value cancels with its matching index, and only the missing one is left."
  - "Template: `result = len(nums)`. For each `i`: `result ^= i ^ nums[i]`. Return `result`."
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

### Missing Number

Write a function `missing_number(nums)` that takes a list of `n` distinct integers drawn from the range `0` to `n` inclusive, with exactly one value from that range left out, and returns the missing value.

Try to solve it in linear time with only constant extra space.

For example, given `nums = [3, 0, 1]`, the list has length `3`, so the full range is `0` to `3`. The values `0`, `1`, and `3` are present but `2` is not, so the function should return `2`.

---

### Tests

<ul>
<li id="test-1"><code>missing_number([3, 0, 1])</code> should return <code>2</code></li>
<li id="test-2"><code>missing_number([0, 1])</code> should return <code>2</code></li>
<li id="test-3"><code>missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])</code> should return <code>8</code></li>
<li id="test-4"><code>missing_number([0])</code> should return <code>1</code></li>
<li id="test-5"><code>missing_number([1])</code> should return <code>0</code></li>
<li id="test-6"><code>missing_number([1, 2])</code> should return <code>0</code></li>
<li id="test-7"><code>missing_number([5, 3, 0, 1, 4])</code> should return <code>2</code></li>
<li id="test-8">Performance: 50,000 numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def missing_number(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result
```

**Brute force:** for each candidate `x` from `0` to `n`, check `x not in nums` and return the first one that's missing. Each `in` scans the list, so this is `O(n^2)` time. Too slow for 50,000 numbers. Sorting first is `O(n log n)`, and a set makes it `O(n)` time but `O(n)` extra space.

**Bottleneck:** each check searches the whole list again to match a value with its candidate.

**Optimal idea:** XOR every index `0..n - 1`, the extra endpoint `n`, and every value in `nums` together. Every value that's present appears twice, once as an index and once as a value, so it cancels. Only the missing value appears once.

**Why it's correct:** the indices plus `n` are exactly `0..n`, each once. The values are `0..n` with one missing. Together, every value in `0..n` appears twice except the missing one, which appears once. XOR cancels pairs in any order, so the result is the missing value. Starting `result` at `n` adds the endpoint, which has no index of its own.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** starting `result` at `0` instead of `n`, which fails when `n` itself is missing, as in `[0, 1]`. The sum formula `n * (n + 1) // 2 - sum(nums)` is also `O(n)` and `O(1)` in Python, but in languages with fixed-width integers the sum can overflow, which XOR never does.

</details>
