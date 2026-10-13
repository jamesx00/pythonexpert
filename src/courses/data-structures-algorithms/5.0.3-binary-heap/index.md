---
lesson_name: "Warm-up: Binary Heap"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log n) push and pop
  space: O(n)
hints:
  - "After appending a new value at the end, the only place the heap property can be broken is between that value and its parent. After moving the last value to the root, where can it be broken?"
  - "Follow *Binary Heap* in *Build-It-Yourself Data Structures Basics*. `_sift_up(i)`: while `i > 0` and `heap[i] < heap[(i - 1) // 2]`, swap with the parent and move up. `pop`: swap the root with the last item, `pop()` it off, then `_sift_down(0)`: find the smaller of the children `2 * i + 1` and `2 * i + 2`, and while it's smaller than `heap[i]`, swap and move down."
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

### Warm-up: Binary Heap

`heapq` is a **binary min-heap** stored in a plain list. Build one yourself in `self._heap`, using the index formulas: the children of index `i` are at `2 * i + 1` and `2 * i + 2`, and its parent is at `(i - 1) // 2`. The **heap property** is that every parent is `<=` its children, so the smallest item is always at index `0`.

Implement:

- `_sift_up(i)`: while the item at `i` is **smaller than** its parent, swap them and continue from the parent's index.
- `_sift_down(i)`: while the item at `i` is larger than its smaller child, swap it with that child and continue from there. If both children are equal, use the left one.
- `push(value)`: append `value` to the end, then sift it up.
- `pop()`: remove and return the smallest item. Swap the root with the last item, remove the last item, then sift the new root down. Raise `IndexError` if the heap is empty.

Don't use the `heapq` module. `peek()` and `len()` are done for you.

---

### Tests

<ul>
<li id="test-1">push 5, 3, 8, 1: <code>_heap</code> should be <code>[1, 3, 8, 5]</code></li>
<li id="test-2">push 7, 2, 9: <code>peek()</code> should return <code>2</code> and <code>len()</code> should be <code>3</code></li>
<li id="test-3">push 5, 3, 8, 1, 9, 2, then pop 6 times: should return <code>1, 2, 3, 5, 8, 9</code></li>
<li id="test-4">push 5, 3, 8, 1, then pop: should return <code>1</code> and leave <code>_heap</code> as <code>[3, 5, 8]</code></li>
<li id="test-5">push 2, 2, 1, 1, then pop 4 times: should return <code>1, 1, 2, 2</code></li>
<li id="test-6">push 4, 1, pop, push 3, 0, pop 3 times: should return <code>1, 0, 3, 4</code></li>
<li id="test-7"><code>pop()</code> on an empty heap should raise <code>IndexError</code></li>
<li id="test-8">push 10 down to 1, then <code>_heap</code> should satisfy the heap property: every parent <code>&lt;=</code> its children</li>
<li id="test-9"><code>main.py</code> doesn't import <code>heapq</code></li>
<li id="test-10">Performance: 30,011 pushes followed by 30,011 pops, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class MinHeap:
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def peek(self):
        return self._heap[0]

    def push(self, value):
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        heap = self._heap
        if not heap:
            raise IndexError("pop from an empty heap")
        heap[0], heap[-1] = heap[-1], heap[0]
        smallest = heap.pop()
        if heap:
            self._sift_down(0)
        return smallest

    def _sift_up(self, i):
        heap = self._heap
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] >= heap[parent]:
                break
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent

    def _sift_down(self, i):
        heap = self._heap
        n = len(heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right
            if smallest == i:
                return
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
```

**Brute force:** keep the list sorted, calling `.sort()` after every push, and pop with `pop(0)`. Or keep it unsorted and pop with `min()` and `remove()`. Either way, one of the two operations touches every item: `O(n)` per operation (`O(n log n)` for a full sort), `O(n²)` for `n` pushes and pops.

**Bottleneck:** a fully sorted list is more order than we need. We only ever ask for the smallest item.

**Optimal idea:** keep the weaker heap property (each parent `<=` its children). It's enough to keep the minimum at index `0`, and it can be repaired along a single root-to-leaf path in `O(log n)` swaps.

**Why it's correct:** before a push, the heap property holds everywhere. Appending a value can only break it between the new value and its parent, and each sift-up swap moves the problem one level up, until the parent is `<=` the value or the value reaches the root. In `pop`, moving the last item to the root can only break the property between the root and its children. Swapping it with the **smaller** child makes that child a valid parent of both subtrees (it's `<=` its sibling), and pushes the problem one level down. Swapping with the larger child would put a bigger item above a smaller one.

**Complexity:** the heap is a complete binary tree, so its height is about `log₂ n`, and each sift moves at most one level per step: `O(log n)` for `push` and `pop`, `O(1)` for `peek`. `O(n)` space for the list. 30,011 pushes and pops take a few hundred thousand swaps instead of hundreds of millions of comparisons.

**Common mistakes:** in `pop`, removing `heap[0]` with `pop(0)`, which shifts the whole list (`O(n)`) and scrambles the parent/child positions. Comparing only with the left child in `_sift_down`. Forgetting the bounds checks `left < n` and `right < n`. Calling `_sift_down(0)` after popping the last item, when the heap is now empty. Getting the parent formula wrong: it's `(i - 1) // 2`, not `i // 2`.

</details>
