---
lesson_name: Greedy Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Greedy
---

## Why This Pattern Matters &#x1F4A1;

A greedy algorithm makes the **locally best choice** at each step and never reconsiders it. When that works, it's usually a single `O(n)` pass (or `O(n log n)` after sorting). The hard part is not the code. It's convincing yourself the local choice can never hurt the final answer.

## Spotting It &#x1F50D;

- A DP solution exists, but the DP only ever keeps one "best so far" value.
- "Can you reach the end?", "minimum number of jumps/groups", "maximum subarray".
- Sorting by some key makes the right choice obvious.

## Core Building Blocks &#x1F9F1;

### Running best (Kadane's algorithm)

```python
def max_subarray(nums):
    best = curr = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)   # extend, or start fresh if the past drags us down
        best = max(best, curr)
    return best
```

### Track the farthest reach

```python
def can_jump(nums):
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False           # stuck before index i
        reach = max(reach, i + step)
    return True
```

### Reset when it can't work from here

In *Gas Station*, if the tank goes negative at station `i`, no station between the current start and `i` can be a valid start either, so jump the start to `i + 1`.

## Tips & Gotchas &#x1F4CC;

- **Try to break your greedy rule.** Spend a minute looking for a counter-example. If you find one, the problem probably needs DP.
- **Exchange argument:** to justify a choice, show that swapping it for any other choice never makes the answer better.
- **Sort first** when order is up to you: by end time for scheduling, by start time for merging, by value for grouping (*Hand of Straights*).
- **Record last positions** (`last[ch] = i`) to know how far a group must extend (*Partition Labels*).
- **Keep a range instead of one value** when a choice is ambiguous. In *Valid Parenthesis String*, track the min and max possible open-bracket count.
- **Check impossible cases up front**, e.g. `sum(gas) < sum(cost)` or `len(hand) % group_size != 0`.
