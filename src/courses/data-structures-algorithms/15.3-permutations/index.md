---
lesson_name: Permutations
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n! · n)
  space: O(n)
hints:
  - "The first position can hold any of the `n` numbers. Once it's chosen, what's left to do?"
  - "Use the *Permutations* row of *How the variants differ* in *Backtracking Basics*: at every level, loop over *all* numbers from index `0` and skip the ones already in the path. When the path has `n` numbers, record a copy."
  - "Template: `def backtrack(path, remaining)`: if `remaining` is empty, record `list(path)`. For each `i`, append `remaining[i]`, recurse with `remaining[:i] + remaining[i + 1:]`, then pop."
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

### Permutations

Write a function `permute(nums)` that takes a list of distinct integers and returns every possible ordering of those integers. The result should be a list of lists, one for each permutation, and the order in which the permutations appear does not matter.

For example, given `[1, 2, 3]`, the function should return all 6 orderings: `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`, in any order.

---

### Tests

<ul>
<li id="test-1"><code>permute([1, 2, 3])</code> should return <code>[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]</code> (any order)</li>
<li id="test-2"><code>permute([0])</code> should return <code>[[0]]</code></li>
<li id="test-3"><code>permute([])</code> should return <code>[[]]</code></li>
<li id="test-4"><code>permute([4, 5])</code> should return <code>[[4, 5], [5, 4]]</code> (any order)</li>
<li id="test-5"><code>permute([1, -1])</code> should return <code>[[1, -1], [-1, 1]]</code> (any order)</li>
<li id="test-6"><code>permute([1, 2, 3, 4])</code> should return all 24 permutations of <code>[1, 2, 3, 4]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(list(path))
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result
```

**Brute force:** there's no faster algorithm to aim for. There are `n!` permutations of length `n`, so any solution takes `O(n! · n)` just to write them out. Generating all `nⁿ` sequences and keeping the ones without repeats also works, but wastes most of its time.

**Bottleneck:** avoiding sequences that reuse a number, without building them first.

**Optimal idea:** fill the positions one at a time. Each level picks one of the numbers not used yet, recurses on the rest, then puts it back. Passing the unused numbers down as `remaining` means a used number can never be picked again.

**Why it's correct:** a permutation is a choice of first number followed by a permutation of the rest. The loop tries every first number, and the recursion produces every permutation of what's left, so each permutation is built exactly once. Because the numbers are distinct, no two are equal.

**Complexity:** `O(n! · n)` time: `n!` leaves, and the slicing and copying cost `O(n)` along each path. `O(n)` extra space for the path and recursion depth, plus the `remaining` lists, not counting the output.

**Common mistakes:** looping from a `start` index as in subsets, which only produces one ordering. Forgetting `path.pop()`. A common alternative uses a `used` list of booleans instead of slicing `remaining`, which is fine too, as long as `used[i]` is reset after the recursive call.

</details>
