---
lesson_name: Koko Eating Bananas
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log m)
  space: O(1)
hints:
  - "Pattern: *Binary Search*."
  - "If Koko can finish at speed `k`, can she also finish at speed `k + 1`?"
  - "Yes, so \"can she finish at speed `k`?\" is false for small `k` and true from some point on. Binary search for the first `k` where it's true (template 2 in *Binary Search Basics*). The answer is between `1` and `max(piles)`."
  - "Template: hours at speed `k` is `sum(ceil(p / k) for p in piles)`. Search `lo = 1`, `hi = max(piles)`. If the hours fit in `h`, set `hi = mid`, otherwise `lo = mid + 1`."
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

### Koko Eating Bananas

A monkey named Koko faces `piles`, a list where `piles[i]` is the number of bananas in the `i`-th pile. She has `h` hours before the zookeeper returns, and picks one eating speed `k` (bananas per hour) that she keeps for every hour. Each hour she chooses a single pile and eats up to `k` bananas from it; if the pile has fewer than `k` bananas left, she finishes that pile for the hour and doesn't start another one until the next hour. Write a function that returns the smallest integer `k` that lets Koko finish every pile within `h` hours.

For example, with `piles = [3, 6, 7, 11]` and `h = 8`, the smallest working speed is `4`: at speed `4` she needs `1 + 2 + 2 + 3 = 8` hours, which just fits, while speed `3` would take `1 + 2 + 3 + 4 = 10` hours.

---

### Tests

<ul>
<li id="test-1"><code>min_eating_speed([3, 6, 7, 11], 8)</code> should return <code>4</code></li>
<li id="test-2"><code>min_eating_speed([30, 11, 23, 4, 20], 5)</code> should return <code>30</code></li>
<li id="test-3"><code>min_eating_speed([30, 11, 23, 4, 20], 6)</code> should return <code>23</code></li>
<li id="test-4"><code>min_eating_speed([1, 1, 1, 1], 4)</code> should return <code>1</code></li>
<li id="test-5"><code>min_eating_speed([1000000000], 2)</code> should return <code>500000000</code></li>
<li id="test-6"><code>min_eating_speed([5], 1)</code> should return <code>5</code></li>
<li id="test-7"><code>min_eating_speed([2, 4, 8], 6)</code> should return <code>3</code></li>
<li id="test-8">Performance: 1,000 piles of 1,000,000 bananas, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import math


def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

Here `n` is the number of piles and `m` the size of the largest pile.

**Brute force:** try `k = 1, 2, 3, ...` and return the first speed that fits. Each check is `O(n)`, and the answer can be as large as `m`, so this is `O(n·m)`. With a single pile of 1,000,000,000 bananas it never finishes.

**Bottleneck:** speeds are tried one at a time, although each check tells you which direction the answer is in.

**Optimal idea:** binary search over the speed. Eating faster never takes more hours, so the speeds that work are exactly `k >= answer`. Find that boundary by halving the range of speeds.

**Why it's correct:** the hours needed only go down (or stay the same) as `k` grows, so "fits in `h` hours" is false and then true. Speed `max(piles)` always works, because each pile takes one hour and there are at most `h` piles. Halving between `1` and `max(piles)` finds the first speed that works.

**Complexity:** `O(log m)` checks of `O(n)` each, so `O(n log m)` time. `O(1)` extra space.

**Common mistakes:** using `p // k` instead of rounding up, which undercounts hours for a partly eaten pile. `math.ceil(p / k)` and `(p + k - 1) // k` both round up. Starting `lo` at `0`, which divides by zero.

</details>
