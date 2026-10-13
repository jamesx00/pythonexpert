---
lesson_name: Cheapest Flights Within K Stops
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(k · E)
  space: O(n)
hints:
  - "Plain Dijkstra finds the cheapest route, but it may use too many flights. How could you find the cheapest price using at most 1 flight, then at most 2, and so on?"
  - "From *Spotting It* and *Tips & Gotchas* in *Advanced Graphs Basics*: run Bellman-Ford for exactly `k + 1` rounds. Each round relaxes every flight once, which allows one more flight. Copy the prices at the start of each round, so a round can't chain two flights together."
  - "Template: `prices = [inf] * n`, `prices[src] = 0`. Repeat `k + 1` times: `updated = prices[:]`, and for each `u, v, w`, if `prices[u] + w < updated[v]`, set `updated[v] = prices[u] + w`. Then `prices = updated`. Return `prices[dst]`, or `-1` if it's still `inf`."
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

### Cheapest Flights Within K Stops

Write a function `find_cheapest_price(n, flights, src, dst, k)` that models `n` airports labeled `0` through `n - 1` and a list of one-way `flights`, each given as `[from_airport, to_airport, price]`. Find the cheapest total price to fly from `src` to `dst` using at most `k` intermediate stops (so at most `k + 1` flights total). If no such route exists, return `-1`.

For example, with `n = 3` airports and `flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]`, flying directly from `0` to `2` costs `500`, but routing through airport `1` costs `100 + 100 = 200` and uses only `1` stop; with `k = 1` that route is allowed, so `find_cheapest_price(n, flights, 0, 2, 1)` should return `200`.

---

### Tests

<ul>
<li id="test-1"><code>find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)</code> should return <code>200</code></li>
<li id="test-2"><code>find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)</code> should return <code>500</code></li>
<li id="test-3"><code>find_cheapest_price(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 1)</code> should return <code>5</code></li>
<li id="test-4"><code>find_cheapest_price(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 2)</code> should return <code>3</code></li>
<li id="test-5"><code>find_cheapest_price(3, [[0, 1, 100]], 0, 2, 5)</code> should return <code>-1</code></li>
<li id="test-6"><code>find_cheapest_price(2, [[0, 1, 10]], 0, 1, 0)</code> should return <code>10</code></li>
<li id="test-7"><code>find_cheapest_price(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1)</code> should return <code>6</code></li>
<li id="test-8">Performance: 66 airports in 8 layers of 8, 464 flights, <code>k = 8</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_cheapest_price(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        updated = prices[:]
        for u, v, w in flights:
            if prices[u] != float("inf") and prices[u] + w < updated[v]:
                updated[v] = prices[u] + w
        prices = updated

    return prices[dst] if prices[dst] != float("inf") else -1
```

Here `n` is the number of airports and `E` the number of flights.

**Brute force:** DFS over every route from `src` with at most `k + 1` flights, and keep the cheapest one that ends at `dst`. The number of routes grows exponentially: the performance test has `8^8`, about 16.8 million.

**Bottleneck:** many routes reach the same airport with the same number of flights, and only the cheapest of them matters.

**Optimal idea:** Bellman-Ford with a limit. After round `i`, `prices[v]` is the cheapest way to reach `v` with at most `i` flights. Each round relaxes every flight once, from the prices of the round before. Stop after `k + 1` rounds.

**Why it's correct:** the cheapest route to `v` with at most `i` flights is either a route with fewer flights, or the cheapest route to some `u` with at most `i - 1` flights plus the flight `u -> v`. One round checks exactly these options. Reading from `prices` and writing to `updated` makes sure a round only adds one flight. Writing straight into `prices` could let one round use `0 -> 1` and then `1 -> 2`, which breaks test 2.

**Complexity:** `O(k · E)` time: `k + 1` rounds over every flight. `O(n)` extra space for the two price lists.

**Common mistakes:** updating `prices` in place within a round. Running `k` rounds instead of `k + 1` (k stops means k + 1 flights). Using plain Dijkstra, which finds the cheapest route to airport 2 through airport 1 in test 7 and then has no stops left to reach 3. Dijkstra on `(price, airport, stops)` also works, but only if it keeps states with more stops instead of skipping every airport it has already seen.

</details>
