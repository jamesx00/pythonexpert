---
lesson_name: Cheapest Flights Within K Stops
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

</details>
