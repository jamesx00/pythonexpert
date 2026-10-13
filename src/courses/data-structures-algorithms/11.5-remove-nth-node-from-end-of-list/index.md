---
lesson_name: Remove Nth Node From End of List
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If one pointer starts `n` nodes ahead of another and they move together, where is the back pointer when the front one reaches the end?"
  - "Use *Gap of `n`* from *Linked List Basics*: move `fast` `n` steps ahead, then move both until `fast.next` is `None`. Start both at a dummy node so removing the head works too."
  - "Template: `dummy = ListNode(0, head)`, `fast = slow = dummy`. Move `fast` `n` times. While `fast.next`: move both. Then `slow.next = slow.next.next` and return `dummy.next`."
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

### Remove Nth Node From End of List

Write a function `remove_nth_from_end(head, n)` that removes the `n`-th node counting from the end of a singly linked list (the last node is `n = 1`), then returns the head of the resulting list. You may assume `n` is always valid for the given list. Try to do it in a single pass over the list.

For example, given `1 -> 2 -> 3 -> 4 -> 5` and `n = 2`, the second-to-last node (`4`) is removed, leaving `1 -> 2 -> 3 -> 5`. If `n` equals the length of the list, the head node itself is removed.

---

### Tests

<ul>
<li id="test-1"><code>remove_nth_from_end([1, 2, 3, 4, 5], 2)</code> should return <code>[1, 2, 3, 5]</code></li>
<li id="test-2"><code>remove_nth_from_end([1], 1)</code> should return <code>[]</code></li>
<li id="test-3"><code>remove_nth_from_end([1, 2], 1)</code> should return <code>[1]</code></li>
<li id="test-4"><code>remove_nth_from_end([1, 2], 2)</code> should return <code>[2]</code></li>
<li id="test-5"><code>remove_nth_from_end([1, 2, 3, 4, 5], 5)</code> should return <code>[2, 3, 4, 5]</code></li>
<li id="test-6"><code>remove_nth_from_end([10, 20, 30, 40], 1)</code> should return <code>[10, 20, 30]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
```

**Brute force:** count the nodes in one pass, then walk `length - n` steps in a second pass and remove the next node. That's also `O(n)` time and `O(1)` space, but needs two passes.

**Bottleneck:** the position from the end isn't known until the whole list has been read once.

**Optimal idea:** keep two pointers exactly `n` nodes apart. When the front one reaches the last node, the back one is right before the node to remove.

**Why it's correct:** after `fast` moves `n` steps from `dummy`, the gap between `fast` and `slow` is `n`. Moving both keeps that gap. When `fast` is the last node, the node after `slow` is the `n`-th from the end. Starting at `dummy` means that when `n` is the length of the list, `slow` stays at `dummy` and the head is removed with no special case.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** starting both pointers at `head` without a dummy, which crashes or misbehaves when the head must be removed, as in `remove_nth_from_end([1, 2], 2)`. Stopping on `while fast` instead of `while fast.next`, which leaves `slow` one node too far.

</details>
