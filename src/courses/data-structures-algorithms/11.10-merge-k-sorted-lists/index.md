---
lesson_name: Merge K Sorted Lists
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

### Merge K Sorted Lists

Write a function `merge_k_lists(lists)` that takes a list of linked-list heads, where each individual linked list is already sorted in ascending order, and merges all of them into a single sorted linked list, returning its head.

For example, given the three lists `1 -> 4 -> 5`, `1 -> 3 -> 4`, and `2 -> 6`, the merged result should be `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`. An empty input list of lists should produce an empty result, and individual lists inside it may also be empty.

---

### Tests

<ul>
<li id="test-1"><code>merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]])</code> should return <code>[1, 1, 2, 3, 4, 4, 5, 6]</code></li>
<li id="test-2"><code>merge_k_lists([])</code> should return <code>[]</code></li>
<li id="test-3"><code>merge_k_lists([[]])</code> should return <code>[]</code></li>
<li id="test-4"><code>merge_k_lists([[5]])</code> should return <code>[5]</code></li>
<li id="test-5"><code>merge_k_lists([[1, 2, 3], []])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-6"><code>merge_k_lists([[9], [1, 5], [2, 3, 7]])</code> should return <code>[1, 2, 3, 5, 7, 9]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

</details>
