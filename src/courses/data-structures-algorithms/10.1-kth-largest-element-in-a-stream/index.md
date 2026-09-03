---
lesson_name: Kth Largest Element in a Stream
section: Heap / Priority Queue
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

### Kth Largest Element in a Stream

Design a class `KthLargest` that keeps track of the k-th largest value seen so far in a stream of integers. The constructor `KthLargest(k, nums)` is given the fixed size `k` and a starting list `nums` of values already seen. Each call to `add(val)` appends `val` to the stream and must return the current k-th largest value among everything added so far (including the starting `nums`).

For example, with `k = 2` and starting values `[3, 8]`, calling `add(5)` makes the stream `[3, 8, 5]`, whose 2nd largest value is `5`. A following `add(1)` leaves the 2nd largest unchanged at `5`, since `1` is too small to matter.

---

### Tests

<ul>
<li id="test-1">KthLargest(2, [3, 8]), add(5) &mdash; should return <code>5</code></li>
<li id="test-2">KthLargest(2, [3, 8]), add(5), add(1) &mdash; should return <code>5</code>, then <code>5</code></li>
<li id="test-3">KthLargest(2, [3, 8]), add(5), add(10) &mdash; should return <code>5</code>, then <code>8</code></li>
<li id="test-4">KthLargest(1, []), add(4), add(2), add(9) &mdash; should return <code>4</code>, then <code>4</code>, then <code>9</code></li>
<li id="test-5">KthLargest(3, [4, 5, 8, 2]), add(3), add(10) &mdash; should return <code>4</code>, then <code>5</code></li>
<li id="test-6">KthLargest(2, []), add(-1), add(-1), add(-2) &mdash; should return <code>-1</code>, then <code>-1</code>, then <code>-1</code></li>
</ul>
