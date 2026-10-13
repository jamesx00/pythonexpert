---
lesson_name: "Warm-up: Remove Linked List Elements"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "To unlink a node you need the node *before* it. What's before the head?"
  - "Use *The dummy (sentinel) node* from *Linked List Basics*: put `dummy = ListNode(0, head)` in front, walk `curr` from `dummy`, and skip `curr.next` with `curr.next = curr.next.next` whenever it matches. Return `dummy.next`."
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

### Warm-up: Remove Linked List Elements

Write a function `remove_elements(head, val)` that removes **every** node whose value equals `val` and returns the head of the resulting list.

For example, removing `6` from `1 -> 6 -> 2 -> 6 -> 3` gives `1 -> 2 -> 3`. Removing `7` from `7 -> 7 -> 7` gives an empty list (`None`).

---

### Tests

<ul>
<li id="test-1"><code>remove_elements([1, 6, 2, 6, 3], 6)</code> should return <code>[1, 2, 3]</code></li>
<li id="test-2"><code>remove_elements([7, 7, 7], 7)</code> should return <code>[]</code></li>
<li id="test-3"><code>remove_elements([], 1)</code> should return <code>[]</code></li>
<li id="test-4"><code>remove_elements([1, 2, 3], 4)</code> should return <code>[1, 2, 3]</code></li>
<li id="test-5"><code>remove_elements([5, 1, 5, 5, 2, 5], 5)</code> should return <code>[1, 2]</code></li>
<li id="test-6"><code>remove_elements([1, 2, 2, 1], 2)</code> should return <code>[1, 1]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def remove_elements(head, val):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```

**Brute force:** first strip matching nodes off the front with a separate loop, then walk the rest. It's also `O(n)`, but the two loops are easy to get wrong, for example when every node matches.

**Bottleneck:** the head has no node before it, so removing it needs a special case.

**Optimal idea:** a dummy node in front of the head gives every real node a predecessor, so one loop handles all removals.

**Why it's correct:** `curr` always stands one node before the node being checked, so it can unlink it. After a removal `curr` stays put, because the new `curr.next` hasn't been checked yet. Removed heads are skipped by `dummy.next` just like any other node.

**Complexity:** `O(n)` time, each node is checked once. `O(1)` extra space.

**Common mistakes:** moving `curr` forward after a removal, which skips the next node, as in `[5, 1, 5, 5, 2, 5]`. Returning `head` instead of `dummy.next`, which still points at a removed node.

</details>
