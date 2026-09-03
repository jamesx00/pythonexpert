---
lesson_name: Jump Game II
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

### Jump Game II

Same stepping-stone setup as before: `nums[i]` is the farthest number of stones ahead you can leap from stone `i`, and it's guaranteed you can always reach the final stone. Write a function `min_jumps(nums)` that returns the minimum number of jumps needed to travel from stone `0` to the last stone in `nums`.

For example, `nums = [2, 3, 1, 1, 4]` can be solved in `2` jumps: `0 -> 1 -> 4`. A single-stone list like `nums = [0]` needs `0` jumps, since you're already standing on the last stone.

---

### Tests

<ul>
<li id="test-1"><code>min_jumps([2, 3, 1, 1, 4])</code> should return <code>2</code></li>
<li id="test-2"><code>min_jumps([0])</code> should return <code>0</code></li>
<li id="test-3"><code>min_jumps([1, 1, 1, 1])</code> should return <code>3</code></li>
<li id="test-4"><code>min_jumps([2, 1, 1, 1, 1])</code> should return <code>3</code></li>
<li id="test-5"><code>min_jumps([5, 1, 1, 1, 1])</code> should return <code>1</code></li>
<li id="test-6"><code>min_jumps([1, 2, 3])</code> should return <code>2</code></li>
<li id="test-7"><code>min_jumps([2, 3, 0, 1, 4])</code> should return <code>2</code></li>
</ul>
