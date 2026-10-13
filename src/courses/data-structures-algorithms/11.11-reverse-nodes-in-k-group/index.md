---
lesson_name: Reverse Nodes in K-Group
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Before reversing a group, what do you need to check? And after reversing it, which two outside nodes need new links?"
  - "Work group by group behind a dummy node. For each group, check `k` nodes exist, reverse them with the `prev = None` loop from *Linked List Basics* (starting `prev` at the node after the group), and reconnect the group to the node before it."
  - "Template: `group_prev = dummy`. Find the `k`-th node after `group_prev` (stop if there isn't one). Reverse from `group_prev.next` up to `kth.next`. Then `first = group_prev.next`, `group_prev.next = kth`, and `group_prev = first`."
rich_test_results: true
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

**Brute force:** copy the values into a Python list, reverse each full chunk of `k`, and build a new list. That's `O(n)` time but `O(n)` extra space, and it builds new nodes instead of relinking the given ones.

**Bottleneck:** the copy is only there to avoid the pointer bookkeeping at the edges of each group.

**Optimal idea:** reverse each group in place with the usual reversal loop, then fix the two links at its edges: the node before the group must point to the group's new first node (the old `k`-th), and the group's new last node (the old first) must point to the node after the group.

**Why it's correct:** starting `prev` at `group_next` makes the old first node of the group point to the node after the group once the reversal finishes. Setting `group_prev.next = kth` links the previous part to the reversed group. The old first node is now the group's last, so it's the `group_prev` for the next group. When fewer than `k` nodes are left, `get_kth` returns `None` and the rest stays as it is.

**Complexity:** `O(n)` time: each node is counted once and reversed once. `O(1)` extra space.

**Common mistakes:** reversing the last group even when it has fewer than `k` nodes. Losing the link between groups by starting `prev` at `None`, which cuts the list after the first group.

</details>
