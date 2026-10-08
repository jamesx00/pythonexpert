---
lesson_name: Find Median from Data Stream
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

### Find Median from Data Stream

Design a class `MedianFinder` that tracks the running median of a growing stream of numbers. Implement `add_num(num)`, which adds `num` to the stream, and `find_median()`, which returns the median of every number added so far. If an even number of values have been added, the median is the average of the two middle values.

For example, after calling `add_num(5)` and `add_num(1)`, the stream is `{5, 1}` and `find_median()` should return `3.0` (the average of `1` and `5`). Calling `add_num(3)` next makes the stream `{5, 1, 3}`, so `find_median()` should now return `3`, the single middle value.

---

### Tests

<ul>
<li id="test-1">add_num(5), add_num(1) &mdash; <code>find_median()</code> should return <code>3.0</code></li>
<li id="test-2">add_num(5), add_num(1), add_num(3) &mdash; <code>find_median()</code> should return <code>3</code></li>
<li id="test-3">add_num(2) &mdash; <code>find_median()</code> should return <code>2</code></li>
<li id="test-4">add_num(6), add_num(2), add_num(9), add_num(1) &mdash; <code>find_median()</code> should return <code>4.0</code></li>
<li id="test-5">add_num(-5), add_num(-2), add_num(-10) &mdash; <code>find_median()</code> should return <code>-5</code></li>
<li id="test-6">add_num(1), add_num(1), add_num(1), add_num(1) &mdash; <code>find_median()</code> should return <code>1.0</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated)
        self.large = []  # min-heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

</details>
