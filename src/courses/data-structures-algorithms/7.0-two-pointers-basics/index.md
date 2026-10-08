---
lesson_name: Two Pointers Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Two Pointers
---

## Why This Pattern Matters &#x1F4A1;

Two pointers walk through a sequence together and skip work a nested loop would repeat. With the right movement rule, an `O(n²)` "check every pair" search becomes a single `O(n)` pass, usually with `O(1)` extra memory.

## Spotting It &#x1F50D;

- The input is **sorted** (or sorting it is cheap and allowed).
- You're looking for a **pair/triplet** meeting a target sum.
- You need to compare things **from both ends** (palindromes, reversing in place).
- You need to **modify an array in place** (remove duplicates, move zeros).

## The Three Shapes &#x1F9F1;

### 1. Opposite ends, moving inward

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

On a **sorted** array, the movement rule decides which side to shrink:

```python
def pair_with_sum(nums, target):  # nums is sorted
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1    # need a bigger sum
        else:
            right -= 1   # need a smaller sum
```

### 2. Fast/slow (read/write) in the same direction

```python
def remove_duplicates(nums):  # sorted, in place
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write  # new length
```

`read` scans everything; `write` marks where the next keeper goes.

### 3. Fix one, two-pointer the rest

For triplets (*3Sum*), sort, loop a fixed index `i`, then run shape 1 on `nums[i+1:]`. That's `O(n²)` instead of `O(n³)`.

## Tips & Gotchas &#x1F4CC;

- **Use `left < right`**, not `<=`, when a pair needs two distinct elements.
- **Be able to say why moving a pointer is safe.** In *Container With Most Water*, you move the shorter wall because keeping it can never produce a bigger area.
- **Skip duplicates after a match** to avoid repeated answers:
  ```python
  while left < right and nums[left] == nums[left - 1]:
      left += 1
  ```
- **Sorting loses original indices.** If you need them, sort `(value, index)` pairs or use a hash map instead.
- **Clean strings on the fly** with `str.isalnum()` and `str.lower()` instead of building a new string, if you need `O(1)` space.
- Every iteration must move **at least one** pointer, or the loop never ends.
