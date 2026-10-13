---
lesson_name: Reconstruct Itinerary
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(E log E)
  space: O(E)
hints:
  - "If you always take the alphabetically smallest ticket, you can get stuck at an airport with tickets left over. Which part of the route are you sure about at the moment you get stuck?"
  - "You need an Eulerian path (every edge exactly once), from *Spotting It* and *Tips & Gotchas* in *Advanced Graphs Basics*: Hierholzer's algorithm. Walk the smallest unused ticket each time. When an airport has no tickets left, it's the *last* stop among those still to place, so add it to the route then, and reverse the route at the end."
  - "Template: build `graph[src]` as a min-heap of destinations. `stack = [\"JFK\"]`, `route = []`. While `stack`: while `graph[stack[-1]]` has tickets, push `heappop(graph[stack[-1]])`. Then `route.append(stack.pop())`. Return `route[::-1]`."
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

### Reconstruct Itinerary

Write a function `find_itinerary(tickets)` that takes a list of `[from_airport, to_airport]` pairs representing one-way flight tickets, all starting from `"JFK"`, and returns the full itinerary as a list of airport codes that uses every ticket exactly once. When more than one valid itinerary exists, return the one that visits airports in lexicographically smallest order at each step. You may assume the input always allows at least one valid itinerary that uses every ticket.

For example, given tickets `[["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]]`, two different full itineraries are possible starting at `JFK`, but the lexicographically smaller one is `["JFK", "ATL", "JFK", "SFO", "ATL"]`, so that is what `find_itinerary(tickets)` should return.

---

### Tests

<ul>
<li id="test-1"><code>find_itinerary([["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]])</code> should return <code>["JFK", "ATL", "JFK", "SFO", "ATL"]</code></li>
<li id="test-2"><code>find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])</code> should return <code>["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]</code></li>
<li id="test-3"><code>find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])</code> should return <code>["JFK", "NRT", "JFK", "KUL"]</code></li>
<li id="test-4"><code>find_itinerary([["JFK", "A"], ["A", "B"], ["B", "JFK"]])</code> should return <code>["JFK", "A", "B", "JFK"]</code></li>
<li id="test-5"><code>find_itinerary([["JFK", "B"], ["JFK", "A"], ["B", "JFK"]])</code> should return <code>["JFK", "B", "JFK", "A"]</code></li>
<li id="test-6"><code>find_itinerary([["JFK", "SFO"]])</code> should return <code>["JFK", "SFO"]</code></li>
<li id="test-7">Performance: a chain of 26 airports, each with a round trip to a side airport, 77 tickets, within 1 second</li>
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

Here `E` is the number of tickets.

**Brute force:** backtracking. Sort the tickets, and from each airport try the smallest unused ticket first. If you get stuck with tickets left, undo the last ticket and try the next one. The first route that uses every ticket is the answer. It works, but a dead end can show up long after the wrong choice, and then you undo and retry everything in between. In the performance test that adds up to about `2^25` routes.

**Bottleneck:** you can't tell that a ticket is the wrong choice until much later.

**Optimal idea:** Hierholzer's algorithm never undoes anything. Follow the smallest ticket until you get stuck. An airport where you get stuck has no tickets left, so it has to come after everything you still need to place: add it to the *end* of the route. Then step back one airport and keep using its remaining tickets. The route is built back to front, so reverse it at the end.

**Why it's correct:** each ticket is popped from a heap once, so each is used once. In a valid route, every airport except the last one has a ticket out for each ticket in. So the first time you get stuck, you're at the airport where the route ends, and it's right to place it last. The same goes for a detour you skipped: when you step back to an airport that still has tickets, they form a loop back to it, and that loop is placed just before the part already placed. The smallest ticket is taken first wherever a full route is still possible, which gives the alphabetically smallest itinerary.

**Complexity:** `O(E log E)` time: each ticket is pushed and popped from a heap once. `O(E)` extra space for the graph, the stack and the route.

**Common mistakes:** adding an airport to the route when you *arrive* there instead of when you get stuck, which gives `["JFK", "KUL", "NRT", "JFK"]` for test 3. Forgetting to reverse the route. Using a plain list and `pop(0)` for the destinations, which works but costs `O(E)` per ticket.

</details>
