---
lesson_name: Last Stone Weight
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "Each smash needs the two heaviest stones, and a smash can put a new stone back. What structure gives you the largest item quickly, again and again?"
  - "`heapq` is a min-heap, so store negated weights to get a max-heap (*Max-heap by negating* in *Heap / Priority Queue Basics*). Pop twice to get the two heaviest."
  - "Template: `heap = [-s for s in stones]`, `heapify(heap)`. While `len(heap) > 1`: pop `a` and `b` (negate them back), and if `a != b`, push `-(a - b)`. Return `-heap[0]` if the heap isn't empty, else `0`."
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

### Last Stone Weight

You are given a list of integers `stones`, where each value is the weight of one stone. Repeatedly take the two heaviest stones and smash them together: if their weights are equal, both stones are destroyed; otherwise the lighter stone is destroyed and the heavier one's weight is reduced by the lighter one's weight, then goes back into the pile. Keep smashing until at most one stone remains, and write a function `last_stone_weight(stones)` that returns the weight of the final remaining stone, or `0` if none remain.

For example, given `stones = [8, 4, 3, 2]`, smashing `8` and `4` leaves a `4`, so the pile becomes `[4, 3, 2]`. Smashing `4` and `3` leaves a `1`, giving `[2, 1]`. Smashing those leaves a single stone of weight `1`, so `last_stone_weight(stones)` returns `1`.

---

### Tests

<ul>
<li id="test-1"><code>last_stone_weight([8, 4, 3, 2])</code> should return <code>1</code></li>
<li id="test-2"><code>last_stone_weight([2, 7, 4, 1, 8, 1])</code> should return <code>1</code></li>
<li id="test-3"><code>last_stone_weight([1])</code> should return <code>1</code></li>
<li id="test-4"><code>last_stone_weight([])</code> should return <code>0</code></li>
<li id="test-5"><code>last_stone_weight([5, 5])</code> should return <code>0</code></li>
<li id="test-6"><code>last_stone_weight([10, 4, 2, 10])</code> should return <code>2</code></li>
<li id="test-7"><code>last_stone_weight([3, 3, 3, 3])</code> should return <code>0</code></li>
<li id="test-8">Performance: 50,000 stones, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import heapq


def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
```

**Brute force:** sort the pile before every smash, or find the heaviest with `max()` and `remove()` it twice. Each smash then costs `O(n)` or more, and there can be up to `n - 1` smashes, so it's `O(n²)`.

**Bottleneck:** after each smash only one stone changes, but the whole pile is searched or sorted again.

**Optimal idea:** keep the pile in a max-heap. The two heaviest stones are two pops away, and the leftover stone is one push.

**Why it's correct:** the heap always holds exactly the stones still in the pile, so its top two are the two heaviest, as the rules require. Equal stones are both destroyed, and otherwise the difference goes back in. The loop stops at one stone or none.

**Complexity:** `O(n log n)` time: `heapify` is `O(n)`, and each of at most `n - 1` smashes does a few `O(log n)` heap operations. `O(n)` space for the heap.

**Common mistakes:** forgetting that `heapq` is a min-heap, which smashes the two *lightest* stones. Negating on the way in but not on the way out. Reading `heap[0]` when the heap is empty instead of returning `0`.

</details>
