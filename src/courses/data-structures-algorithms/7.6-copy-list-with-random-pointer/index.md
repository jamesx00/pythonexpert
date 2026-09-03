---
lesson_name: Copy List with Random Pointer
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

### Copy List with Random Pointer

Write a function `copy_random_list(head)` that takes the head of a linked list where each node has a `val`, a `next` pointer, and an extra `random` pointer that can point to any node in the list (or to `None`), and returns a completely independent deep copy of the list - none of the new nodes may reuse or point back into the original list's nodes.

For example, if a node holding `3` has its `random` pointer aimed at the node holding `1` two positions later, the copied node holding `3` must have its own `random` pointer aimed at the *copied* node holding `1`, not the original.

---

### Tests

<ul>
<li id="test-1">list <code>[7, 13, 11, 10, 1]</code> with randoms <code>[None, 0, 4, 2, 0]</code> - the copy should match value/random-index pairs <code>[(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]</code></li>
<li id="test-2">list <code>[1, 2]</code> with randoms <code>[1, 1]</code> - the copy should match <code>[(1, 1), (2, 1)]</code></li>
<li id="test-3">list <code>[3]</code> with random <code>[0]</code> - the copy should match <code>[(3, 0)]</code></li>
<li id="test-4">an empty list - the copy should be empty</li>
<li id="test-5">list <code>[5, 6, 7]</code> with randoms <code>[None, None, None]</code> - the copy should match <code>[(5, None), (6, None), (7, None)]</code></li>
<li id="test-6">list <code>[1, 2, 3, 4]</code> with randoms <code>[3, 2, 1, 0]</code> - the copy should match <code>[(1, 3), (2, 2), (3, 1), (4, 0)]</code></li>
</ul>
