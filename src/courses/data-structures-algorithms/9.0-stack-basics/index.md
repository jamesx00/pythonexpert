---
lesson_name: Stack Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Stack
---

## Why This Pattern Matters &#x1F4A1;

A stack is last-in, first-out (LIFO): the most recent thing you pushed is the first thing you pop. That matches any problem where the **most recent unresolved item** is the one that matters next, such as matching brackets, undoing operations, or evaluating nested expressions.

In Python, a plain `list` is the stack:

```python
stack = []
stack.append(x)   # push      O(1)
top = stack[-1]   # peek      O(1)
stack.pop()       # pop       O(1)
if stack: ...     # non-empty check
```

## Spotting It &#x1F50D;

- **Matching pairs** or nesting: parentheses, tags, `decode "3[a2[c]]"`.
- **Evaluating** expressions (Reverse Polish Notation).
- "**Next greater / smaller** element", "how many days until a warmer temperature?"
- Keeping a running min/max alongside pushes and pops (*Min Stack*).

## Core Building Blocks &#x1F9F1;

### Matching brackets

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack  # leftovers mean unclosed brackets
```

### Monotonic stack: "next greater element"

Keep the stack sorted (here, decreasing). When a new value breaks the order, it's the answer for everything it pops.

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # holds INDICES, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            j = stack.pop()
            result[j] = x      # x is the next greater for j
        stack.append(i)
    return result
```

Each index is pushed and popped at most once, so this is `O(n)` despite the nested `while`.

## Tips & Gotchas &#x1F4CC;

- **Always check `if stack`** before `stack[-1]` or `stack.pop()`. Popping an empty list raises `IndexError`.
- **Store indices, not values**, in monotonic stacks. You can always look up the value, and the index lets you compute distances (*Daily Temperatures*: `i - j`).
- **Decreasing stack → next greater; increasing stack → next smaller.**
- **Flush at the end.** In *Largest Rectangle in Histogram*, append a sentinel `0` height so everything left on the stack gets processed.
- **Store pairs** when you need extra state per entry, e.g. `(value, current_min)` for *Min Stack*.
- **RPN division:** use `int(a / b)` to truncate toward zero. `a // b` floors, which is wrong for negatives.
- For a queue (FIFO), use `collections.deque`, not `list.pop(0)` (which is `O(n)`).
