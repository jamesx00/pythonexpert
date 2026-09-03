---
lesson_name: Missing Number
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

### Missing Number

Write a function `missing_number(nums)` that takes a list of `n` distinct integers drawn from the range `0` to `n` inclusive, with exactly one value from that range left out, and returns the missing value.

A neat way to solve this without extra space is with XOR: XOR every index `0..n-1` together with every value in `nums`, plus the extra endpoint `n`. Every number that actually appears in `nums` gets XOR-ed with its matching index and cancels out to `0`, leaving only the one value that was never paired up — the missing number.

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

</details>
