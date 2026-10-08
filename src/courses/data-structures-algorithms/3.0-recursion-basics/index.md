---
lesson_name: Recursion Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Recursion
---

## Why This Matters &#x1F4A1;

A **recursive** function solves a problem by calling itself on a smaller version of the same problem. Trees, backtracking, divide-and-conquer sorting and dynamic programming are all built on recursion, so it's worth getting comfortable with it now, on easy problems, before those sections rely on it.

## The Two Parts of Every Recursive Function &#x1F9F1;

1. **Base case.** The smallest input, where you know the answer directly and don't recurse.
2. **Recursive case.** Break the input into a smaller piece, call the function on it, and combine the result.

```python
def sum_list(nums):
    if not nums:                         # base case: empty list sums to 0
        return 0
    return nums[0] + sum_list(nums[1:])  # recursive case: first + sum of the rest
```

If the recursive case doesn't move toward the base case, the function never stops. Python gives up after about 1,000 nested calls with a `RecursionError`.

## Trust the Recursion &#x1F91D;

When writing the recursive case, **assume the recursive call already works** for the smaller input. Don't trace it all the way down in your head. For `sum_list`, assume `sum_list(nums[1:])` correctly returns the sum of the rest. Then the only question is: "given that, how do I get the answer for the whole list?" Add `nums[0]`.

This is the same thinking you'll use for trees: "assume `height(node.left)` and `height(node.right)` are correct. How do I get the height of `node`?"

## The Call Stack &#x1F4DA;

Each call gets its own **stack frame** holding its own local variables. Calls stack up until a base case returns, then the frames unwind in reverse order:

```
sum_list([1, 2, 3])
└─ 1 + sum_list([2, 3])
       └─ 2 + sum_list([3])
              └─ 3 + sum_list([])
                     └─ returns 0
              └─ returns 3
       └─ returns 5
└─ returns 6
```

Tracing a small input like this by hand is the best way to debug recursive code. Write down each call's arguments, then fill in the return values from the bottom up.

## Common Shapes &#x1F50D;

### Shrink by one

```python
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
```

### Split in half

```python
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x
# O(log n) calls instead of O(n)
```

### Branch into several calls

```python
def count_paths(rows, cols):
    """Paths from the top-left to the bottom-right moving only right or down."""
    if rows == 1 or cols == 1:
        return 1
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)
```

Branching recursion can repeat the same work many times. `count_paths` recomputes the same sub-grids over and over, which makes it exponential. Caching the results (memoization) fixes that, and it's the starting point of the dynamic programming sections.

## Complexity of Recursive Code &#x23F1;&#xFE0F;

- **Time:** (number of calls) × (work per call, not counting the recursive calls).
- **Space:** the maximum depth of the call stack, plus whatever each frame stores.

`sum_list` makes `n + 1` calls, but each one slices the list (`O(n)`), so it's `O(n²)` time. Passing an index instead of slicing brings it down to `O(n)`:

```python
def sum_list(nums, i=0):
    if i == len(nums):
        return 0
    return nums[i] + sum_list(nums, i + 1)
```

## Tips & Gotchas &#x1F4CC;

- **Write the base case first.** Then check that every recursive call moves toward it.
- **Return the recursive result.** Calling `f(smaller)` without `return` (or without using its value) is the most common recursion bug.
- **Watch for hidden copies.** Slicing (`nums[1:]`) and string concatenation in every call add an `O(n)` cost per call.
- **Mind the depth.** Python's default limit is about 1,000 frames. For very deep inputs, an iterative version with an explicit stack is safer.
