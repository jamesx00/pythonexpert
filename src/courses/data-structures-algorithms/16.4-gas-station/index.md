---
lesson_name: Gas Station
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

### Gas Station

There are `n` charging stations arranged in a circle. `gas[i]` is the amount of charge you pick up at station `i`, and `cost[i]` is the amount of charge burned driving from station `i` to the next station (station `n - 1` connects back around to station `0`). Write a function `can_complete_circuit(gas, cost)` that returns the index of the station you should start from to complete the full loop without your charge ever dropping below zero, or `-1` if no such starting station exists. You may assume there is at most one valid starting index.

For example, `gas = [1, 2, 3, 4, 5]` and `cost = [3, 4, 5, 1, 2]` lets you start at station `3` and make it all the way around. But `gas = [2, 3, 4]` and `cost = [3, 4, 3]` has no valid starting point, since the total charge collected never covers the total cost, so the answer is `-1`.

---

### Tests

<ul>
<li id="test-1"><code>can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])</code> should return <code>3</code></li>
<li id="test-2"><code>can_complete_circuit([2, 3, 4], [3, 4, 3])</code> should return <code>-1</code></li>
<li id="test-3"><code>can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])</code> should return <code>4</code></li>
<li id="test-4"><code>can_complete_circuit([3, 3, 4], [3, 4, 4])</code> should return <code>-1</code></li>
<li id="test-5"><code>can_complete_circuit([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9])</code> should return <code>-1</code></li>
<li id="test-6"><code>can_complete_circuit([7], [6])</code> should return <code>0</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def can_complete_circuit(gas, cost):
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
```

</details>
