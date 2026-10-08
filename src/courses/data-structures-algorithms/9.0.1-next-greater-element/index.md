---
lesson_name: "Warm-up: Next Greater Element"
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

### Warm-up: Next Greater Element

Write a function `next_greater(nums)` that returns a list where position `i` holds the first number to the **right** of `nums[i]` that is strictly greater than it, or `-1` if there isn't one.

For example, `next_greater([2, 1, 3, 2, 4])` returns `[3, 3, 4, 4, -1]`.

**Hint:** use a monotonic stack of **indices** whose values are decreasing. When a new number is bigger than the value at the top of the stack, it's the answer for that index: pop it, record the answer, and keep popping while that's still true. Then push the current index.

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

The stack holds indices still waiting for a bigger number, and their values are decreasing from bottom to top. A new value `x` resolves every waiting index with a smaller value. Indices left on the stack at the end never found one, so they keep `-1`. Each index is pushed and popped at most once: `O(n)`.

</details>
