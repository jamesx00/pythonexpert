---
lesson_name: Copy List with Random Pointer
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When you copy a node, its `random` target might not have been copied yet. What would you need to look up, to wire it later?"
  - "Use a dictionary from each original node to its copy (the *Hash map of node → node* tip in *Linked List Basics*). Create all the copies in one pass, then wire `next` and `random` in a second pass."
  - "Template: pass 1, `old_to_new[curr] = Node(curr.val)` for every node. Pass 2, `old_to_new[curr].next = old_to_new.get(curr.next)` and the same for `random`. Return `old_to_new[head]`, or `None` for an empty list."
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

### Copy List with Random Pointer

Write a function `copy_random_list(head)` that takes the head of a linked list where each node has a `val`, a `next` pointer, and an extra `random` pointer that can point to any node in the list (or to `None`), and returns a completely independent deep copy of the list - none of the new nodes may reuse or point back into the original list's nodes.

For example, if a node holding `3` has its `random` pointer aimed at the node holding `1` two positions later, the copied node holding `3` must have its own `random` pointer aimed at the *copied* node holding `1`, not the original.

---

### Tests

<ul>
<li id="test-1">list <code>[7, 13, 11, 10, 1]</code> with randoms <code>[None, 0, 4, 2, 0]</code> - the copy should match value/random-index pairs <code>[(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]</code></li>
<li id="test-2">list <code>[1, 2]</code> with randoms <code>[1, 1]</code> - the copy should match <code>[(1, 1), (2, 1)]</code></li>
<li id="test-3">list <code>[3]</code> with random <code>[0]</code> - the copy should match <code>[(3, 0)]</code></li>
<li id="test-4">an empty list - the copy should be empty</li>
<li id="test-5">list <code>[5, 6, 7]</code> with randoms <code>[None, None, None]</code> - the copy should match <code>[(5, None), (6, None), (7, None)]</code></li>
<li id="test-6">list <code>[1, 2, 3, 4]</code> with randoms <code>[3, 2, 1, 0]</code> - the copy should match <code>[(1, 3), (2, 2), (3, 1), (4, 0)]</code></li>
<li id="test-7">Performance: a 10,000-node list with random pointers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def copy_random_list(head):
    if not head:
        return None

    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]
```

**Brute force:** copy the `next` chain first. Then, for each original node, walk from the head to find the position of its `random` target, and walk the copy the same number of steps to find the matching copied node. Each lookup is `O(n)`, so this is `O(n²)`.

**Bottleneck:** finding "the copy of this original node" by walking the list, again and again.

**Optimal idea:** remember each original node's copy in a dictionary, so the copy of any node is one lookup away.

**Why it's correct:** after the first pass, every original node has exactly one copy in the dictionary. In the second pass, each copy's `next` and `random` are set to the copies of the original's `next` and `random`, so the copy has the same shape as the original but only points at new nodes. `.get()` maps `None` to `None`.

**Complexity:** `O(n)` time for two passes with `O(1)` dictionary operations. `O(n)` extra space for the dictionary.

**Common mistakes:** copying `random` as `curr.random`, which points into the original list. Setting `random` in the same pass that creates the copies, when the target's copy might not exist yet.

</details>
