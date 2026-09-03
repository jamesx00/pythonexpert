---
lesson_name: Longest Increasing Subsequence
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

### Longest Increasing Subsequence

Write a function `length_of_lis(nums)` that takes a list of integers and returns the length of the longest strictly increasing subsequence, meaning a sequence of elements picked from `nums` in their original relative order (not necessarily adjacent) where each element is strictly greater than the one before it.

For example, given `nums = [0, 3, 1, 6, 2, 2, 7]`, one longest increasing subsequence is `0, 1, 2, 7`, giving a length of `4`.

---

### Tests

<ul>
<li id="test-1"><code>length_of_lis([0, 3, 1, 6, 2, 2, 7])</code> should return <code>4</code></li>
<li id="test-2"><code>length_of_lis([7, 7, 7, 7])</code> should return <code>1</code></li>
<li id="test-3"><code>length_of_lis([4, 10, 4, 3, 8, 9])</code> should return <code>3</code></li>
<li id="test-4"><code>length_of_lis([5])</code> should return <code>1</code></li>
<li id="test-5"><code>length_of_lis([1, 2, 3, 4, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>length_of_lis([5, 4, 3, 2, 1])</code> should return <code>1</code></li>
<li id="test-7"><code>length_of_lis([9, 1, 4, 2, 3, 3, 7])</code> should return <code>4</code></li>
</ul>
