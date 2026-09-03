---
lesson_name: Maximum Product Subarray
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
</ul>
