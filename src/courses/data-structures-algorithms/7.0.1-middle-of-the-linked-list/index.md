---
lesson_name: "Warm-up: Middle of the Linked List"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If two runners start together and one runs twice as fast, where is the slow one when the fast one finishes?"
  - "Use *Fast & slow pointers* from *Linked List Basics*: start both at `head`, move `slow` one step and `fast` two steps while `fast and fast.next`, then return `slow`."
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

### Warm-up: Middle of the Linked List

Write a function `middle_node(head)` that returns the **middle node** of a singly linked list. If there are two middle nodes (an even number of nodes), return the **second** one. Return `None` for an empty list.

For example, for `1 -> 2 -> 3 -> 4 -> 5` return the node `3` (the tests show the list from that node onward: `[3, 4, 5]`). For `1 -> 2 -> 3 -> 4` return node `3`.

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

**Brute force:** copy every node into a Python list and return `nodes[len(nodes) // 2]`. That's `O(n)` time, but `O(n)` extra space. Counting the length first and then walking half of it avoids the list, but reads the list twice.

**Bottleneck:** you only need the length to know when to stop, and the length isn't known until you reach the end.

**Optimal idea:** move two pointers at once, `slow` one step and `fast` two steps. When `fast` reaches the end, `slow` has gone half as far.

**Why it's correct:** after `k` steps, `slow` is at node `k` and `fast` at node `2k`. The loop stops when `fast` is the last node (odd length) or `None` just past it (even length), which leaves `slow` at index `n // 2`: the middle, or the second of the two middles.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space for the two pointers.

**Common mistakes:** looping `while fast.next and fast.next.next`, which returns the *first* middle for even lengths and crashes on an empty list.

</details>
