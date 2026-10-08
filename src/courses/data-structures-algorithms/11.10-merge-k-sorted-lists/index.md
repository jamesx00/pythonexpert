---
lesson_name: Merge K Sorted Lists
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(N log k)
  space: O(k)
hints:
  - "The next node of the result is the smallest of the `k` current heads. How can you find the smallest of `k` values quickly, over and over?"
  - "Keep the current heads in a min-heap (`heapq`). Pop the smallest, attach it behind a dummy node as in *Merge Two Sorted Lists*, and push that node's `next`. Use the `tail` pointer pattern from *Linked List Basics*."
  - "Template: push `(node.val, i, node)` for each non-empty list (`i` breaks ties, since nodes can't be compared). While the heap isn't empty: pop, attach, and push `(node.next.val, i, node.next)` if there is one."
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
<li id="test-7">Performance: 1,000 lists of 50 nodes each, within 1 second</li>
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

Here `N` is the total number of nodes and `k` the number of lists.

**Brute force:** merge the lists into the result one at a time with *Merge Two Sorted Lists*. The result keeps growing, so the `i`-th merge walks up to `i * N/k` nodes, which adds up to `O(k·N)`.

**Bottleneck:** the early nodes are walked over again in every later merge.

**Optimal idea:** take nodes one at a time in final order. The next node is always the smallest of the `k` current heads, and a min-heap of those heads gives it in `O(log k)`.

**Why it's correct:** the heap always holds the smallest remaining node of every non-empty list, so its minimum is the smallest remaining node overall. Popping it and pushing its successor keeps that true. Each node goes into the heap once, so the result has every node, in sorted order.

**Complexity:** `O(N log k)` time: `N` pushes and pops on a heap of at most `k` items. `O(k)` extra space for the heap. Merging the lists in pairs (divide and conquer) also gets `O(N log k)` time.

**Common mistakes:** pushing `(node.val, node)`, which raises `TypeError` when two values tie because nodes can't be compared. Pushing every node at the start, which costs `O(N)` space.

</details>
