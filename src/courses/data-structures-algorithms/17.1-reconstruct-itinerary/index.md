---
lesson_name: Reconstruct Itinerary
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

### Reconstruct Itinerary

Write a function `find_itinerary(tickets)` that takes a list of `[from_airport, to_airport]` pairs representing one-way flight tickets, all starting from `"JFK"`, and returns the full itinerary as a list of airport codes that uses every ticket exactly once. When more than one valid itinerary exists, return the one that visits airports in lexicographically smallest order at each step. You may assume the input always allows at least one valid itinerary that uses every ticket.

For example, given tickets `[["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]]`, two different full itineraries are possible starting at `JFK`, but the lexicographically smaller one is `["JFK", "ATL", "JFK", "SFO", "ATL"]`, so that is what `find_itinerary(tickets)` should return.

---

### Tests

<ul>
<li id="test-1"><code>find_itinerary([["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]])</code> should return <code>["JFK", "ATL", "JFK", "SFO", "ATL"]</code></li>
<li id="test-2"><code>find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])</code> should return <code>["JFK", "ATL", "JFK", "ATL", "SFO", "ATL"]</code></li>
<li id="test-3"><code>find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])</code> should return <code>["JFK", "NRT", "JFK", "KUL"]</code></li>
<li id="test-4"><code>find_itinerary([["JFK", "A"], ["A", "B"], ["B", "JFK"]])</code> should return <code>["JFK", "A", "B", "JFK"]</code></li>
<li id="test-5"><code>find_itinerary([["JFK", "B"], ["JFK", "A"], ["B", "JFK"]])</code> should return <code>["JFK", "B", "JFK", "A"]</code></li>
<li id="test-6"><code>find_itinerary([["JFK", "SFO"]])</code> should return <code>["JFK", "SFO"]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq
from collections import defaultdict


def find_itinerary(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)

    route = []
    stack = ["JFK"]
    while stack:
        while graph[stack[-1]]:
            stack.append(heapq.heappop(graph[stack[-1]]))
        route.append(stack.pop())
    return route[::-1]
```

</details>
