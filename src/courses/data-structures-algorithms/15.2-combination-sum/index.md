---
lesson_name: Combination Sum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n^(t/m))
  space: O(t / m)
hints:
  - "`[2, 3, 3]` and `[3, 2, 3]` are the same combination. How do you build each one in only one order, while still letting a number repeat?"
  - "Use the *Combination Sum (reuse allowed)* row of *How the variants differ* in *Backtracking Basics*: loop from `start` and recurse with `backtrack(i)`, not `i + 1`, so the same number can be picked again but nothing earlier can. Sort first, and `break` as soon as a candidate is bigger than what's left."
  - "Template: `candidates.sort()`. `def backtrack(start, remaining)`: if `remaining == 0`, record `path[:]`. For `i` from `start`: if `candidates[i] > remaining`, `break`. Append, `backtrack(i, remaining - candidates[i])`, pop."
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

### Combination Sum

Write a function `combination_sum(candidates, target)` that takes a list of distinct positive integers and a target value, and returns every unique combination of numbers from `candidates` that adds up exactly to `target`. A number may be reused as many times as needed within a single combination, but the same multiset of numbers must not appear twice in the result. Both the order of the combinations and the order of numbers within each combination are unimportant.

For example, with `candidates = [2, 3, 5]` and `target = 8`, valid combinations include `[2, 2, 2, 2]`, `[2, 3, 3]`, and `[3, 5]`, so the function should return exactly those three combinations (in any order).

---

### Tests

<ul>
<li id="test-1"><code>combination_sum([2, 3, 5], 8)</code> should return <code>[[2, 2, 2, 2], [2, 3, 3], [3, 5]]</code> (any order)</li>
<li id="test-2"><code>combination_sum([2], 1)</code> should return <code>[]</code></li>
<li id="test-3"><code>combination_sum([1], 3)</code> should return <code>[[1, 1, 1]]</code></li>
<li id="test-4"><code>combination_sum([3, 4, 6], 12)</code> should return <code>[[3, 3, 3, 3], [3, 3, 6], [4, 4, 4], [6, 6]]</code> (any order)</li>
<li id="test-5"><code>combination_sum([7, 11], 5)</code> should return <code>[]</code></li>
<li id="test-6"><code>combination_sum([2, 4], 8)</code> should return <code>[[2, 2, 2, 2], [2, 2, 4], [4, 4]]</code> (any order)</li>
<li id="test-7">Performance: candidates <code>[2, 3, 5, 7]</code> with target 50 (158 combinations), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def combination_sum(candidates, target):
    candidates = sorted(candidates)
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result
```

Here `n` is the number of candidates, `t` the target, and `m` the smallest candidate, so a combination has at most `t / m` numbers.

**Brute force:** at each step try every candidate, recurse until the sum reaches the target, and put each result into a set as a sorted tuple to remove duplicates. This builds every *ordering* of every combination, so `[2, 3, 3]` is found three times. With `[2, 3, 5, 7]` and target 50 there are only 158 combinations, but a huge number of orderings.

**Bottleneck:** the same combination is built in every order, then thrown away.

**Optimal idea:** build each combination in non-decreasing order of index. Each call only picks candidates from `start` onwards, and recursing with `i` (not `i + 1`) lets the same candidate be picked again. Sorting the candidates lets the loop `break` as soon as one is too big, because every later one is bigger.

**Why it's correct:** every combination has exactly one ordering whose indices never go down, and the `start` argument only builds those, so each combination appears once. Nothing valid is pruned: once `candidates[i] > remaining`, no candidate from `i` on can fit.

**Complexity:** exponential, `O(n^(t/m))` in the worst case: the search tree has depth at most `t / m` and up to `n` branches per node. In practice it's far smaller, because the order rule and the `break` cut most branches. `O(t / m)` extra space for the path and the recursion, not counting the output.

**Common mistakes:** recursing with `i + 1`, which stops numbers from repeating and misses `[2, 2, 2, 2]`. Looping from `0` instead of `start`, which gives duplicates in different orders. Appending `path` instead of a copy.

</details>
