---
lesson_name: Heap / Priority Queue Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Heap / Priority Queue
---

## Why This Pattern Matters &#x1F4A1;

A heap gives you the smallest item in `O(1)` and lets you add or remove items in `O(log n)`. Use it when you repeatedly need "the current best" from a collection that keeps changing. Sorting once can't do that, and re-sorting every time is too slow.

Python's `heapq` works on a plain list and is a **min-heap**:

```python
import heapq

heap = []
heapq.heappush(heap, 5)      # O(log n)
smallest = heap[0]           # peek, O(1)
heapq.heappop(heap)          # remove smallest, O(log n)
heapq.heapify(nums)          # turn a list into a heap in place, O(n)
```

## Spotting It &#x1F50D;

- "**K-th** largest / smallest", "**top k**", "**k closest**".
- Repeatedly take the biggest/smallest, process it, maybe put something back (*Last Stone Weight*, *Task Scheduler*).
- **Merge k sorted** lists/streams.
- A running **median** over a stream.
- Shortest paths with weights (Dijkstra, in Advanced Graphs).

## Core Building Blocks &#x1F9F1;

### Max-heap by negating

```python
heap = [-x for x in nums]
heapq.heapify(heap)
largest = -heapq.heappop(heap)
```

### Top-k with a size-k heap

To find the k **largest**, keep a **min**-heap of size k. Its root is the smallest of the top k, which is exactly the k-th largest.

```python
def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)   # drop the smallest
    return heap[0]
```

That's `O(n log k)` time and `O(k)` space, better than sorting when `k` is small.

### Tuples for priorities

Heaps compare tuples element by element, so put the priority first:

```python
heapq.heappush(heap, (distance, x, y))
```

### Two heaps for a median

Keep a max-heap for the lower half and a min-heap for the upper half. Their sizes differ by at most 1, and the median is at the top(s).

## Tips & Gotchas &#x1F4CC;

- **No max-heap built in.** Negate numbers (or the priority in a tuple).
- **Tie-breaking crashes:** if two tuples tie on priority, Python compares the next element. Objects like `ListNode` can't be compared, so add a unique counter: `(val, i, node)`.
- **`heap[0]` is the min, but `heap[1]` is not necessarily the second smallest.** A heap is only partially ordered.
- **Opposite heap for top-k:** k largest → min-heap; k smallest → max-heap.
- **`heapq.nlargest(k, nums)` / `nsmallest`** are handy one-liners when you don't need to stream.
- **Dijkstra / lazy deletion:** instead of removing stale entries, skip them when popped (`if d > dist[node]: continue`).
