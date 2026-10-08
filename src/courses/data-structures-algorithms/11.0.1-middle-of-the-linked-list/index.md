---
lesson_name: "Warm-up: Middle of the Linked List"
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

### Warm-up: Middle of the Linked List

Write a function `middle_node(head)` that returns the **middle node** of a singly linked list. If there are two middle nodes (an even number of nodes), return the **second** one. Return `None` for an empty list.

For example, for `1 -> 2 -> 3 -> 4 -> 5` return the node `3` (the tests show the list from that node onward: `[3, 4, 5]`). For `1 -> 2 -> 3 -> 4` return node `3`.

**Hint:** use fast & slow pointers. Start both at `head`. Move `slow` one step and `fast` two steps while `fast and fast.next`. When `fast` runs out of list, `slow` is halfway.

---

### Tests

<ul>
<li id="test-1"><code>middle_node([1, 2, 3, 4, 5])</code> should return <code>[3, 4, 5]</code></li>
<li id="test-2"><code>middle_node([1, 2, 3, 4])</code> should return <code>[3, 4]</code></li>
<li id="test-3"><code>middle_node([1])</code> should return <code>[1]</code></li>
<li id="test-4"><code>middle_node([1, 2])</code> should return <code>[2]</code></li>
<li id="test-5"><code>middle_node([])</code> should return <code>[]</code></li>
<li id="test-6"><code>middle_node([10, 20, 30, 40, 50, 60, 70])</code> should return <code>[40, 50, 60, 70]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

`fast` covers twice the distance of `slow`, so when `fast` reaches the end, `slow` has covered half. The condition `fast and fast.next` stops safely for both odd and even lengths, and an empty list just returns `None`. This finds the middle in one pass, without counting the length first.

</details>
