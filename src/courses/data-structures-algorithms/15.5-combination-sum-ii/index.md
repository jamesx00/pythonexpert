---
lesson_name: Combination Sum II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(2ⁿ · n)
  space: O(n)
hints:
  - "This is *Combination Sum* where each element is used at most once, but the input has duplicates. Which two rules from earlier lessons does that combine?"
  - "Combine two rows of *How the variants differ* in *Backtracking Basics*: recurse with `i + 1` so each element is used once, and sort + skip `candidates[i] == candidates[i - 1]` when `i > start` so equal values don't start the same branch twice. Since the list is sorted, `break` once a candidate is bigger than what's left."
  - "Template: `candidates.sort()`. `def backtrack(start, remaining)`: if `remaining == 0`, record `path[:]`. For `i` from `start`: skip duplicates, `break` if `candidates[i] > remaining`, append, `backtrack(i + 1, remaining - candidates[i])`, pop."
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

### Combination Sum II

Write a function `combination_sum2(candidates, target)` that takes a list of positive integers (which may contain duplicate values) and a target value, and returns every unique combination of numbers from `candidates` that adds up exactly to `target`. Unlike a plain combination-sum search, each element of `candidates` may be used **at most once per combination** — but because the list can contain duplicate values, the same value may still appear more than once in a combination if it was listed more than once in `candidates`. No two combinations in the result should contain the same multiset of numbers, and the order of the combinations and the order of numbers within each combination do not matter.

For example, with `candidates = [2, 5, 2, 1, 2]` and `target = 5`, the valid combinations are `[1, 2, 2]` and `[5]` — note that `[2, 2, 1]` is the same combination as `[1, 2, 2]` and must not be listed twice.

---

### Tests

<ul>
<li id="test-1"><code>combination_sum2([2, 5, 2, 1, 2], 5)</code> should return <code>[[1, 2, 2], [5]]</code> (any order)</li>
<li id="test-2"><code>combination_sum2([2], 1)</code> should return <code>[]</code></li>
<li id="test-3"><code>combination_sum2([1, 1, 1], 2)</code> should return <code>[[1, 1]]</code></li>
<li id="test-4"><code>combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)</code> should return <code>[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]</code> (any order)</li>
<li id="test-5"><code>combination_sum2([3, 3, 3], 9)</code> should return <code>[[3, 3, 3]]</code></li>
<li id="test-6"><code>combination_sum2([4, 8], 20)</code> should return <code>[]</code></li>
<li id="test-7">Performance: 30 candidates (fifteen 1s, ten 2s, five 3s) with target 15, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def combination_sum2(candidates, target):
    candidates = sorted(candidates)
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result
```

**Brute force:** try every subset of positions, keep the ones that sum to `target`, and remove duplicates with a set of sorted tuples. That's `O(2ⁿ · n)`, and with many repeated values almost every hit is a duplicate. Fifteen 1s, ten 2s and five 3s with target 15 have only 27 distinct combinations, but millions of position choices reach them.

**Bottleneck:** equal values in different positions build the same combination again and again.

**Optimal idea:** sort, then search like *Subsets II* with a running total. Each level picks the next element from `start` onwards and recurses with `i + 1`, so each element is used at most once. Skipping `candidates[i]` when it equals `candidates[i - 1]` and `i > start` stops equal values from starting the same branch twice. Because the list is sorted, the loop can `break` as soon as a candidate is bigger than the remaining sum.

**Why it's correct:** a distinct combination is a count of each value. With equal values adjacent, the skip rule only allows taking the first `k` copies of a value, so each count pattern is built exactly once. The `break` only drops candidates that can't fit, and everything after them is at least as big.

**Complexity:** `O(2ⁿ · n)` time in the worst case (all values distinct), since each element is either used or not. Pruning by sum and skipping duplicates make it much faster in practice. `O(n)` extra space for the path and recursion, not counting the output.

**Common mistakes:** recursing with `i` instead of `i + 1`, which reuses the same element. Skipping with `i > 0` instead of `i > start`, which misses `[1, 1]` from `[1, 1, 1]`. Removing duplicate values from the input up front, which loses combinations like `[1, 2, 2]`.

</details>
