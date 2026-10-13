---
lesson_name: Reverse Linked List
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "When you flip `curr.next` to point backwards, how do you still reach the rest of the list?"
  - "Use the `prev = None` reversal loop from *Linked List Basics*: save `nxt = curr.next` before flipping the pointer, then step `prev` and `curr` forward."
  - "Template: `prev, curr = None, head`. While `curr`: `nxt = curr.next`, `curr.next = prev`, `prev = curr`, `curr = nxt`. Return `prev`."
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

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Brute force:** copy the values into a Python list and build a new linked list from it in reverse. That's `O(n)` time but `O(n)` extra space, and it creates new nodes instead of reversing the given ones.

**Bottleneck:** the copy only exists because flipping a pointer seems to lose the rest of the list.

**Optimal idea:** walk the list once and flip each `next` pointer to the previous node, saving the old `next` first so the rest of the list isn't lost.

**Why it's correct:** before each step, `prev` is the head of the already-reversed part and `curr` the head of the untouched part. One step moves `curr` from the second part to the front of the first. When `curr` is `None`, everything is reversed and `prev` is the new head. Starting with `prev = None` makes the old head the new tail.

**Complexity:** `O(n)` time, `O(1)` extra space.

**Common mistakes:** setting `curr.next = prev` before saving `curr.next`, which cuts off the rest of the list. Returning `head` or `curr` instead of `prev`. A recursive version is also `O(n)` time, but uses `O(n)` stack space and hits Python's recursion limit on long lists.

</details>
