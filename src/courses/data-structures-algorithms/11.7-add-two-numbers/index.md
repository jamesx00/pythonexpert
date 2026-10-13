---
lesson_name: Add Two Numbers
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(max(m, n))
  space: O(max(m, n))
hints:
  - "How do you add two numbers on paper, and which digit do you start with?"
  - "The lists already start at the ones digit, so add digit by digit from the heads, carrying `total // 10` to the next step. Build the result behind a dummy node, as in *Linked List Basics*."
  - "Template: `carry = 0`. While `l1 or l2 or carry`: add the two digits (`0` for a finished list) and `carry`, append `ListNode(total % 10)`, set `carry = total // 10`, and advance whichever lists are left."
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

### Add Two Numbers

Write a function `add_two_numbers(l1, l2)` that takes two non-empty linked lists, each representing a non-negative integer with the digits stored in reverse order (the ones digit is the head node), and returns a new linked list representing the sum of the two numbers, also with digits stored in reverse order.

For example, the list `2 -> 4 -> 3` represents `342`, and the list `5 -> 6 -> 4` represents `465`. Adding them together gives `807`, which should be returned as the list `7 -> 0 -> 8`.

---

### Tests

<ul>
<li id="test-1"><code>add_two_numbers([2, 4, 3], [5, 6, 4])</code> should return <code>[7, 0, 8]</code></li>
<li id="test-2"><code>add_two_numbers([0], [0])</code> should return <code>[0]</code></li>
<li id="test-3"><code>add_two_numbers([9, 9, 9], [1])</code> should return <code>[0, 0, 0, 1]</code></li>
<li id="test-4"><code>add_two_numbers([5], [5])</code> should return <code>[0, 1]</code></li>
<li id="test-5"><code>add_two_numbers([1, 2], [9, 9, 9])</code> should return <code>[0, 2, 0, 1]</code></li>
<li id="test-6"><code>add_two_numbers([9, 9], [9, 9])</code> should return <code>[8, 9, 1]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def add_two_numbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
```

Here `m` and `n` are the lengths of the two lists.

**Brute force:** turn each list into a Python integer, add them, and turn the sum back into a list of digits. It works in Python because integers have no size limit, but converting very long numbers to and from integers is slower than linear, and in most other languages the numbers wouldn't fit in an integer at all.

**Bottleneck:** the conversion is unnecessary: the digits are already in the order you'd add them.

**Optimal idea:** do school addition directly on the lists, one digit at a time from the ones digit, carrying into the next position.

**Why it's correct:** at each position the digit is `(d1 + d2 + carry) % 10` and the carry is `(d1 + d2 + carry) // 10`, which is exactly column addition. Treating a finished list as `0` handles different lengths, and looping while `carry` is non-zero adds the final digit, as in `999 + 1 = 1000`.

**Complexity:** `O(max(m, n))` time, one step per digit. `O(max(m, n))` space for the result, `O(1)` besides it.

**Common mistakes:** stopping when both lists end, which drops the last carry, as in `[5] + [5]`. Advancing `l1.next` when `l1` is already `None`.

</details>
