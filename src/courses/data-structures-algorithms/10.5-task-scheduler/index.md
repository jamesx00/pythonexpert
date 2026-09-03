---
lesson_name: Task Scheduler
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

### Task Scheduler

A CPU is given a list `tasks` of task labels (each a single character) to run, one per time slot. Between two occurrences of the *same* task label, at least `n` other time slots must pass, either running a different task or sitting idle. Write a function `least_interval(tasks, n)` that returns the minimum total number of time slots (including any idle slots) needed to run every task in `tasks` under this cooldown rule.

For example, with `tasks = ['a', 'a', 'a', 'b', 'b']` and `n = 2`, one valid schedule is `a, b, idle, a, b, idle, a`, which takes 7 slots — `least_interval(tasks, n)` should return `7`.

---

### Tests

<ul>
<li id="test-1"><code>least_interval(['a', 'a', 'a', 'b', 'b'], 2)</code> should return <code>7</code></li>
<li id="test-2"><code>least_interval(['a', 'a', 'a', 'b', 'b', 'b'], 0)</code> should return <code>6</code></li>
<li id="test-3"><code>least_interval(['a', 'a', 'a', 'a'], 3)</code> should return <code>13</code></li>
<li id="test-4"><code>least_interval(['a'], 5)</code> should return <code>1</code></li>
<li id="test-5"><code>least_interval(['a', 'b', 'c', 'd'], 2)</code> should return <code>4</code></li>
<li id="test-6"><code>least_interval(['a', 'a', 'b', 'b', 'c', 'c'], 2)</code> should return <code>6</code></li>
</ul>
