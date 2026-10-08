---
lesson_name: Binary Search Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Binary Search
---

## Why This Pattern Matters &#x1F4A1;

Binary search halves the search space every step: `O(log n)` instead of `O(n)`. A million elements take about 20 checks. It works on more than sorted arrays. It works on **any yes/no question whose answers flip exactly once**, like `False False False True True`.

## Spotting It &#x1F50D;

- The input is **sorted** (or sorted then rotated).
- The problem asks for `O(log n)`.
- "Find the **minimum/maximum value** such that ___ is possible." If checking one candidate is easy and feasibility is monotonic, binary search **the answer** (*Koko Eating Bananas*).

## Core Templates &#x1F9F1;

### 1. Find an exact value

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### 2. Find the first position where a condition becomes true

This is the more versatile template. Use it for lower bounds, insertion points, and "minimum feasible answer" problems.

```python
def first_true(lo, hi, condition):
    # assumes condition(hi) is True
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid        # mid might be the answer, keep it
        else:
            lo = mid + 1    # mid is definitely not it
    return lo
```

For example, the minimum eating speed:

```python
import math

def min_speed(piles, h):
    def can_finish(k):
        return sum(math.ceil(p / k) for p in piles) <= h
    return first_true(1, max(piles), can_finish)
```

## Tips & Gotchas &#x1F4CC;

- **Match the loop and the updates:**
  - `while lo <= hi` goes with `lo = mid + 1` / `hi = mid - 1` (exact search).
  - `while lo < hi` goes with `hi = mid` / `lo = mid + 1` (boundary search).
  Mixing them causes infinite loops or skipped answers.
- **Test with a 2-element range.** If `lo = mid` is ever possible, `mid` must round up (`(lo + hi + 1) // 2`), or the loop gets stuck.
- **Rotated arrays:** at least one half around `mid` is always sorted. Check which half is sorted, then whether the target falls inside it.
- **2-D matrix** treated as one long sorted list: `row, col = divmod(mid, cols)`.
- **Python's `bisect`** module has these built in: `bisect_left(a, x)` is the first index with `a[i] >= x`, and `bisect_right` is the first with `a[i] > x`.
- Python ints don't overflow, so `(lo + hi) // 2` is fine. In other languages you'll see `lo + (hi - lo) // 2`.
