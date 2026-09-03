---
lesson_name: Container With Most Water
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

### Container With Most Water

You're given a list of non-negative integers, where each value represents the height of a vertical wall standing at that position. Picking any two walls forms a container whose width is the distance between their positions and whose height is limited by the shorter of the two walls. Write a function that returns the largest amount of water such a container could hold (width times height).

For example, with heights `[1, 7, 2, 5, 4, 7, 3]`, choosing the walls at positions `1` and `5` (heights `7` and `7`) gives a width of `4` and a height of `7`, holding `28` units of water — the best possible choice for this input.

---

### Tests

<ul>
<li id="test-1"><code>max_area([1, 7, 2, 5, 4, 7, 3])</code> should return <code>28</code></li>
<li id="test-2"><code>max_area([1, 1])</code> should return <code>1</code></li>
<li id="test-3"><code>max_area([4, 3, 2, 1, 4])</code> should return <code>16</code></li>
<li id="test-4"><code>max_area([1, 2, 1])</code> should return <code>2</code></li>
<li id="test-5"><code>max_area([0, 2])</code> should return <code>0</code></li>
<li id="test-6"><code>max_area([2, 3, 4, 5, 18, 17, 6])</code> should return <code>17</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        best = max(best, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
```

</details>
