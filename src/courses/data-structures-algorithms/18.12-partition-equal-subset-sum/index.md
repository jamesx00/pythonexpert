---
lesson_name: Partition Equal Subset Sum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n * sum)
  space: O(sum)
hints:
  - "If the two halves have equal sums, what must each half add up to? So which question about subsets are you really asking?"
  - "Each half is `sum(nums) // 2` (an odd total means `False`). So ask: can some subset reach that target? Keep the set of sums you can reach so far, and grow it one number at a time. That's the DP recipe in *1-D Dynamic Programming Basics* with the state \"reachable sums\"."
  - "Template: if `total % 2`, return `False`. `target = total // 2`, `reachable = {0}`. For each `n`: `reachable |= {n + x for x in reachable if n + x <= target}`. Return `target in reachable`."
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

### Partition Equal Subset Sum

Write a function `can_partition(nums)` that takes a list of positive integers and returns `True` if the list can be split into two subsets whose elements sum to the same total, or `False` if no such split exists. Every element must belong to exactly one of the two subsets.

For example, given `nums = [1, 5, 11, 5]`, splitting into `[1, 5, 5]` and `[11]` gives two subsets that both sum to `11`, so the function should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>can_partition([1, 5, 11, 5])</code> should return <code>True</code></li>
<li id="test-2"><code>can_partition([1, 2, 3, 5])</code> should return <code>False</code></li>
<li id="test-3"><code>can_partition([1, 1])</code> should return <code>True</code></li>
<li id="test-4"><code>can_partition([1])</code> should return <code>False</code></li>
<li id="test-5"><code>can_partition([2, 2, 3, 5])</code> should return <code>False</code></li>
<li id="test-6"><code>can_partition([3, 3, 3, 4, 5])</code> should return <code>True</code></li>
<li id="test-7"><code>can_partition([2, 2, 2, 2, 3, 4, 5])</code> should return <code>True</code></li>
<li id="test-8">Performance: 61 even numbers whose total is 1,442, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = {0}
    for n in nums:
        dp |= {n + x for x in dp if n + x <= target}
    return target in dp
```

**Brute force:** try every subset and check its sum. That's `O(2^n)`: with 61 numbers it never finishes, even with pruning, when the answer is `False`.

**Bottleneck:** many different subsets have the same sum, and from then on they behave the same. The brute force keeps them all apart.

**Optimal idea:** the two halves must each sum to `target = total // 2`, so the question is whether some subset reaches `target`. Keep the set of sums that some subset of the numbers seen so far can make. Each new number `n` adds `x + n` for every sum `x` already in the set.

**Why it's correct:** a sum is reachable using the first `i` numbers if it's reachable without number `i`, or if it's `x + nums[i]` for some `x` reachable with the earlier ones. The update does exactly that. Sums above `target` can never come back down (all numbers are positive), so they can be dropped. If one subset reaches `target`, the rest makes the other half.

**Complexity:** `O(n * target)` time, since the set never holds more than `target + 1` sums, which is `O(n * sum)`. `O(sum)` space for the set. The same idea works with a list of booleans `dp[s]`, filled with `s` going down so each number is used once.

**Common mistakes:** forgetting the odd-total check. Adding to the set while iterating over it, which raises an error or uses one number twice: build the new sums first. With the boolean list, looping `s` upward lets one number be used many times.

</details>
