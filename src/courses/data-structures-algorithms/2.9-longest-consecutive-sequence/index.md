---
lesson_name: Longest Consecutive Sequence
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

### Longest Consecutive Sequence

Write a function `longest_consecutive(nums)` that takes a list of integers (in any order, possibly with duplicates) and returns the length of the longest run of consecutive integers that can be formed from the values in the list. A run of consecutive integers is a sequence like `4, 5, 6, 7` where each number is exactly one more than the previous, and the numbers do not need to appear next to each other in `nums`. Your solution should run in O(n) time.

For example, given `nums = [9, 1, 4, 2, 3, 100]`, the values `1, 2, 3, 4` form a run of length `4`, which is the longest one available, so `longest_consecutive(nums)` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>longest_consecutive([9, 1, 4, 2, 3, 100])</code> should return <code>4</code></li>
<li id="test-2"><code>longest_consecutive([])</code> should return <code>0</code></li>
<li id="test-3"><code>longest_consecutive([5])</code> should return <code>1</code></li>
<li id="test-4"><code>longest_consecutive([1, 2, 0, 1])</code> should return <code>3</code></li>
<li id="test-5"><code>longest_consecutive([10, 5, 12, 11, 6, 7])</code> should return <code>3</code></li>
<li id="test-6"><code>longest_consecutive([-2, -1, 0, 1, 2, 8])</code> should return <code>5</code></li>
</ul>
