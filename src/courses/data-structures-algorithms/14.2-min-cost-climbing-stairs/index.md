---
lesson_name: Min Cost Climbing Stairs
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

### Min Cost Climbing Stairs

Write a function `min_cost_climbing_stairs(cost)` that takes a list of integers where `cost[i]` is the price to step on stair `i`. From either stair `0` or stair `1` you may start for free, and each move advances you 1 or 2 stairs. The staircase has one extra stair past the last index in `cost`, representing the top, and you're done once you reach or pass it. Return the minimum total cost to reach the top.

For example, given `cost = [10, 15, 20]`, the cheapest route is to start on index `1` (cost `15`) and then take a single 2-step move straight to the top, for a total of `15`.

---

### Tests

<ul>
<li id="test-1"><code>min_cost_climbing_stairs([10, 15, 20])</code> should return <code>15</code></li>
<li id="test-2"><code>min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])</code> should return <code>6</code></li>
<li id="test-3"><code>min_cost_climbing_stairs([0, 0, 0, 0])</code> should return <code>0</code></li>
<li id="test-4"><code>min_cost_climbing_stairs([1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>min_cost_climbing_stairs([5, 3, 4, 2, 6])</code> should return <code>5</code></li>
<li id="test-6"><code>min_cost_climbing_stairs([2, 5])</code> should return <code>2</code></li>
</ul>
