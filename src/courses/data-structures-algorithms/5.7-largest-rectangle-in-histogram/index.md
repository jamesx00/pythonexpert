---
lesson_name: Largest Rectangle in Histogram
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
</ul>
