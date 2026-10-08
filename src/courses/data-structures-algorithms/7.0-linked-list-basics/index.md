---
lesson_name: Linked List Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Linked List
---

## Why This Pattern Matters &#x1F4A1;

A linked list is a chain of nodes, each holding a value and a pointer to the next node. There's no indexing: to reach the 5th node, you follow `.next` five times. Linked-list problems are mostly about **rewiring pointers without losing track of anything**.

Every lesson in this section uses this node class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Spotting It &#x1F50D;

- The input is a `head` node, so you're already in this pattern.
- Common sub-tasks: reverse (all or part), merge, find the middle, detect a cycle, remove the k-th from the end.
- Harder problems usually **chain these sub-tasks together**. *Reorder List* = find middle + reverse second half + merge.

## Core Building Blocks &#x1F9F1;

### Traversal

```python
curr = head
while curr:
    # use curr.val
    curr = curr.next
```

### `prev = None` for reversing

Reversing needs to remember the node **before** `curr`. At the start there isn't one, so `prev` starts as `None`, which is also exactly what the new tail's `.next` should be.

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next     # 1. save the rest of the list
        curr.next = prev    # 2. flip the pointer
        prev = curr         # 3. step prev forward
        curr = nxt          # 4. step curr forward
    return prev             # prev is the new head
```

Always save `curr.next` **before** overwriting it, or the rest of the list is lost.

### The dummy (sentinel) node

When the head itself might change (merging, removing the first node, building a new list), start from a fake node in front of it. You never need a special case for "is the list empty?" or "am I removing the head?".

```python
def remove_value(head, target):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next   # skip it
        else:
            curr = curr.next
    return dummy.next                    # the real head
```

To build an output list, keep a `tail` pointer starting at `dummy` and append with `tail.next = node; tail = tail.next`.

### Fast & slow pointers

`slow` moves 1 step, `fast` moves 2.

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now the middle; if fast ever == slow inside the loop, there's a cycle
```

### Gap of `n`

To remove the n-th node from the end, move `fast` `n` steps ahead, then move both until `fast` reaches the end. `slow` then sits just before the target. Starting both at a dummy makes removing the head work too.

## Tips & Gotchas &#x1F4CC;

- **Draw it.** Sketch 3–4 boxes and arrows and walk your code over them by hand. This catches most bugs.
- **Check before dereferencing.** `curr.next.val` crashes if `curr.next` is `None`. Loop conditions like `while fast and fast.next` exist for this.
- **Return `dummy.next`, not `head`.** `head` may have moved or been removed.
- **Edge cases to test:** empty list (`None`), one node, two nodes, and changes at the head or tail.
- **Splitting a list?** Cut it explicitly (`slow.next = None`), or you'll get cycles or duplicated tails.
- **Hash map of node → node** solves copy problems (*Copy List with Random Pointer*): first pass creates copies, second pass wires them.
- **Python `OrderedDict`** or a dict + doubly linked list with dummy `head`/`tail` nodes is the classic *LRU Cache* setup. The dummies again remove all edge cases.
