---
lesson_name: Reverse Nodes in K-Group
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

### Reverse Nodes in K-Group

Write a function `reverse_k_group(head, k)` that reverses the nodes of a linked list `k` at a time and returns the new head. If the number of nodes remaining at the end of the list is fewer than `k`, that final group should be left untouched, in its original order.

For example, with `1 -> 2 -> 3 -> 4 -> 5` and `k = 2`, the result should be `2 -> 1 -> 4 -> 3 -> 5` - the first two pairs get reversed, but the last node has no partner so it stays as-is. With `k = 3` on the same list, the result should be `3 -> 2 -> 1 -> 4 -> 5`.

---

### Tests

<ul>
<li id="test-1"><code>reverse_k_group([1, 2, 3, 4, 5], 2)</code> should return <code>[2, 1, 4, 3, 5]</code></li>
<li id="test-2"><code>reverse_k_group([1, 2, 3, 4, 5], 3)</code> should return <code>[3, 2, 1, 4, 5]</code></li>
<li id="test-3"><code>reverse_k_group([1, 2, 3, 4, 5, 6], 1)</code> should return <code>[1, 2, 3, 4, 5, 6]</code></li>
<li id="test-4"><code>reverse_k_group([1, 2, 3, 4, 5, 6], 6)</code> should return <code>[6, 5, 4, 3, 2, 1]</code></li>
<li id="test-5"><code>reverse_k_group([1, 2], 3)</code> should return <code>[1, 2]</code></li>
<li id="test-6"><code>reverse_k_group([1, 2, 3, 4, 5, 6, 7], 3)</code> should return <code>[3, 2, 1, 6, 5, 4, 7]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reverse_k_group(head, k):
    def get_kth(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = group_next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next
```

</details>
