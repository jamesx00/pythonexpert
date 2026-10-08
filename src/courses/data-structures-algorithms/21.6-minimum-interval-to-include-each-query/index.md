---
lesson_name: Minimum Interval to Include Each Query
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

### Minimum Interval to Include Each Query

Write a function `min_interval_for_queries(intervals, queries)` that takes a list of `[start, end]` intervals and a list of query points. For each query `q`, find the size (`end - start + 1`) of the smallest interval that contains `q` (i.e. `start <= q <= end`), and return a list of those sizes in the same order as `queries`. If no interval contains a given query, its size should be `-1`.

For example, given `intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]` and `queries = [2, 3, 4, 5]`, the query `4` is covered by `[4, 4]` (size 1), `[2, 4]` (size 3), and `[1, 4]` (size 4) — the smallest is 1 — while the query `2` is only covered by `[1, 4]` and `[2, 4]`, and the smallest of those is `[2, 4]` with size 3. Query `5` is only covered by `[3, 6]` (size 4). The full result is `[3, 3, 1, 4]`.

---

### Tests

<ul>
<li id="test-1"><code>min_interval_for_queries([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5])</code> should return <code>[3, 3, 1, 4]</code></li>
<li id="test-2"><code>min_interval_for_queries([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22])</code> should return <code>[2, -1, 4, 6]</code></li>
<li id="test-3"><code>min_interval_for_queries([[1, 5]], [1, 3, 5, 6])</code> should return <code>[5, 5, 5, -1]</code></li>
<li id="test-4"><code>min_interval_for_queries([], [1, 2, 3])</code> should return <code>[-1, -1, -1]</code></li>
<li id="test-5"><code>min_interval_for_queries([[1, 10], [1, 3], [4, 10]], [1, 4, 10])</code> should return <code>[3, 7, 7]</code></li>
<li id="test-6"><code>min_interval_for_queries([[1, 1], [2, 2], [3, 3]], [1, 2, 3, 4])</code> should return <code>[1, 1, 1, -1]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq

def min_interval_for_queries(intervals, queries):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    answer = [-1] * len(queries)
    order = sorted(range(len(queries)), key=lambda i: queries[i])

    heap = []
    idx = 0
    for qi in order:
        q = queries[qi]
        while idx < len(ordered) and ordered[idx][0] <= q:
            start, end = ordered[idx]
            heapq.heappush(heap, (end - start + 1, end))
            idx += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            answer[qi] = heap[0][0]

    return answer
```

</details>
