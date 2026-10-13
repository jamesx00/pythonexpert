---
lesson_name: Daily Temperatures
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When a warm day arrives, which earlier days has it just answered?"
  - "This is *Next Greater Element* again, but you record a distance instead of a value. Keep a stack of days still waiting for a warmer one (the *Monotonic stack* block in *Stack Basics*)."
  - "Template: for each `i, t`, while the day on top of the stack is colder than `t`, pop it as `j` and set `answer[j] = i - j`. Then push `i`."
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

### Daily Temperatures

Write a function `daily_temperatures(temps)` that takes a list of daily temperature readings and returns a list `answer` of the same length, where `answer[i]` is the number of days you'd have to wait after day `i` to see a strictly warmer day. If no future day is warmer, `answer[i]` should be `0`.

For example, given `[68, 70, 65, 72]`, day 0 (68) only has to wait 1 day to hit 70, day 1 (70) waits 2 days to hit 72, day 2 (65) waits 1 day to hit 72, and day 3 (72) never gets a warmer day, so the answer is `[1, 2, 1, 0]`.

---

### Tests

<ul>
<li id="test-1"><code>daily_temperatures([68, 70, 65, 72])</code> should return <code>[1, 2, 1, 0]</code></li>
<li id="test-2"><code>daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])</code> should return <code>[1, 1, 4, 2, 1, 1, 0, 0]</code></li>
<li id="test-3"><code>daily_temperatures([30, 40, 50, 60])</code> should return <code>[1, 1, 1, 0]</code></li>
<li id="test-4"><code>daily_temperatures([60, 50, 40, 30])</code> should return <code>[0, 0, 0, 0]</code></li>
<li id="test-5"><code>daily_temperatures([55])</code> should return <code>[0]</code></li>
<li id="test-6"><code>daily_temperatures([50, 50, 50])</code> should return <code>[0, 0, 0]</code></li>
<li id="test-7">Performance: 100,000 days of falling temperatures, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def daily_temperatures(temps):
    answer = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

**Brute force:** for each day, scan forward until a warmer day appears. When temperatures fall all the way, every scan reaches the end, so this is `O(n²)`.

**Bottleneck:** the same days are rescanned for many different starting days.

**Optimal idea:** scan once with a stack of days still waiting for a warmer day. Their temperatures decrease from bottom to top, so a warm day resolves the top few at once.

**Why it's correct:** a day waits on the stack until the first warmer day arrives, which pops it right away, so `i - j` is the wait until the *first* warmer day. Days never popped keep their default `0`.

**Complexity:** `O(n)` time, because each day is pushed once and popped at most once. `O(n)` space for the stack and the answer.

**Common mistakes:** popping on `<=`, which treats an equal temperature as warmer, as in `[50, 50, 50]`. Storing temperatures on the stack instead of indices, which loses the information needed to compute the wait.

</details>
