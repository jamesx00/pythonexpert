---
lesson_name: Longest Consecutive Sequence
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Pattern: *Arrays & Hashing*."
  - "Sorting would put runs next to each other, but costs `O(n log n)`. Without sorting, how could you quickly check whether `x + 1` is among the values?"
  - "Put every value in a `set` (the *Seen-set* block in *Arrays & Hashing Basics*). Only count upward from values that *start* a run, i.e. where `x - 1` isn't in the set."
  - "Template: for each `x` in the set with `x - 1` missing, count `x + 1, x + 2, ...` while they're in the set, and keep the longest count."
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

### Longest Consecutive Sequence

Write a function `longest_consecutive(nums)` that takes a list of integers (in any order, possibly with duplicates) and returns the length of the longest run of consecutive integers that can be formed from the values in the list. A run of consecutive integers is a sequence like `4, 5, 6, 7` where each number is exactly one more than the previous, and the numbers do not need to appear next to each other in `nums`. Your solution should run in O(n) time.

For example, given `nums = [9, 1, 4, 2, 3, 100]`, the values `1, 2, 3, 4` form a run of length `4`, which is the longest one available, so `longest_consecutive(nums)` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>longest_consecutive([9, 1, 4, 2, 3, 100])</code> should return <code>4</code></li>
<li id="test-2"><code>longest_consecutive([])</code> should return <code>0</code></li>
<li id="test-3"><code>longest_consecutive([5])</code> should return <code>1</code></li>
<li id="test-4"><code>longest_consecutive([1, 2, 0, 1])</code> should return <code>3</code></li>
<li id="test-5"><code>longest_consecutive([10, 5, 12, 11, 6, 7])</code> should return <code>3</code></li>
<li id="test-6"><code>longest_consecutive([-2, -1, 0, 1, 2, 8])</code> should return <code>5</code></li>
<li id="test-7">Performance: one shuffled run of 100,000 consecutive values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
```

**Brute force:** for every value, count upward while the next value is present. With a list, each "is it present?" check is `O(n)`, so this is `O(n³)` in the worst case. Using a set for the checks still leaves `O(n²)`: in one run of length `n`, every value counts up through the rest of the run.

**Bottleneck:** a run of length `L` is counted again from each of its `L` values, though only the count from its smallest value matters.

**Optimal idea:** put the values in a set, and only start counting from `x` when `x - 1` isn't in the set, i.e. `x` is the first value of its run.

**Why it's correct:** every run has exactly one smallest value, and the count from there reaches the end of the run. So every run is measured once, in full, and the longest one is kept.

**Complexity:** `O(n)` time. Each value is checked as a start once, and the inner `while` loop visits each value at most once across all runs. `O(n)` space for the set.

**Common mistakes:** dropping the `x - 1 not in num_set` check, which makes the solution `O(n²)` on one long run. Looping over `nums` instead of `num_set` repeats work for duplicate values.

</details>
