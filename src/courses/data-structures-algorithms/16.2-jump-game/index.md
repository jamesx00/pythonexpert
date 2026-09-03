---
lesson_name: Jump Game
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

### Jump Game

You're standing on stone `0` of a line of stepping stones described by `nums`, where `nums[i]` is the farthest number of stones ahead you're allowed to leap from stone `i`. Write a function `can_jump(nums)` that returns `True` if some sequence of jumps can carry you from stone `0` to the last stone in the list, and `False` otherwise.

For example, `nums = [2, 3, 1, 1, 4]` lets you jump `0 -> 1 -> 4`, reaching the final stone, so the answer is `True`. But `nums = [2, 0, 0, 1]` strands you at stone `1` or `2` with nowhere left to go, so the answer is `False`.

---

### Tests

<ul>
<li id="test-1"><code>can_jump([2, 3, 1, 1, 4])</code> should return <code>True</code></li>
<li id="test-2"><code>can_jump([2, 0, 0, 1])</code> should return <code>False</code></li>
<li id="test-3"><code>can_jump([0])</code> should return <code>True</code></li>
<li id="test-4"><code>can_jump([1, 0, 1, 0])</code> should return <code>False</code></li>
<li id="test-5"><code>can_jump([3, 2, 1, 0, 4])</code> should return <code>False</code></li>
<li id="test-6"><code>can_jump([1, 1, 1, 1])</code> should return <code>True</code></li>
<li id="test-7"><code>can_jump([5, 0, 0, 0, 0, 0])</code> should return <code>True</code></li>
</ul>
