---
lesson_name: Trapping Rain Water
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Look at a single position. How high can water stand above it, in terms of the walls to its left and right?"
  - "Water at position `i` rises to `min(highest wall on the left, highest wall on the right)`, minus `heights[i]`. You can precompute both maximums in two passes, or track them with two pointers: whichever side has the lower maximum so far already knows its water level."
  - "Template: opposite-ends pointers (shape 1 in *Two Pointers Basics*) with `left_max` and `right_max`. If `left_max <= right_max`, step `left` inward, update `left_max`, and add `left_max - heights[left]`. Otherwise do the same on the right."
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

### Trapping Rain Water

You're given a list of non-negative integers representing the height of a bumpy floor, one unit wide per position. After rain, water settles into the dips between higher ground on either side. Write a function that returns the total number of water units the floor can trap.

For example, with heights `[0, 1, 0, 2, 1, 0, 3, 1, 0, 2]`, water collects above the low spots between the taller bars, trapping `7` units total in this case.

---

### Tests

<ul>
<li id="test-1"><code>trap_rain_water([0, 1, 0, 2, 1, 0, 3, 1, 0, 2])</code> should return <code>7</code></li>
<li id="test-2"><code>trap_rain_water([4, 2, 3])</code> should return <code>1</code></li>
<li id="test-3"><code>trap_rain_water([1, 1, 1])</code> should return <code>0</code></li>
<li id="test-4"><code>trap_rain_water([5, 4, 1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>trap_rain_water([])</code> should return <code>0</code></li>
<li id="test-6"><code>trap_rain_water([3, 0, 0, 2, 0, 4])</code> should return <code>10</code></li>
<li id="test-7">Performance: 100,000 positions, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def trap_rain_water(heights):
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water = 0
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
    return water
```

**Brute force:** for each position, scan left for the tallest wall and scan right for the tallest wall, then add `min(left_max, right_max) - heights[i]`. Each position rescans the list, so this is `O(n²)` time.

**Bottleneck:** the left and right maximums for neighbouring positions are almost the same, but they're recomputed from scratch every time.

**Optimal idea:** precomputing `left_max[i]` and `right_max[i]` in two passes gives `O(n)` time with `O(n)` space. Two pointers do it in `O(1)` space: keep `left_max` and `right_max`, and always move inward from the side whose maximum is lower.

**Why it's correct:** suppose `left_max <= right_max`. The tallest wall on the right of position `left` is at least `right_max`, so it's at least `left_max`. The water level at `left` is the smaller of the two sides, which is `left_max`. That's known already, so the water at `left` can be added and the pointer moved on. The other case is symmetric.

**Complexity:** `O(n)` time, because each step moves one pointer. `O(1)` extra space.

**Common mistakes:** adding water before updating `left_max`, which can add a negative amount when the new bar is taller. Using the overall maximum of the whole list as the water level everywhere.

</details>
