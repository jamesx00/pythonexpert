---
lesson_name: Car Fleet
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "Pattern: *Stack*."
  - "A car can only be slowed down by cars *ahead* of it. In what order would you look at the cars?"
  - "Sort the cars by position, closest to the target first, and compute each car's arrival time if it drove alone: `(target - position) / speed`. A car that would arrive no later than the fleet in front catches it and joins it."
  - "Template: walk the sorted cars, tracking the slowest arrival time so far. A car whose time is greater starts a new fleet and becomes the new slowest time. (A stack of fleet times, as in *Stack Basics*, works the same way.)"
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

### Car Fleet

`n` cars are driving toward the same destination along a single-lane road, all heading in the same direction. Write a function `car_fleet(target, positions, speeds)` that returns the number of "fleets" that will arrive at the destination.

`target` is the distance to the finish line. `positions[i]` is the starting position of car `i` (all positions are distinct and less than `target`), and `speeds[i]` is that car's constant speed. A car can never pass the car ahead of it — if a faster car catches up to a slower car in front of it before the slower car finishes, they merge and continue at the slower car's speed as one fleet, arriving together. Each car that never catches up to another (and isn't caught) forms its own fleet of one.

For example, with `target = 10`, `positions = [0, 4]`, and `speeds = [2, 1]`: the car at position 0 travels at speed 2 and would reach position 4 after 2 time units, but the car ahead (starting at 4, speed 1) is still moving, so it never actually passes — it catches up and they merge into a single fleet, giving an answer of `1`.

---

### Tests

<ul>
<li id="test-1"><code>car_fleet(10, [0, 4], [2, 1])</code> should return <code>1</code></li>
<li id="test-2"><code>car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])</code> should return <code>3</code></li>
<li id="test-3"><code>car_fleet(100, [0, 2, 4], [4, 2, 1])</code> should return <code>1</code></li>
<li id="test-4"><code>car_fleet(10, [3], [3])</code> should return <code>1</code></li>
<li id="test-5"><code>car_fleet(20, [0, 5, 10, 15], [1, 1, 1, 1])</code> should return <code>4</code></li>
<li id="test-6">Performance: 100,000 cars, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def car_fleet(target, positions, speeds):
    cars = sorted(zip(positions, speeds), reverse=True)
    fleets = 0
    max_time = 0
    for pos, speed in cars:
        time = (target - pos) / speed
        if time > max_time:
            fleets += 1
            max_time = time
    return fleets
```

**Brute force:** for each car, check every car ahead of it to see whether any of them arrives later and would hold it up. A car that isn't held up leads its own fleet. That's `O(n²)`.

**Bottleneck:** each car compares itself with every car ahead, but only the slowest arrival time ahead of it matters.

**Optimal idea:** sort the cars from the front of the road to the back and keep the slowest arrival time seen so far. A car leads a new fleet only if it would arrive later than that.

**Why it's correct:** a car arriving no later than some car ahead catches up before the target and is then held to that fleet's pace, so it can't start a fleet of its own. A car arriving strictly later never catches anything ahead, so it leads a new fleet, and its time becomes the one the cars behind must beat.

**Complexity:** `O(n log n)` time for the sort, plus `O(n)` for the scan. `O(n)` space for the sorted list.

**Common mistakes:** sorting from the back of the road instead of the front. Using `>=` instead of `>`, which counts a car that arrives exactly with the fleet ahead as a separate fleet. Integer division for the times, which makes different arrival times look equal.

</details>
