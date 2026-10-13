---
lesson_name: K Closest Points to Origin
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log k)
  space: O(k)
hints:
  - "Comparing distances doesn't need the square root. And while scanning, which point would you throw out first if you could only keep `k`?"
  - "Keep the `k` closest points so far in a **max**-heap keyed by squared distance, so the farthest of them is at the root (*Top-k with a size-k heap* and *Max-heap by negating* in *Heap / Priority Queue Basics*). A closer point pushes it out."
  - "Template: for each `[x, y]`, `heappush(heap, (-(x * x + y * y), x, y))`, and `heappop` if `len(heap) > k`. Return `[[x, y] for _, x, y in heap]`."
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

### K Closest Points to Origin

Write a function `k_closest(points, k)` that takes a list of 2D points, each given as `[x, y]`, and returns the `k` points that are closest to the origin `(0, 0)`, measured by straight-line (Euclidean) distance. The returned points can be in any order.

For example, given `points = [[1, 1], [4, 4], [0, 1], [3, 3]]` and `k = 2`, the distances from the origin are roughly `1.41`, `5.66`, `1.0`, and `4.24`, so the two closest points are `[0, 1]` and `[1, 1]`.

---

### Tests

<ul>
<li id="test-1"><code>k_closest([[1, 1], [4, 4], [0, 1], [3, 3]], 2)</code> should return <code>[[0, 1], [1, 1]]</code> (any order)</li>
<li id="test-2"><code>k_closest([[3, 3], [5, -1], [-2, 4]], 1)</code> should return <code>[[3, 3]]</code></li>
<li id="test-3"><code>k_closest([[0, 0], [1, 0], [2, 0]], 2)</code> should return <code>[[0, 0], [1, 0]]</code> (any order)</li>
<li id="test-4"><code>k_closest([[-5, 4], [-6, -1], [3, 1]], 3)</code> should return <code>[[-5, 4], [-6, -1], [3, 1]]</code> (any order)</li>
<li id="test-5"><code>k_closest([[1, 2], [-1, -2], [1, -2], [-1, 2]], 2)</code> should return any 2 of the points, since all 4 are at squared distance <code>5</code></li>
<li id="test-6"><code>k_closest([[7, 7]], 1)</code> should return <code>[[7, 7]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def k_closest(points, k):
    heap = []  # max-heap of the k closest so far: (-distance, x, y)
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # drop the farthest
    return [[x, y] for _, x, y in heap]
```

**Brute force:** sort all points by `x * x + y * y` and take the first `k`. That's `O(n log n)` and passes here. `heapq.nsmallest(k, points, key=...)` is a one-line `O(n log k)` alternative.

**Bottleneck:** sorting orders all `n` points, but only the `k` closest are needed.

**Optimal idea:** scan the points and keep the `k` closest so far in a max-heap of size `k`. The root is the farthest of them, so it's the one to drop when a closer point comes along.

**Why it's correct:** after each point, the heap holds the `k` closest points seen so far. A popped point has at least `k` points at least as close, so it can't be in the answer. After the scan, the heap holds the `k` closest overall. Squared distance keeps the same order as distance, so no square root is needed.

**Complexity:** `O(n log k)` time: one push and at most one pop per point on a heap of size `k + 1`. `O(k)` space for the heap.

**Common mistakes:** a min-heap of size `k` (no negation), which pops the *closest* point and keeps the farthest. Using `math.sqrt`, which is slower and can round. Returning tuples `(x, y)` instead of lists `[x, y]`.

</details>
