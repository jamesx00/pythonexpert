---
lesson_name: Hand of Straights
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

</details>
