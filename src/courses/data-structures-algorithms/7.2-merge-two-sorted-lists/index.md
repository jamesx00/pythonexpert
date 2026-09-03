---
lesson_name: Merge Two Sorted Lists
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

### Merge Two Sorted Lists

Write a function `merge_two_lists(list1, list2)` that takes the heads of two singly linked lists, each already sorted in ascending order, and returns the head of a single merged list that is also sorted in ascending order. Both input lists are built from the shared `ListNode` class.

For example, merging `1 -> 3 -> 5` with `2 -> 4 -> 6` should produce `1 -> 2 -> 3 -> 4 -> 5 -> 6`. If one of the input lists is empty, the result should simply be the other list's values in order.

---

### Tests

<ul>
<li id="test-1"><code>merge_two_lists([1, 3, 5], [2, 4, 6])</code> should return <code>[1, 2, 3, 4, 5, 6]</code></li>
<li id="test-2"><code>merge_two_lists([], [])</code> should return <code>[]</code></li>
<li id="test-3"><code>merge_two_lists([], [1, 2, 3])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-4"><code>merge_two_lists([5], [1])</code> should return <code>[1, 5]</code></li>
<li id="test-5"><code>merge_two_lists([1, 1, 3], [1, 2])</code> should return <code>[1, 1, 1, 2, 3]</code></li>
<li id="test-6"><code>merge_two_lists([2, 8, 9], [1, 3, 4, 10])</code> should return <code>[1, 2, 3, 4, 8, 9, 10]</code></li>
</ul>
