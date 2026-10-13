---
lesson_name: "Warm-up: Next Greater Element"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When a new number arrives, which earlier numbers has it just become the answer for?"
  - "Keep a stack of indices still waiting for an answer, with decreasing values (the *Monotonic stack* block in *Stack Basics*). When `nums[i]` is bigger than the value on top, it's that index's answer: pop, record, and repeat. Then push `i`."
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

### Warm-up: Next Greater Element

Write a function `next_greater(nums)` that returns a list where position `i` holds the first number to the **right** of `nums[i]` that is strictly greater than it, or `-1` if there isn't one.

For example, `next_greater([2, 1, 3, 2, 4])` returns `[3, 3, 4, 4, -1]`.

---

### Tests

<ul>
<li id="test-1"><code>next_greater([2, 1, 3, 2, 4])</code> should return <code>[3, 3, 4, 4, -1]</code></li>
<li id="test-2"><code>next_greater([5, 4, 3])</code> should return <code>[-1, -1, -1]</code></li>
<li id="test-3"><code>next_greater([1, 2, 3])</code> should return <code>[2, 3, -1]</code></li>
<li id="test-4"><code>next_greater([])</code> should return <code>[]</code></li>
<li id="test-5"><code>next_greater([7])</code> should return <code>[-1]</code></li>
<li id="test-6"><code>next_greater([3, 3, 4])</code> should return <code>[4, 4, -1]</code></li>
<li id="test-7"><code>next_greater([4, 1, 2, 5, 3])</code> should return <code>[5, 2, 5, -1, -1]</code></li>
<li id="test-8">Performance: 100,000 falling values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result
```

**Brute force:** for each index, scan to the right until a bigger value appears. On a falling list every scan runs to the end, so this is `O(n²)`.

**Bottleneck:** the same stretch of the list is rescanned for many different indices.

**Optimal idea:** scan once, keeping a stack of indices that haven't found a bigger value yet. Their values decrease from bottom to top, so a new value resolves the top few at once.

**Why it's correct:** an index waits on the stack until the first bigger value to its right arrives, and that value pops it immediately, so the recorded answer is the *first* greater value. Indices never popped keep their default `-1`.

**Complexity:** `O(n)` time, because each index is pushed once and popped at most once. `O(n)` space for the stack and the result.

**Common mistakes:** pushing values instead of indices, which leaves no way to know where to write the answer. Popping on `<=` instead of `<`, which treats an equal value as greater, as in `[3, 3, 4]`.

</details>
