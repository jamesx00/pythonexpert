---
lesson_name: Jump Game II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Which stones can you reach with exactly one jump? With at most two? What do those sets look like?"
  - "The stones you can reach with `k` jumps form a block `0..cur_end`, as in *Track the farthest reach* in *Greedy Basics*. Scanning that block for the farthest landing spot gives the block for `k + 1` jumps."
  - "Template: `jumps = cur_end = farthest = 0`. For `i` in `range(len(nums) - 1)`: `farthest = max(farthest, i + nums[i])`, and if `i == cur_end`, add a jump and set `cur_end = farthest`. Return `jumps`."
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

### Jump Game II

Same stepping-stone setup as before: `nums[i]` is the farthest number of stones ahead you can leap from stone `i`, and it's guaranteed you can always reach the final stone. Write a function `min_jumps(nums)` that returns the minimum number of jumps needed to travel from stone `0` to the last stone in `nums`.

For example, `nums = [2, 3, 1, 1, 4]` can be solved in `2` jumps: `0 -> 1 -> 4`. A single-stone list like `nums = [0]` needs `0` jumps, since you're already standing on the last stone.

---

### Tests

<ul>
<li id="test-1"><code>min_jumps([2, 3, 1, 1, 4])</code> should return <code>2</code></li>
<li id="test-2"><code>min_jumps([0])</code> should return <code>0</code></li>
<li id="test-3"><code>min_jumps([1, 1, 1, 1])</code> should return <code>3</code></li>
<li id="test-4"><code>min_jumps([2, 1, 1, 1, 1])</code> should return <code>3</code></li>
<li id="test-5"><code>min_jumps([5, 1, 1, 1, 1])</code> should return <code>1</code></li>
<li id="test-6"><code>min_jumps([1, 2, 3])</code> should return <code>2</code></li>
<li id="test-7"><code>min_jumps([2, 3, 0, 1, 4])</code> should return <code>2</code></li>
<li id="test-8">Performance: 30,000 stones, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def min_jumps(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

**Brute force:** let `best[j]` be the fewest jumps to stone `j`. For each stone `i`, relax every stone it can land on: `best[j] = min(best[j], best[i] + 1)`. That's `O(n * m)` time, where `m` is the longest leap, so `O(n^2)` in the worst case, plus `O(n)` space.

**Bottleneck:** the DP works out an exact count for every stone, but stones you can reach in the same number of jumps form one block. Only the block's right end matters.

**Optimal idea:** do a breadth-first search over blocks. `cur_end` is the last stone reachable with `jumps` jumps. While scanning up to `cur_end`, track `farthest`, the farthest landing spot from any stone in that block. When the scan reaches `cur_end`, one more jump is needed, and the new block ends at `farthest`.

**Why it's correct:** this is a stays-ahead argument. With `k` jumps, the reachable stones are an unbroken block `0..end_k` (a leap can land on any stone up to its length, so no gaps). Any path with `k + 1` jumps leaves from some stone in that block, so it can't land past `max(i + nums[i])` over the block, which is exactly `end_{k + 1}`. So after every number of jumps, the greedy block reaches at least as far as any other strategy. The first `k` whose block covers the last stone is therefore the minimum. The loop stops before the last stone because you never jump *from* it.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** looping over all of `range(len(nums))`, which adds an extra jump when `cur_end` lands exactly on the last stone (`[0]` returns `1`). Always jumping to the stone with the biggest `nums[i]` instead of the biggest `i + nums[i]`.

</details>
