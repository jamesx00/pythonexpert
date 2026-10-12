---
lesson_name: Minimum Interval to Include Each Query
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n log n + m log m)
  space: O(n + m)
hints:
  - "If you answer the queries from smallest to largest, how does the set of intervals that could contain the query change from one query to the next?"
  - "Intervals only join (once their start is passed) or expire (once their end is passed). Keep the joined ones in a min-heap by size, and drop expired ones from the top (see *Queries over intervals* in *Tips & Gotchas* in *Intervals Basics*)."
  - "Template: sort the intervals by start and the query indexes by value. For each query `q`, push `(size, end)` for every interval with `start <= q`, pop while `heap[0][1] < q`, and answer `heap[0][0]` or `-1`."
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
<li id="test-7">Performance: 50,001 intervals and 50,000 queries, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def min_interval_for_queries(intervals, queries):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    answer = [-1] * len(queries)
    order = sorted(range(len(queries)), key=lambda i: queries[i])

    heap = []  # (size, end) of intervals that start at or before q
    idx = 0
    for qi in order:
        q = queries[qi]
        while idx < len(ordered) and ordered[idx][0] <= q:
            start, end = ordered[idx]
            heapq.heappush(heap, (end - start + 1, end))
            idx += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)  # ended before q, and later queries are larger
        if heap:
            answer[qi] = heap[0][0]

    return answer
```

Here `n` is `len(intervals)` and `m` is `len(queries)`.

**Brute force:** for each query, check every interval and keep the smallest one that contains it. That's `O(n * m)`.

**Bottleneck:** every query looks at every interval again, even though nearby queries are covered by mostly the same intervals.

**Optimal idea:** answer the queries in sorted order, and remember where each one goes in the answer. Sort the intervals by start too. As the query grows, push every interval that has now started onto a min-heap keyed by size. Before reading the top, pop intervals that ended before the query. The top is then the smallest interval that contains it.

**Why it's correct:** every interval in the heap has `start <= q`. Popping the top while its end is below `q` leaves a top that also has `end >= q`, so it contains `q`, and nothing smaller in the heap was skipped. Expired intervals deeper in the heap are harmless: they're popped as soon as they reach the top. And the queries only grow, so an interval that ended before one query is never needed again.

**Complexity:** `O(n log n + m log m)` time: the two sorts, and each interval is pushed and popped at most once. `O(n + m)` space for the heap, the sorted copies and the answer.

**Common mistakes:** answering the queries in sorted order but writing the answers in that order too, instead of back at each query's original index. Popping with `<=`, which drops an interval whose end equals the query. Sizing an interval as `end - start` instead of `end - start + 1`.

</details>
