---
lesson_name: Min Cost to Connect All Points
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

### Min Cost to Connect All Points

Write a function `min_cost_connect_points(points)` that takes a list of `[x, y]` integer coordinates and returns the minimum total cost required to connect every point to every other point through some path, directly or indirectly. The cost of connecting two points is the Manhattan distance between them: `abs(x1 - x2) + abs(y1 - y2)`. You may connect any pair of points directly; the answer is the cost of the cheapest set of connections that leaves all points in one connected network.

For example, given points `[[0, 0], [2, 2], [3, 10]]`, connecting `[0, 0]` to `[2, 2]` costs `4`, and connecting `[2, 2]` to `[3, 10]` costs `9`, for a total of `13`, which is cheaper than any other way of linking all three points, so `min_cost_connect_points(points)` should return `13`.

---

### Tests

<ul>
<li id="test-1"><code>min_cost_connect_points([[0, 0], [2, 2], [3, 10]])</code> should return <code>13</code></li>
<li id="test-2"><code>min_cost_connect_points([[0, 0], [2, 2]])</code> should return <code>4</code></li>
<li id="test-3"><code>min_cost_connect_points([[0, 0]])</code> should return <code>0</code></li>
<li id="test-4"><code>min_cost_connect_points([[0, 0], [1, 1], [1, 0], [-1, 1]])</code> should return <code>4</code></li>
<li id="test-5"><code>min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]])</code> should return <code>18</code></li>
<li id="test-6"><code>min_cost_connect_points([[0, 0], [5, 0], [10, 0], [15, 0]])</code> should return <code>15</code></li>
</ul>
