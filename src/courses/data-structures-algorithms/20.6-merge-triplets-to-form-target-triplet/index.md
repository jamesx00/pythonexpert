---
lesson_name: Merge Triplets to Form Target Triplet
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Merging takes the max, so values can only go up. Which triplets can you never merge without ruining the result?"
  - "A triplet with any value above the target's is useless, since that value can't come down again. Every other triplet is safe to merge, so merge them all and see if you hit the target. This is the *Exchange argument* idea from *Greedy Basics*: adding a safe triplet never makes the result worse."
  - "Template: `best = [0, 0, 0]`. For each `t` with `t[i] <= target[i]` for all three `i`, set `best[i] = max(best[i], t[i])`. Return `best == target`."
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

### Merge Triplets to Form Target Triplet

You're given a list of triplets `triplets`, where each triplet is `[x, y, z]`, and a `target` triplet `[a, b, c]`. Starting from a running result of `[0, 0, 0]`, you may repeatedly pick any triplet from the list and merge it in by taking the elementwise maximum (merging `[2, 5, 3]` into `[0, 0, 0]` gives `[2, 5, 3]`). Write a function `merge_triplets(triplets, target)` that returns `True` if some choice and order of merges can make the running result exactly equal `target`, and `False` otherwise.

For example, `triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]` and `target = [2, 7, 5]` can reach the target by merging only the first and last triplets, so the answer is `True`. But `triplets = [[3, 4, 5], [4, 5, 6]]` and `target = [3, 2, 5]` can never bring the middle value down to `2` once it's been merged up, so the answer is `False`.

---

### Tests

<ul>
<li id="test-1"><code>merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])</code> should return <code>True</code></li>
<li id="test-2"><code>merge_triplets([[5, 2, 3]], [5, 2, 3])</code> should return <code>True</code></li>
<li id="test-3"><code>merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])</code> should return <code>True</code></li>
<li id="test-4"><code>merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5])</code> should return <code>False</code></li>
<li id="test-5"><code>merge_triplets([[1, 1, 1]], [2, 2, 2])</code> should return <code>False</code></li>
<li id="test-6"><code>merge_triplets([[2, 2, 2], [1, 1, 1], [3, 3, 3]], [3, 3, 3])</code> should return <code>True</code></li>
<li id="test-7">Performance: 10,000 triplets, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def merge_triplets(triplets, target):
    best = [0, 0, 0]
    for t in triplets:
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            best = [max(best[i], t[i]) for i in range(3)]
    return best == target
```

**Brute force:** try every subset of triplets, merge it, and compare with `target`. That's `O(2^n)`, hopeless beyond about 20 triplets.

**Bottleneck:** most subsets are pointless. A triplet is either always safe to use or never usable, so there's nothing to search.

**Optimal idea:** skip every triplet that goes over the target in any position. Merge all the rest. The target is reachable exactly when that merge equals it.

**Why it's correct:** merging uses `max`, so a value can only go up. A triplet with any value above the target's would push that position past the target for good, so no valid choice uses it. Every other triplet is *safe*: merging it keeps each position at or below the target. Now take any choice of triplets that reaches the target. It uses only safe triplets. Adding the remaining safe ones can't push anything above the target, and can't lower anything either. So merging all safe triplets gives the target too. If merging all of them doesn't reach it, no subset can.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** merging a triplet because it matches the target in one position, without checking that the other two positions aren't over. Only checking that each target value shows up somewhere in the list: in `[[3, 4, 5], [4, 5, 6]]` with target `[3, 2, 5]`, the values `3` and `5` appear, but the triplet that has them also has a `4` in the middle.

</details>
