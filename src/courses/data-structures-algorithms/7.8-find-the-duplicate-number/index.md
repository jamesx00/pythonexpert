---
lesson_name: Find the Duplicate Number
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

### Find the Duplicate Number

Write a function `find_duplicate(nums)` that takes a list of `n + 1` integers where every value is between `1` and `n` inclusive, and exactly one value appears more than once (though it may appear more than twice). Return that repeated value. You may not modify the input list, and you should use only constant extra space - treat the list like a linked list where each index points to the index named by its value, and detect the cycle that forms.

For example, `find_duplicate([1, 3, 4, 2, 2])` should return `2`, since every other value from `1` to `4` appears exactly once.

---

### Tests

<ul>
<li id="test-1"><code>find_duplicate([1, 3, 4, 2, 2])</code> should return <code>2</code></li>
<li id="test-2"><code>find_duplicate([3, 1, 3, 4, 2])</code> should return <code>3</code></li>
<li id="test-3"><code>find_duplicate([1, 1])</code> should return <code>1</code></li>
<li id="test-4"><code>find_duplicate([2, 2, 2, 2, 2])</code> should return <code>2</code></li>
<li id="test-5"><code>find_duplicate([5, 4, 3, 2, 1, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>find_duplicate([1, 2, 3, 4, 5, 3])</code> should return <code>3</code></li>
</ul>
