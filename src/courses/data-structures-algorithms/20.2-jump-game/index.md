---
lesson_name: Jump Game
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If you can reach stone `5`, can you also reach stones `1` to `4`? What does that say about the set of stones you can reach?"
  - "Use *Track the farthest reach* from *Greedy Basics*: the reachable stones are always `0` to `reach`. If you get to a stone past `reach`, you're stuck."
  - "Template: `reach = 0`. For each `i, n`: if `i > reach`, return `False`, else `reach = max(reach, i + n)`. Return `True` after the loop."
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

### Jump Game

You're standing on stone `0` of a line of stepping stones described by `nums`, where `nums[i]` is the farthest number of stones ahead you're allowed to leap from stone `i`. Write a function `can_jump(nums)` that returns `True` if some sequence of jumps can carry you from stone `0` to the last stone in the list, and `False` otherwise.

For example, `nums = [2, 3, 1, 1, 4]` lets you jump `0 -> 1 -> 4`, reaching the final stone, so the answer is `True`. But `nums = [2, 0, 0, 1]` strands you at stone `1` or `2` with nowhere left to go, so the answer is `False`.

---

### Tests

<ul>
<li id="test-1"><code>can_jump([2, 3, 1, 1, 4])</code> should return <code>True</code></li>
<li id="test-2"><code>can_jump([2, 0, 0, 1])</code> should return <code>False</code></li>
<li id="test-3"><code>can_jump([0])</code> should return <code>True</code></li>
<li id="test-4"><code>can_jump([1, 0, 1, 0])</code> should return <code>False</code></li>
<li id="test-5"><code>can_jump([3, 2, 1, 0, 4])</code> should return <code>False</code></li>
<li id="test-6"><code>can_jump([1, 1, 1, 1])</code> should return <code>True</code></li>
<li id="test-7"><code>can_jump([5, 0, 0, 0, 0, 0])</code> should return <code>True</code></li>
<li id="test-8">Performance: 20,000 stones, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def can_jump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True
```

**Brute force:** keep a `reachable` list. For every reachable stone `i`, mark the stones `i + 1` to `i + nums[i]` as reachable. That's `O(n^2)` time when the leaps are long, and `O(n)` space. A recursive search that tries each leap without remembering stones is exponential.

**Bottleneck:** the brute force marks the same stones over and over. It only needs to know how far right the marks go.

**Optimal idea:** keep one number, `reach`: the farthest stone you can get to using the stones seen so far. Scan left to right and update it with `i + nums[i]`. If you hit a stone past `reach`, stop.

**Why it's correct:** the reachable stones always form an unbroken block `0..reach`. If a leap from stone `k` can land on stone `j`, it can also land on every stone between `k` and `j`, so there are no gaps. So stone `i` is reachable exactly when `i <= reach`. If `i > reach`, no earlier stone gets to `i` or beyond, and the stones from `i` on can't help because you can't stand on them. So the answer is `False`. If the scan finishes, every stone, including the last one, was within reach.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** updating `reach` from a stone you can't stand on, by checking `i > reach` *after* the update. Picking the biggest single leap (`nums[i]`) instead of the farthest landing spot (`i + nums[i]`).

</details>
