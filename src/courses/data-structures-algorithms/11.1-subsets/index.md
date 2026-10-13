---
lesson_name: Subsets
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(2ⁿ · n)
  space: O(n)
hints:
  - "Each element is either in a subset or not. How many subsets does that give, and how can you build them one decision at a time?"
  - "Use the *Include / exclude form* from *Backtracking Basics*: at index `i`, include `nums[i]` and recurse, pop it, then recurse without it. Record a copy of `path` when `i == len(nums)`."
  - "Template: `def dfs(i)`: if `i == len(nums)`, append `path[:]` and return. Otherwise `path.append(nums[i]); dfs(i + 1); path.pop(); dfs(i + 1)`. Or, without recursion: start from `[[]]` and for each `n`, add `subset + [n]` for every subset so far."
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

### Subsets

Write a function `subsets(nums)` that takes a list of distinct integers and returns every possible subset of that list, including the empty subset and the list itself. The result should be a list of lists, and neither the order of the subsets nor the order of elements within a subset needs to match any particular arrangement.

For example, given `[1, 2, 3]`, a valid return value would be `[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]` — eight subsets in total, since a set of 3 distinct elements has 2³ possible subsets.

---

### Tests

<ul>
<li id="test-1"><code>subsets([1, 2, 3])</code> should return <code>[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]</code> (any order)</li>
<li id="test-2"><code>subsets([])</code> should return <code>[[]]</code></li>
<li id="test-3"><code>subsets([5])</code> should return <code>[[], [5]]</code> (any order)</li>
<li id="test-4"><code>subsets([4, 7])</code> should return <code>[[], [4], [7], [4, 7]]</code> (any order)</li>
<li id="test-5"><code>subsets([0, -1])</code> should return <code>[[], [0], [-1], [0, -1]]</code> (any order)</li>
<li id="test-6"><code>subsets([1, 2, 3, 4])</code> should return all 16 subsets of <code>[1, 2, 3, 4]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def subsets(nums):
    result = [[]]
    for n in nums:
        result += [subset + [n] for subset in result]
    return result
```

**Brute force:** there isn't a faster idea to beat. The answer itself has `2ⁿ` subsets with up to `n` elements each, so every correct solution takes `O(2ⁿ · n)`. The question is only how to generate them cleanly.

**Bottleneck:** making sure every subset appears exactly once, without generating duplicates and removing them afterwards.

**Optimal idea:** decide element by element. Before looking at `n`, `result` holds every subset of the elements seen so far. Each of those either leaves `n` out (it's already in `result`) or takes it (`subset + [n]`). So adding a copy of each subset with `n` appended gives every subset of one more element. The recursive *Include / exclude* backtracking makes the same two choices per element.

**Why it's correct:** by induction, after processing the first `i` elements, `result` holds each of their `2ⁱ` subsets once. Every new subset either contains the next element or doesn't, and the two halves can't overlap. Since the elements are distinct, no two subsets are equal.

**Complexity:** `O(2ⁿ · n)` time: `2ⁿ` subsets, each built by copying up to `n` elements. `O(n)` extra space apart from the output (`O(n)` for the recursion depth in the backtracking version).

**Common mistakes:** writing `for subset in result: result.append(subset + [n])`, which loops forever because `result` keeps growing. The list comprehension builds the new subsets first, then adds them. In the backtracking version, appending `path` instead of `path[:]`.

</details>
