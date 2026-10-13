---
lesson_name: Largest Rectangle in Histogram
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Pick one bar and make it the *shortest* bar in the rectangle. How far left and right could the rectangle stretch?"
  - "It stretches until it hits a shorter bar on each side. A stack of bars with increasing heights (the *Monotonic stack* block in *Stack Basics*) finds those limits: a bar is popped exactly when a shorter bar arrives on its right."
  - "Template: keep `(start, height)` on the stack. For each new bar, pop every taller bar, computing `height * (i - start)` and moving this bar's `start` back to the popped one's. After the loop, every bar left on the stack extends to the end."
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

### Largest Rectangle in Histogram

Write a function `largest_rectangle_area(heights)` that takes a list of non-negative integers representing the bar heights of a histogram, where each bar has width `1` and the bars sit side by side, and returns the area of the largest rectangle that can be formed using contiguous bars.

The rectangle's height is limited by the shortest bar it spans, so a wide rectangle can only be as tall as its shortest included bar. For example, given `[2, 1, 5, 6, 2, 3]`, the best rectangle uses the two bars of height `5` and `6` at width `2`, giving an area of `10`.

---

### Tests

<ul>
<li id="test-1"><code>largest_rectangle_area([2, 1, 5, 6, 2, 3])</code> should return <code>10</code></li>
<li id="test-2"><code>largest_rectangle_area([2, 4])</code> should return <code>4</code></li>
<li id="test-3"><code>largest_rectangle_area([1, 1, 1, 1])</code> should return <code>4</code></li>
<li id="test-4"><code>largest_rectangle_area([6, 2, 5, 4, 5, 1, 6])</code> should return <code>12</code></li>
<li id="test-5"><code>largest_rectangle_area([5])</code> should return <code>5</code></li>
<li id="test-6"><code>largest_rectangle_area([0, 0, 0])</code> should return <code>0</code></li>
<li id="test-7">Performance: 100,000 bars, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def largest_rectangle_area(heights):
    stack = []  # (start_index, height)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area
```

**Brute force:** for every pair of left and right edges, track the lowest bar between them and compute the area. That's `O(n²)`.

**Bottleneck:** the rectangle limited by a bar's height only depends on the nearest shorter bar on each side, but the brute force rediscovers those limits over and over.

**Optimal idea:** keep a stack of bars with increasing heights, each with the leftmost index it can extend back to. When a shorter bar arrives, every taller bar on the stack has reached its right limit, so pop it and record its area.

**Why it's correct:** when a bar is popped at index `i`, `i` is the first shorter bar to its right. Its `start` is how far left it can extend, because everything popped before it was taller. So `height * (i - start)` is the widest rectangle with this bar as its shortest bar. The best rectangle has some shortest bar, and every bar's rectangle is measured.

**Complexity:** `O(n)` time, because each bar is pushed and popped at most once. `O(n)` space for the stack.

**Common mistakes:** forgetting the bars still on the stack after the loop. They extend to the end of the histogram, as in an increasing histogram, where nothing is popped during the loop. Using the popped bar's own index as the left edge instead of the earliest index it can reach.

</details>
