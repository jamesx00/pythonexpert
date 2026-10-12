---
lesson_name: Hand of Straights
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "Look at the smallest card in the hand. What can its group look like?"
  - "The smallest card has nothing below it, so it must *start* a group: it needs the next `group_size - 1` values. Sort the distinct values and take the groups from the smallest up (*Sort first* in *Greedy Basics*)."
  - "Template: return `False` if `len(hand) % group_size`. `count = Counter(hand)`. For each `k` in `sorted(count)`, let `needed = count[k]` and skip it if it's `0`. For each `j` in `range(k, k + group_size)`, return `False` if `count[j] < needed`, else subtract `needed`. Return `True`."
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

### Hand of Straights

You have a hand of cards `hand`, each showing an integer, and you'd like to rearrange them into groups of exactly `group_size` cards each, where every group's values form a run of consecutive integers (like `4, 5, 6`). Write a function `is_n_straight_hand(hand, group_size)` that returns `True` if such a grouping is possible, and `False` otherwise. Card values may repeat.

For example, `hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]` with `group_size = 3` splits neatly into `[1, 2, 3]`, `[2, 3, 4]`, and `[6, 7, 8]`, so the answer is `True`. But `hand = [1, 2, 3, 4, 5]` with `group_size = 4` can't be split evenly at all, since `5` cards isn't a multiple of `4`, so the answer is `False`.

---

### Tests

<ul>
<li id="test-1"><code>is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)</code> should return <code>True</code></li>
<li id="test-2"><code>is_n_straight_hand([1, 2, 3, 4, 5], 4)</code> should return <code>False</code></li>
<li id="test-3"><code>is_n_straight_hand([9, 13, 15, 23, 22, 25, 31, 20, 29, 14, 26, 12, 10, 27, 21, 11, 17, 30, 24, 28, 16, 18, 19, 32], 3)</code> should return <code>True</code></li>
<li id="test-4"><code>is_n_straight_hand([1, 1, 2, 2, 3, 3], 2)</code> should return <code>False</code></li>
<li id="test-5"><code>is_n_straight_hand([3, 4, 2, 1], 4)</code> should return <code>True</code></li>
<li id="test-6"><code>is_n_straight_hand([1, 2, 3], 1)</code> should return <code>True</code></li>
<li id="test-7">Performance: 150,000 cards, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter

def is_n_straight_hand(hand, group_size):
    if len(hand) % group_size != 0:
        return False
    count = Counter(hand)
    for k in sorted(count.keys()):
        needed = count[k]
        if needed == 0:
            continue
        for j in range(k, k + group_size):
            if count[j] < needed:
                return False
            count[j] -= needed
    return True
```

**Brute force:** sort the hand into a list. Repeatedly take the first card `k` and `list.remove` the values `k` to `k + group_size - 1`, failing if one is missing. Each `remove` shifts the list, so that's `O(n^2)` time. Finding the smallest card with `min(count)` each time is `O(n^2)` too.

**Bottleneck:** removing one card at a time from a list, and finding the smallest card again after every group.

**Optimal idea:** count the cards and visit each distinct value once, from smallest to largest. If `count[k]` copies of `k` are left, they must all start groups, so take `count[k]` copies of each of the next `group_size - 1` values in one go.

**Why it's correct:** the smallest card left has no smaller card to sit behind, so it must be the lowest card of its group. The group is then forced: `k, k + 1, ..., k + group_size - 1`. There's no choice, so making it can't hurt. The same is true for every copy of `k`. After those groups are taken out, the next smallest value with copies left is in the same position, and so on. If a needed value runs short, no arrangement works, because the forced groups already need more of it than there are.

**Complexity:** `O(n log n)` time to sort the distinct values. Each group start does `group_size` steps, and there are at most `n / group_size` starts, so the inner loops are `O(n)` in total. `O(n)` space for the counter.

**Common mistakes:** building groups from an arbitrary card instead of the smallest one, which can take a card that another group needed. Subtracting one copy at a time while re-scanning from the start each time, which is quadratic. The `len(hand) % group_size` check is a quick exit; the loop would also fail without it.

</details>
