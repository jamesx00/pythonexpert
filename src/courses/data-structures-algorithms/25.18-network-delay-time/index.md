---
lesson_name: Network Delay Time
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(E log V)
  space: O(V + E)
hints:
  - "Pattern: *Advanced Graphs*."
  - "Each node hears the signal at the cheapest total time from `start`. Once you know that for every node, what's the answer?"
  - "Run Dijkstra from *Advanced Graphs Basics* from `start`. The signal has reached everything at the *largest* of those times (see *Tips & Gotchas*). If some node is never reached, return `-1`."
  - "Template: build `graph[u]` as a list of `(v, w)`. `dist = {}`, `heap = [(0, start)]`. Pop `(d, node)`. If `node` is in `dist`, skip it. Otherwise set `dist[node] = d` and push `(d + w, v)` for each neighbour. At the end return `max(dist.values())` if `len(dist) == n`, else `-1`."
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

### Network Delay Time

Write a function `network_delay_time(times, n, start)` that models a one-way signal broadcast across `n` nodes labeled `1` through `n`. `times` is a list of `[source, target, weight]` entries, each meaning a signal takes `weight` units of time to travel from `source` to `target`. Starting a broadcast at node `start`, return the number of time units it takes for the signal to reach every node. If some node can never be reached, return `-1` instead.

For example, with `n = 4`, `start = 1`, and `times = [[1, 2, 2], [1, 3, 5], [2, 3, 1], [3, 4, 1]]`, node `2` is reached at time `2`, node `3` is reached at time `3` (via node `2`, faster than the direct edge), and node `4` is reached at time `4`, so the whole network is covered by time `4` and `network_delay_time(times, n, start)` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>network_delay_time([[1, 2, 2], [1, 3, 5], [2, 3, 1], [3, 4, 1]], 4, 1)</code> should return <code>4</code></li>
<li id="test-2"><code>network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)</code> should return <code>2</code></li>
<li id="test-3"><code>network_delay_time([[1, 2, 1]], 2, 1)</code> should return <code>1</code></li>
<li id="test-4"><code>network_delay_time([[1, 2, 1]], 2, 2)</code> should return <code>-1</code></li>
<li id="test-5"><code>network_delay_time([[1, 2, 1], [2, 3, 2], [1, 3, 5]], 3, 1)</code> should return <code>3</code></li>
<li id="test-6"><code>network_delay_time([[1, 2, 1]], 3, 1)</code> should return <code>-1</code></li>
<li id="test-7">Performance: 20,000 nodes in a line with about 40,000 edges, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq
from collections import defaultdict


def network_delay_time(times, n, start):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    min_heap = [(0, start)]

    while min_heap:
        d, node = heapq.heappop(min_heap)
        if node in dist:
            continue
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(min_heap, (d + w, nei))

    if len(dist) != n:
        return -1
    return max(dist.values())
```

Here `V` is `n`, the number of nodes, and `E` the number of edges in `times`.

**Brute force:** Bellman-Ford: relax every edge again and again until no time improves. That can take `V - 1` rounds, so `O(V · E)`.

**Bottleneck:** each round goes over every edge, even though only a few times changed.

**Optimal idea:** Dijkstra. Pop the node with the smallest known time from a min-heap. The first time a node is popped, its time is final, so record it in `dist`. Then push its neighbours with the time through it. The answer is the largest time in `dist`.

**Why it's correct:** times are never negative, so the smallest time in the heap can't be beaten by a route through any other heap entry. The first pop of a node is therefore its earliest arrival. The whole network has the signal when the last node gets it, which is the largest of these times. If fewer than `n` nodes ever get popped, some node can't be reached.

**Complexity:** `O(E log V)` time: each edge pushes at most one heap entry. `O(V + E)` extra space for the graph, `dist` and the heap.

**Common mistakes:** returning the *sum* of the times instead of the largest. Forgetting that nodes are numbered `1` to `n`, so a list of size `n` is off by one. Checking only the nodes that appear in `times`, which misses a node with no edges at all, as in test 6.

</details>
