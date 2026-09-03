---
lesson_name: Last Stone Weight
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

### Last Stone Weight

You are given a list of integers `stones`, where each value is the weight of one stone. Repeatedly take the two heaviest stones and smash them together: if their weights are equal, both stones are destroyed; otherwise the lighter stone is destroyed and the heavier one's weight is reduced by the lighter one's weight, then goes back into the pile. Keep smashing until at most one stone remains, and write a function `last_stone_weight(stones)` that returns the weight of the final remaining stone, or `0` if none remain.

For example, given `stones = [8, 4, 3, 2]`, smashing `8` and `4` leaves a `4`, so the pile becomes `[4, 3, 2]`. Smashing `4` and `3` leaves a `1`, giving `[2, 1]`. Smashing those leaves a single stone of weight `1`, so `last_stone_weight(stones)` returns `1`.

---

### Tests

<ul>
<li id="test-1"><code>last_stone_weight([8, 4, 3, 2])</code> should return <code>1</code></li>
<li id="test-2"><code>last_stone_weight([2, 7, 4, 1, 8, 1])</code> should return <code>1</code></li>
<li id="test-3"><code>last_stone_weight([1])</code> should return <code>1</code></li>
<li id="test-4"><code>last_stone_weight([])</code> should return <code>0</code></li>
<li id="test-5"><code>last_stone_weight([5, 5])</code> should return <code>0</code></li>
<li id="test-6"><code>last_stone_weight([10, 4, 2, 10])</code> should return <code>2</code></li>
<li id="test-7"><code>last_stone_weight([3, 3, 3, 3])</code> should return <code>0</code></li>
</ul>
