---
lesson_name: Task Scheduler
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(len(tasks))
  space: O(number of distinct tasks)
hints:
  - "Which task is hardest to fit in? Think about the task that appears most often and the gaps it forces between its copies."
  - "Greedily run the most frequent task that's off cooldown (a max-heap of counts, see *Max-heap by negating* in *Heap / Priority Queue Basics*). Counting shows what that schedule looks like: the most frequent task makes `max_count - 1` blocks of `n + 1` slots, and other tasks fill the gaps."
  - "Template: count with `Counter`, find `max_count` and `num_max` (how many tasks have that count), and return `max(len(tasks), (max_count - 1) * (n + 1) + num_max)`."
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
<li id="test-7">Performance: 10,000 copies of one task plus 25 others, with <code>n = 1,000</code> (about 10 million slots), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter


def least_interval(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + num_max)
```

Here `m` is `len(tasks)`.

**Brute force:** simulate the CPU one slot at a time. In each slot, run the remaining task with the highest count that's off cooldown, or idle. That's correct, but the loop runs once per slot, idle ones included, and with a long cooldown the answer can be far bigger than `m`.

**Bottleneck:** most of those slots are idle, and the simulation steps through them one by one.

**Optimal idea:** count instead of simulating. The most frequent task, with count `max_count`, splits the schedule into `max_count - 1` blocks of `n + 1` slots, plus a last row holding every task that also has `max_count` copies (`num_max` of them). Other tasks fill the idle slots in the blocks. If there are more tasks than idle slots, no idle slot is needed at all, and the answer is just `len(tasks)`.

**Why it's correct:** the copies of the most frequent task need at least `n` slots between each pair, so `(max_count - 1) * (n + 1) + num_max` is a lower bound, and so is `len(tasks)`. Placing tasks round-robin into the blocks, most frequent first, never puts two copies of a task closer than `n + 1`, and reaches whichever bound is larger.

**Complexity:** `O(m)` time to count. `O(number of distinct tasks)` space for the counts, which is `O(1)` if the labels are letters. A max-heap simulation that jumps over idle stretches is also fast: `O(m log m)`.

**Common mistakes:** forgetting the `max(len(tasks), ...)`, which undercounts when there are many different tasks, as in `['a', 'b', 'c', 'd']`. Adding `1` for the last row instead of `num_max`, which is wrong when several tasks tie for the highest count.

</details>
