---
lesson_name: Detect Squares
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(1) add, O(n) count
  space: O(n)
hints:
  - "The query point is one corner. Once you pick the corner diagonally opposite it, are the other two corners already decided?"
  - "Count points in a dictionary keyed by `(x, y)`, so you can look up how many copies sit at any spot in `O(1)`. See *Geometry with points* in *Math & Geometry Basics*."
  - "Template: in `count`, loop over the other points `(x, y2)` in the query's column. With `d = y2 - y`, try `x2 = x + d` and `x2 = x - d`, and add `counts[(x, y2)] * counts[(x2, y)] * counts[(x2, y2)]`."
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

### Detect Squares

Design a class, `DetectSquares`, that tracks points added on a 2D plane and can report how many axis-aligned squares can be formed using a given point as one corner and three previously-added points as the other three corners.

The class needs two methods: `add(point)` records a new point (given as a two-element `[x, y]` list), and points may be added more than once at the same coordinates. `count(point)` takes a query point and returns the number of ways to pick three already-added points that, together with the query point, form a square whose sides are parallel to the x and y axes (i.e. each side is either purely horizontal or purely vertical). If the same three points could combine with the query point in more than one valid way (because of duplicates), each valid combination counts separately.

For example, after adding `[3, 10]`, `[11, 2]`, and `[3, 2]`, calling `count([11, 10])` returns `1`, because those three points plus `[11, 10]` form a square with side length `8`.

---

### Tests

<ul>
<li id="test-1">adding <code>[3, 10]</code>, <code>[11, 2]</code>, <code>[3, 2]</code> then calling <code>count([11, 10])</code> should return <code>1</code></li>
<li id="test-2">continuing from test 1, calling <code>count([14, 8])</code> should return <code>0</code></li>
<li id="test-3">continuing from test 1, adding <code>[11, 10]</code> then calling <code>count([13, 6])</code> should return <code>0</code></li>
<li id="test-4">a fresh instance: adding <code>[0, 0]</code>, <code>[0, 2]</code>, <code>[2, 0]</code>, <code>[2, 2]</code> then calling <code>count([0, 0])</code> should return <code>1</code></li>
<li id="test-5">continuing from test 4, adding <code>[0, 0]</code> again then calling <code>count([0, 0])</code> should return <code>1</code> (the query point itself is not one of the three), and <code>count([2, 2])</code> should return <code>2</code></li>
<li id="test-6">a fresh instance: calling <code>count([5, 5])</code> with no points added should return <code>0</code></li>
<li id="test-7">a fresh instance: adding <code>[0, 0]</code>, <code>[0, 2]</code>, <code>[2, 0]</code>, <code>[2, 2]</code>, <code>[2, 2]</code> then calling <code>count([0, 0])</code> should return <code>2</code> and <code>count([4, 4])</code> should return <code>0</code></li>
<li id="test-8">a fresh instance: adding <code>[1, 1]</code>, <code>[1, 3]</code>, <code>[3, 1]</code>, <code>[-1, 1]</code>, <code>[-1, 3]</code> then calling <code>count([3, 3])</code> should return <code>1</code> and <code>count([1, 1])</code> should return <code>1</code></li>
<li id="test-9">Performance: every point of a 2,000 x 10 grid added, then 5,000 <code>count</code> calls, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.counts = defaultdict(int)
        self.points = defaultdict(set)

    def add(self, point):
        x, y = point
        self.counts[(x, y)] += 1
        self.points[x].add(y)

    def count(self, point):
        x, y = point
        total = 0
        for y2 in list(self.points[x]):
            if y2 == y:
                continue
            d = y2 - y
            for x2 in (x + d, x - d):
                total += self.counts[(x, y2)] * self.counts[(x2, y)] * self.counts[(x2, y2)]
        return total
```

Here `n` is the number of points added.

**Brute force:** in `count`, scan every distinct point that has been added and treat it as the opposite corner, if it's on a diagonal from the query. Then look up the other two corners. That's `O(n)` per call. Test 9 adds 20,000 points and makes 5,000 calls, about 100 million checks.

**Bottleneck:** most of the scanned points aren't on a diagonal from the query, so they're looked at for nothing.

**Optimal idea:** a square with sides along the axes has a corner straight above or below the query point. So only scan the points in the query's column, `(x, y2)`. The side is `d = y2 - y`, and the square goes either right (`x + d`) or left (`x - d`). The other two corners are then fixed, so look them up in the count dictionary.

**Why it's correct:** each square with the query as a corner has exactly one other corner in the same column, and the square lies either to its right or to its left. So each square is found exactly once. Multiplying the three counts picks one copy of each corner in every possible way, which is how duplicates are counted. A zero count for any corner adds nothing.

**Complexity:** `add` is `O(1)`. `count` is `O(k)`, where `k` is the number of distinct points in the query's column: `O(n)` in the worst case, when every point is in one column, but usually far less (10 per call in test 9, against 20,000 for the brute force). `O(n)` space for the dictionary and the column sets.

**Common mistakes:** counting `y2 == y`, a square of side `0`. Forgetting one of the two directions, left or right. Multiplying by the count at the query point itself, which isn't one of the three chosen points (test 5).

</details>
