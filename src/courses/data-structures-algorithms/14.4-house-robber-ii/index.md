---
lesson_name: House Robber II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "The circle adds just one rule: the first and last houses can't both be robbed. So at least one of them is skipped. What problems are left in each case?"
  - "Run plain House Robber twice, once on `houses[1:]` and once on `houses[:-1]`, and take the larger (see *Tips & Gotchas* in *1-D Dynamic Programming Basics*). A single house is a special case."
  - "Template: if `len(houses) == 1`, return `houses[0]`. Otherwise return `max(rob_line(houses[1:]), rob_line(houses[:-1]))`, where `rob_line` is the two-variable loop from House Robber."
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

### House Robber II

Write a function `rob_circular(houses)` that solves the same problem as House Robber, except this time the houses are arranged in a circle, so the first house and the last house are also considered neighbors. As before you may never rob two adjacent houses, and you must return the maximum total amount stealable.

For example, given `houses = [2, 3, 2]`, robbing house `0` and house `2` is not allowed since they are adjacent in the circle, so the best you can do is rob house `1` alone for a total of `3`.

---

### Tests

<ul>
<li id="test-1"><code>rob_circular([2, 3, 2])</code> should return <code>3</code></li>
<li id="test-2"><code>rob_circular([1, 2, 3, 1])</code> should return <code>4</code></li>
<li id="test-3"><code>rob_circular([1, 2, 3])</code> should return <code>3</code></li>
<li id="test-4"><code>rob_circular([5])</code> should return <code>5</code></li>
<li id="test-5"><code>rob_circular([5, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>rob_circular([0, 0, 0, 0])</code> should return <code>0</code></li>
<li id="test-7"><code>rob_circular([6, 7, 1, 3, 8, 2, 4])</code> should return <code>19</code></li>
<li id="test-8">Performance: 200 houses in a circle, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def _rob_line(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr

def rob_circular(houses):
    if len(houses) == 1:
        return houses[0]
    return max(_rob_line(houses[1:]), _rob_line(houses[:-1]))
```

**Brute force:** try every take/skip choice around the circle and reject plans that rob two neighbors, including the first and last house. That's `O(2^n)`.

**Bottleneck:** the circle has no clear start, so the usual left-to-right DP doesn't apply directly. The only thing that's different from a straight line is the link between the first and last house.

**Optimal idea:** in any valid plan, the first house or the last house (or both) is left alone. If the first is skipped, the rest is a straight line, `houses[1:]`. If the last is skipped, it's `houses[:-1]`. Solve both lines with House Robber and take the larger.

**Why it's correct:** every valid circular plan is a valid plan for at least one of the two lines, and every plan for either line is valid in the circle, because each line leaves out one of the two houses that would close the loop. So the best of the two lines is the best circular plan.

**Complexity:** `O(n)` time for two linear passes. `O(n)` extra space for the two slices. Passing start and end indices instead would make it `O(1)`.

**Common mistakes:** forgetting the single-house case: both slices are empty and the answer comes out `0` instead of `houses[0]`. Running House Robber on the full list, which may rob both ends. Excluding both ends at once, which misses plans that rob one of them.

</details>
