---
lesson_name: Find Median from Data Stream
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(log n) add_num, O(1) find_median
  space: O(n)
hints:
  - "The median splits the numbers into a lower half and an upper half. Which number from each half do you actually need?"
  - "Keep the lower half in a max-heap and the upper half in a min-heap, with sizes that differ by at most 1 (*Two heaps for a median* in *Heap / Priority Queue Basics*). The median is then at the top of one or both heaps."
  - "Template: in `add_num`, push `-num` to `small`, move `small`'s top to `large`, and if `large` is now bigger, move its top back to `small`. In `find_median`, return `-small[0]` if `small` is bigger, else `(-small[0] + large[0]) / 2`."
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
<li id="test-7">Performance: 100,000 <code>add_num</code> calls, each followed by <code>find_median</code>, within 1 second</li>
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

**Brute force:** keep every number in a list and sort it in each `find_median`, which is `O(n log n)` per call. Keeping the list sorted with `bisect.insort` makes `find_median` `O(1)`, but each insert still shifts up to `n` items, so `add_num` is `O(n)`.

**Bottleneck:** only the one or two middle values matter, but the whole list is kept in order.

**Optimal idea:** split the numbers into a lower half (`small`, a max-heap via negation) and an upper half (`large`, a min-heap). `small` has the same size as `large` or one more. The middle values are the two heap tops.

**Why it's correct:** every new number goes through `small` into `large`, so the largest of the lower half always moves up if it belongs there, and everything in `small` stays `<=` everything in `large`. The final step moves one number back if `large` got bigger, which restores the sizes. With an odd count the median is `small`'s top. With an even count it's the average of both tops.

**Complexity:** `O(log n)` per `add_num`: a constant number of heap pushes and pops. `O(1)` per `find_median`. `O(n)` space.

**Common mistakes:** forgetting to negate when reading `small[0]`. Only balancing the sizes, not the order, so a big number can end up in `small`. Using `//` instead of `/` for the even case, which turns `3.5` into `3`.

</details>
