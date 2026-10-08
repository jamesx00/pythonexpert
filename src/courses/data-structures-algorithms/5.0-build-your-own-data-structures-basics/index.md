---
lesson_name: Build-It-Yourself Data Structures Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Build-It-Yourself Data Structures
---

## Why This Matters &#x1F4A1;

Most solutions in this course lean on four built-in structures: `list`, `dict`, `heapq` and, in the Trees section, binary search trees. It's easy to treat them as black boxes and memorise their complexities. This section opens each box. Once you've built them yourself, `O(1)` amortized append, `O(1)` average lookup and `O(log n)` heap push stop being facts to memorise and become things you can explain.

## Dynamic Array (how `list` works) &#x1F4E6;

A dynamic array keeps its items in a fixed-capacity block and tracks how many slots are used.

- **Append:** if there's room, write into the next slot (`O(1)`). If it's full, allocate a block twice the size and copy everything over (`O(n)`, but rare). That gives `O(1)` **amortized** append.
- **Insert at the front:** every item shifts one slot to the right, so it's `O(n)`.
- **Index access:** the slot's position is computed directly, so it's `O(1)`.

```python
class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
```

## Hash Map (how `dict` works) &#x1F5C2;&#xFE0F;

A hash map stores entries in an array of **buckets**. To find a key, compute `hash(key) % number_of_buckets` and look only in that bucket.

- **Collisions:** two keys can land in the same bucket. With **separate chaining**, each bucket holds a small list of `(key, value)` pairs that you scan.
- **Load factor:** when `entries / buckets` gets too high, the chains get long. Double the bucket count and re-insert everything, just like a dynamic array resize.
- **Why `O(1)` on average:** a good hash spreads keys evenly, so each bucket holds only a few entries. In the worst case, when every key collides, lookups degrade to `O(n)`.
- **Why keys must be hashable:** if a key could change after being inserted, its hash would change and you'd look in the wrong bucket. That's why lists can't be dict keys but tuples can.

## Binary Heap (how `heapq` works) &#x26F0;&#xFE0F;

A min-heap is a complete binary tree where every parent is `<=` its children, stored in a plain list:

- children of index `i` are at `2*i + 1` and `2*i + 2`
- the parent of index `i` is at `(i - 1) // 2`

```python
def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] >= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
```

- **Push:** append to the end, then **sift up** while smaller than the parent. `O(log n)`.
- **Pop:** take the root, move the last item to the root, then **sift down** while larger than the smaller child. `O(log n)`.
- **Peek:** `heap[0]`, `O(1)`.
- **Heapify:** sifting down from the last parent to the root builds a heap in `O(n)`.

## Binary Search Tree &#x1F333;

Every node's left subtree holds smaller keys and its right subtree holds larger keys.

- **Search / insert:** compare with the current node and go left or right. `O(h)`, where `h` is the tree's height.
- **Delete:** a leaf is removed directly. A node with one child is replaced by that child. A node with two children takes the value of its **in-order successor** (the smallest node in its right subtree), and then that successor is deleted.
- **Height matters:** a balanced tree has `h ≈ log n`. Inserting already sorted keys builds a tree that is just a linked list, with `h = n`.
- **In-order traversal** of a BST visits the keys in sorted order. Several Trees problems rely on this.

## Tips & Gotchas &#x1F4CC;

- **Resize by multiplying, not adding.** Growing by a fixed amount (say, +10 slots) makes append `O(n)` amortized.
- **Off-by-one in heap indexes** is the most common heap bug. Write the parent/child formulas down before coding.
- **BST delete has three cases.** Handle and test each one separately.
