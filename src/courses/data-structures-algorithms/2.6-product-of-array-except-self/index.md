---
lesson_name: Product of Array Except Self
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

### Product of Array Except Self

Write a function `product_except_self(nums)` that takes a list of integers and returns a new list `output` where `output[i]` is the product of every value in `nums` except `nums[i]`. You must not use division anywhere in your solution.

For example, given `nums = [2, 3, 4, 5]`, the value at index `0` should be `3 * 4 * 5 = 60`, the value at index `1` should be `2 * 4 * 5 = 40`, and so on, so `product_except_self(nums)` should return `[60, 40, 30, 24]`.

---

### Tests

<ul>
<li id="test-1"><code>product_except_self([2, 3, 4, 5])</code> should return <code>[60, 40, 30, 24]</code></li>
<li id="test-2"><code>product_except_self([1, 1, 1, 1])</code> should return <code>[1, 1, 1, 1]</code></li>
<li id="test-3"><code>product_except_self([1, 2])</code> should return <code>[2, 1]</code></li>
<li id="test-4"><code>product_except_self([-1, 2, -3])</code> should return <code>[-6, 3, -2]</code></li>
<li id="test-5"><code>product_except_self([0, 4, 5])</code> should return <code>[20, 0, 0]</code></li>
<li id="test-6"><code>product_except_self([3, 0, 0, 6])</code> should return <code>[0, 0, 0, 0]</code></li>
</ul>
