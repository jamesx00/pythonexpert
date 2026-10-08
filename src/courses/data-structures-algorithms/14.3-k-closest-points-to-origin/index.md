---
lesson_name: K Closest Points to Origin
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
<li id="test-5"><code>k_closest([[1, 2], [-1, -2], [1, -2], [-1, 2]], 2)</code> should return 2 points, each with squared distance <code>5</code></li>
<li id="test-6"><code>k_closest([[7, 7]], 1)</code> should return <code>[[7, 7]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def k_closest(points, k):
    heap = [(x ** 2 + y ** 2, x, y) for x, y in points]
    heapq.heapify(heap)
    closest = heapq.nsmallest(k, heap)
    return [[x, y] for d, x, y in closest]
```

</details>
