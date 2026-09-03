---
lesson_name: Reverse Linked List
code_editor: True
code_execution: True
adding_file_allowed: False
section: Linked List
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

### Reverse Linked List

Write a function `reverse_list(head)` that takes the head node of a singly linked list and returns the head of the list with all of its nodes in reverse order. The list is built from a shared `ListNode` class with `val` and `next` attributes.

For example, given the list `1 -> 2 -> 3 -> 4`, the function should return a list starting `4 -> 3 -> 2 -> 1`. An empty list (`head` is `None`) should stay empty, and a single-node list should be returned unchanged.

---

### Tests

<ul>
<li id="test-1"><code>reverse_list([1, 2, 3, 4])</code> should return <code>[4, 3, 2, 1]</code></li>
<li id="test-2"><code>reverse_list([])</code> should return <code>[]</code></li>
<li id="test-3"><code>reverse_list([7])</code> should return <code>[7]</code></li>
<li id="test-4"><code>reverse_list([1, 2])</code> should return <code>[2, 1]</code></li>
<li id="test-5"><code>reverse_list([5, 5, 5, 5])</code> should return <code>[5, 5, 5, 5]</code></li>
<li id="test-6"><code>reverse_list([9, -3, 4, 0, 2])</code> should return <code>[2, 0, 4, -3, 9]</code></li>
</ul>
