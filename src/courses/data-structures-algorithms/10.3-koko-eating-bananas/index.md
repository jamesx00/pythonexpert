---
lesson_name: Koko Eating Bananas
code_editor: True
code_execution: True
adding_file_allowed: False
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

</details>
