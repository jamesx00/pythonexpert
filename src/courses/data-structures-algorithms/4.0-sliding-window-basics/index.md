---
lesson_name: Sliding Window Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Sliding Window
---

## Why This Pattern Matters &#x1F4A1;

A sliding window is two pointers that mark a **contiguous range** `[left, right]`. Instead of recomputing every subarray from scratch (`O(n²)` or worse), you update the window as it moves: add the element entering on the right, remove the one leaving on the left. Each element enters and leaves once, so the whole scan is `O(n)`.

## Spotting It &#x1F50D;

- The problem mentions a **substring** or **subarray**, meaning contiguous elements.
- It asks for the **longest / shortest / count** of ranges meeting a condition.
- "At most k distinct", "without repeating", "contains all characters of", "window of size k".

## Two Kinds of Window &#x1F9F1;

### Fixed size `k`

```python
def max_sum_of_size_k(nums, k):
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]  # add new, drop old
        best = max(best, window)
    return best
```

### Variable size: grow right, shrink left

This template covers most window problems:

```python
def longest_without_repeat(s):
    seen = {}       # window state
    left = 0
    best = 0
    for right, ch in enumerate(s):
        seen[ch] = seen.get(ch, 0) + 1          # 1. expand
        while seen[ch] > 1:                     # 2. shrink while invalid
            seen[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)      # 3. record answer
    return best
```

Learn the three steps: **expand, shrink while invalid, record.**

- For **longest** problems, record after shrinking, once the window is valid again.
- For **shortest** problems (e.g., *Minimum Window Substring*), record *inside* the shrink loop while the window is still valid, then shrink to try for something smaller.

## Tips & Gotchas &#x1F4CC;

- **Window length is `right - left + 1`.** Off-by-one here is the most common bug.
- **Keep the window state cheap to update.** Use a `dict`/`Counter` of chars, a running sum, or a count of how many requirements are met (`have == need`). Don't re-scan the window on every step.
- **Shrink with `while`, not `if`.** One new element can require removing several old ones.
- Sliding window needs a condition that **stays broken as the window grows** (it's monotonic). With negative numbers, "sum ≤ k" isn't monotonic. Use prefix sums + a hash map instead.
- **Max in the window?** Use a monotonic `deque` of indices (*Sliding Window Maximum*). The front is always the max; pop from the back anything smaller than the new element.
- *Longest Repeating Character Replacement* trick: a window is valid when `length - max_freq <= k`.
