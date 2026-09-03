---
lesson_name: Target Sum
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

### Target Sum

You are given a list of non-negative integers `nums` and an integer `target`. In front of each number you must place either a `+` or a `-` sign, then sum the whole expression. Write a function `count_target_sums(nums, target)` that returns how many different ways of assigning `+`/`-` signs make the expression evaluate to exactly `target`.

For example, with `nums = [1, 1, 1, 1, 1]` and `target = 3`, one valid assignment is `+1+1+1+1-1 = 3`; counting every sign combination that sums to `3` gives `count_target_sums([1, 1, 1, 1, 1], 3)` a return value of `5`.

---

### Tests

<ul>
<li id="test-1"><code>count_target_sums([1, 1, 1, 1, 1], 3)</code> should return <code>5</code></li>
<li id="test-2"><code>count_target_sums([1], 1)</code> should return <code>1</code></li>
<li id="test-3"><code>count_target_sums([1], 0)</code> should return <code>0</code></li>
<li id="test-4"><code>count_target_sums([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)</code> should return <code>256</code></li>
<li id="test-5"><code>count_target_sums([2, 3, 1, 4], 2)</code> should return <code>2</code></li>
<li id="test-6"><code>count_target_sums([1, 2, 1], 0)</code> should return <code>2</code></li>
</ul>
