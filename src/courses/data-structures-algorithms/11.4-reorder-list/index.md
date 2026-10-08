---
lesson_name: Reorder List
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

### Reorder List

Write a function `reorder_list(head)` that rearranges a singly linked list in place by weaving the first half with the reversed second half: first node, last node, second node, second-to-last node, and so on. The function should modify the list's node links directly and return nothing.

For example, the list `1 -> 2 -> 3 -> 4 -> 5` should be rearranged into `1 -> 5 -> 2 -> 4 -> 3`. The list `1 -> 2 -> 3 -> 4` should become `1 -> 4 -> 2 -> 3`.

---

### Tests

<ul>
<li id="test-1"><code>reorder_list([1, 2, 3, 4, 5])</code> should leave the list as <code>[1, 5, 2, 4, 3]</code></li>
<li id="test-2"><code>reorder_list([1, 2, 3, 4])</code> should leave the list as <code>[1, 4, 2, 3]</code></li>
<li id="test-3"><code>reorder_list([1])</code> should leave the list as <code>[1]</code></li>
<li id="test-4"><code>reorder_list([1, 2])</code> should leave the list as <code>[1, 2]</code></li>
<li id="test-5"><code>reorder_list([9, 8, 7])</code> should leave the list as <code>[9, 7, 8]</code></li>
<li id="test-6"><code>reorder_list([1, 2, 3, 4, 5, 6])</code> should leave the list as <code>[1, 6, 2, 5, 3, 4]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reorder_list(head):
    if not head:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```

</details>
