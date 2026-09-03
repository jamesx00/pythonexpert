---
lesson_name: Car Fleet
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
</ul>
