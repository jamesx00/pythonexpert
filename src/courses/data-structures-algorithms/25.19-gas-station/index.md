---
lesson_name: Gas Station
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Pattern: *Greedy*."
  - "If you start at station `s` and run out of charge driving into station `i + 1`, could any station between `s` and `i` do better as a start?"
  - "Use *Reset when it can't work from here* from *Greedy Basics*: when the tank goes negative at `i`, move the start to `i + 1` and empty the tank. Separately, if the total of `gas - cost` is negative, no start works."
  - "Template: keep `total`, `tank` and `start = 0`. For each `i`, add `gas[i] - cost[i]` to both sums, and if `tank < 0`, set `start = i + 1` and `tank = 0`. Return `start if total >= 0 else -1`."
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
<li id="test-7"><code>can_complete_circuit([3, 1, 1], [1, 2, 2])</code> should return <code>0</code></li>
<li id="test-8">Performance: 20,000 stations, within 1 second</li>
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

**Brute force:** try every start and drive around the loop until the tank goes negative or you get back. That's `O(n^2)` time, `O(1)` space.

**Bottleneck:** when a start fails at station `i`, the brute force tries the next start and drives over the same stations again.

**Optimal idea:** drive once. Keep `tank` for the current start. When it goes negative at station `i`, give up on every start up to `i` and try `i + 1` with an empty tank. Keep `total`, the sum of all `gas[i] - cost[i]`, to decide at the end whether any start works.

**Why it's correct:** two facts.

1. *A failed run rules out all of its stations.* Say you start at `s` and the tank goes negative at `i`. Every station `k` between `s` and `i` was reached with a tank of at least `0`. Starting at `k` means arriving there with exactly `0`, which is no better, so that run also fails by `i`. So the answer can't be anywhere in `s..i`, and jumping `start` to `i + 1` skips nothing.
2. *If `total >= 0`, the last `start` works.* From `start` to the end of the list, the tank never goes negative, and it ends at some `t >= 0`. The stations before `start` split into failed runs, each with a negative sum. The tail of a failed run is negative too, because the part before it never went below `0`. So for any `j` before `start`, the stations `j + 1..start - 1` add up to at most `0`. After wrapping around and passing station `j`, your tank is `t` plus the sum of stations `0..j`, which is at least `t` plus the sum of `0..start - 1`, which is `total >= 0`. So the tank never goes negative on the way back either.

If `total < 0`, you burn more than you collect over the whole loop, so no start can work.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** setting `start = i` instead of `i + 1`. Returning `start` without checking `total`. Checking only `total >= 0` and returning `0`, which ignores where the shortfalls are.

</details>
