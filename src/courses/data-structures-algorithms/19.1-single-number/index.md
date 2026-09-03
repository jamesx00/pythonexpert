---
lesson_name: Single Number
section: Bit Manipulation
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

### Single Number

Write a function `single_number(nums)` that takes a list of integers where every value appears exactly twice except for one value that appears only once, and returns that lone value. Your solution should run in linear time while using only constant extra space, so sorting or building a frequency map with an extra structure defeats the point of the exercise.

A useful trick: XOR-ing a number with itself always produces `0`, and XOR-ing any number with `0` returns that number unchanged. XOR is also commutative and associative, so the order of the values in the list doesn't matter.

For example, given `nums = [4, 1, 2, 1, 2]`, the values `1` and `2` each appear twice, leaving `4` as the single number, so the function should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>single_number([4, 1, 2, 1, 2])</code> should return <code>4</code></li>
<li id="test-2"><code>single_number([1])</code> should return <code>1</code></li>
<li id="test-3"><code>single_number([2, 2, 1])</code> should return <code>1</code></li>
<li id="test-4"><code>single_number([7, 3, 5, 4, 5, 3, 4])</code> should return <code>7</code></li>
<li id="test-5"><code>single_number([-1, -1, -2])</code> should return <code>-2</code></li>
<li id="test-6"><code>single_number([0, 1, 0])</code> should return <code>1</code></li>
<li id="test-7"><code>single_number([9, 5, 9])</code> should return <code>5</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
```

</details>
