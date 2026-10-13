---
lesson_name: Subsets II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(2ⁿ · n)
  space: O(n)
hints:
  - "With `[1, 2, 2]`, choosing \"the first 2\" or \"the second 2\" gives the same subset. Where in the search do those two choices happen?"
  - "Use the *Subsets II* row of *How the variants differ* in *Backtracking Basics*: sort the input, then in the loop skip `nums[i]` when `i > start and nums[i] == nums[i - 1]`. Copies of a value can still be taken one after another, just never as the first pick at the same level."
  - "Template: `nums.sort()`. `def backtrack(start)`: record `path[:]` first. For `i` from `start`: skip duplicates as above, append `nums[i]`, `backtrack(i + 1)`, pop."
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

### Subsets II

Write a function `subsets_with_dup(nums)` that takes a list of integers which may contain duplicate values, and returns every distinct subset of that list (including the empty subset and the full list). Even though the same value can appear more than once in `nums`, no two subsets in the result should contain the exact same multiset of values. The order of the subsets and the order of elements within each subset do not matter.

For example, given `[1, 2, 2]`, the subsets `[2]` picked from either copy of `2` are the same subset and must only appear once, so a valid return value is `[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]`.

---

### Tests

<ul>
<li id="test-1"><code>subsets_with_dup([1, 2, 2])</code> should return <code>[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]</code> (any order)</li>
<li id="test-2"><code>subsets_with_dup([0])</code> should return <code>[[], [0]]</code></li>
<li id="test-3"><code>subsets_with_dup([])</code> should return <code>[[]]</code></li>
<li id="test-4"><code>subsets_with_dup([4, 4, 4])</code> should return <code>[[], [4], [4, 4], [4, 4, 4]]</code> (any order)</li>
<li id="test-5"><code>subsets_with_dup([1, 2, 3])</code> should return <code>[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]</code> (any order)</li>
<li id="test-6"><code>subsets_with_dup([2, 1, 2, 1])</code> should return <code>[[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]</code> (any order)</li>
<li id="test-7">Performance: 22 values, <code>[1, 2]</code> repeated 11 times (144 distinct subsets), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def subsets_with_dup(nums):
    nums = sorted(nums)
    result = []

    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

**Brute force:** generate all `2ⁿ` subsets as in *Subsets*, sort each one, and keep them in a set to drop duplicates. That's `O(2ⁿ · n)` no matter how many distinct subsets there are. For `[1, 2]` repeated 11 times it builds about 4 million subsets to find 144.

**Bottleneck:** with many repeated values, almost every generated subset is a duplicate.

**Optimal idea:** sort the input so equal values sit together, and never start a branch with the same value twice at the same level. At each level, the loop picks the next element of the subset. If `nums[i]` equals `nums[i - 1]` and `i > start`, picking it here would build exactly the subsets already built by picking `nums[i - 1]`, so skip it.

**Why it's correct:** a distinct subset is described by how many copies of each value it uses. Because copies are adjacent, taking `k` copies of a value always means taking the first `k` of them, one after another, and the skip rule only allows that version. So each distinct subset is built exactly once. Every node is recorded, since every partial path is itself a subset.

**Complexity:** `O(2ⁿ · n)` time in the worst case (all values distinct), but the search only visits distinct subsets, so it's proportional to the size of the output times `n`. `O(n)` extra space for the path and recursion, not counting the output.

**Common mistakes:** forgetting to sort, so duplicates aren't adjacent and the skip misses them. Writing `i > 0` instead of `i > start`, which also skips the second `2` in `[2, 2]` and loses that subset.

</details>
