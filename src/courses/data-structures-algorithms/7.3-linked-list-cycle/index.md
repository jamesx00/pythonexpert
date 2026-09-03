---
lesson_name: Linked List Cycle
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

### Linked List Cycle

Write a function `has_cycle(head)` that takes the head node of a singly linked list and returns `True` if the list loops back on itself at any point, or `False` if it ends normally with a `None`. You are not allowed to use extra data structures to remember every node you've visited - solve it using constant extra space.

For example, if the last node of a list points back to an earlier node instead of `None`, `has_cycle` should return `True`. A list with no such loop should return `False`.

---

### Tests

<ul>
<li id="test-1">a list <code>3 -> 2 -> 0 -> -4</code> whose tail points back to the node holding <code>2</code> - <code>has_cycle(head)</code> should return <code>True</code></li>
<li id="test-2">a list <code>1 -> 2</code> whose tail points back to the head - <code>has_cycle(head)</code> should return <code>True</code></li>
<li id="test-3">a single node <code>1</code> with no cycle - <code>has_cycle(head)</code> should return <code>False</code></li>
<li id="test-4">an empty list (<code>head</code> is <code>None</code>) - <code>has_cycle(head)</code> should return <code>False</code></li>
<li id="test-5">a list <code>1 -> 2 -> 3 -> 4 -> 5</code> with no cycle - <code>has_cycle(head)</code> should return <code>False</code></li>
<li id="test-6">a list <code>7 -> 8 -> 9</code> whose tail points back to itself - <code>has_cycle(head)</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

</details>
