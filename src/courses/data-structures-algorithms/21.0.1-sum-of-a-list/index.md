---
lesson_name: "Warm-up: Sum of a List"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "What's the sum of an empty list? And if you already knew the sum of everything after the first element, how would you get the sum of the whole list?"
  - "Use the *Shrink by one* shape from *Recursion Basics*: base case `[]` → `0`, recursive case `nums[0]` + the sum of the rest. To avoid copying a slice on every call, pass an index instead: `def sum_list(nums, i=0)`, with the base case `i == len(nums)`."
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

### Warm-up: Sum of a List

Write a **recursive** function `sum_list(nums)` that returns the sum of the numbers in `nums`. The sum of an empty list is `0`.

Don't use `sum()` or a loop: `sum_list` must call itself. You may add a parameter with a default value, such as `def sum_list(nums, i=0)`, as long as `sum_list(nums)` still works.

---

### Tests

<ul>
<li id="test-1"><code>sum_list([])</code> should return <code>0</code></li>
<li id="test-2"><code>sum_list([5])</code> should return <code>5</code></li>
<li id="test-3"><code>sum_list([1, 2, 3, 4])</code> should return <code>10</code></li>
<li id="test-4"><code>sum_list([-3, 7, -1])</code> should return <code>3</code></li>
<li id="test-5"><code>sum_list([0, 0, 0])</code> should return <code>0</code></li>
<li id="test-6"><code>sum_list(list(range(500)))</code> should return <code>124750</code></li>
<li id="test-7"><code>sum_list([1, 2, 3])</code> calls itself</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def sum_list(nums, i=0):
    if i == len(nums):
        return 0
    return nums[i] + sum_list(nums, i + 1)
```

**Brute force:** the textbook version, `return nums[0] + sum_list(nums[1:])`, is correct. But each call copies the rest of the list with a slice, so the calls copy `n - 1`, `n - 2`, …, `0` items: `O(n²)` time.

**Bottleneck:** the slice. The recursive call only needs to know *where* the rest of the list starts, not a fresh copy of it.

**Optimal idea:** pass an index `i` meaning "sum everything from position `i` onwards". The base case is `i == len(nums)` (nothing left, sum `0`), and the recursive case adds `nums[i]` to the sum from `i + 1`.

**Why it's correct:** trust the recursion. If `sum_list(nums, i + 1)` correctly sums `nums[i + 1:]`, then adding `nums[i]` gives the sum of `nums[i:]`. Every call moves `i` one step closer to `len(nums)`, so the base case is always reached, and `sum_list(nums)` (with `i = 0`) sums the whole list.

**Complexity:** `n + 1` calls doing `O(1)` work each, so `O(n)` time. The call stack is `n + 1` frames deep, so `O(n)` space. That depth is also why recursion isn't the right tool for very long lists in Python: past about 1,000 elements you'll hit `RecursionError`.

**Common mistakes:** forgetting the base case, or writing it as `len(nums) == 1` (then `sum_list([])` crashes). Calling `sum_list(nums, i + 1)` without returning or using its value. Using a mutable running total as a default argument (`total=[]`), which keeps its value between separate calls.

</details>
