---
lesson_name: Sorting Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Sorting
---

## Why This Matters &#x1F4A1;

You'll call `sorted()` in many problems, and it's almost always the right choice in real code. But knowing how sorting works teaches you two ideas you'll reuse everywhere: **divide and conquer** (merge sort) and **partitioning** (quicksort). Partitioning is exactly what *Quickselect* and the *Kth Largest* problems use later on.

## Why `O(n log n)`? &#x1F9EE;

Merge sort splits the list in half, sorts each half recursively, and merges the two sorted halves. The list can only be halved about `log n` times before the pieces have one element, and each level of halving does `O(n)` total merging work. `log n` levels × `O(n)` per level = `O(n log n)`.

## Merge Sort &#x1F9F1;

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= keeps equal items in their original order (stable)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

- **Time:** `O(n log n)` in every case.
- **Space:** `O(n)` for the merged lists.
- **Stable:** equal items keep their relative order.

## Quicksort and Partitioning &#x2702;&#xFE0F;

Quicksort picks a **pivot**, rearranges the list so smaller items come before the pivot and larger items after it (the **partition** step), then sorts each side recursively. After partitioning, the pivot is already in its final sorted position.

```python
def partition(nums, lo, hi):
    """Lomuto partition: uses nums[hi] as the pivot. Returns the pivot's final index."""
    pivot = nums[hi]
    store = lo
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[i], nums[store] = nums[store], nums[i]
            store += 1
    nums[store], nums[hi] = nums[hi], nums[store]
    return store


def quicksort(nums, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1
    if lo < hi:
        p = partition(nums, lo, hi)
        quicksort(nums, lo, p - 1)
        quicksort(nums, p + 1, hi)
```

- **Time:** `O(n log n)` on average, `O(n²)` in the worst case (an already sorted list with the last element as pivot). Picking a random pivot makes the worst case very unlikely.
- **Space:** `O(log n)` on average for the call stack. It sorts in place.
- **Not stable.**

### From quicksort to Quickselect

To find the `k`-th smallest item, you don't need to sort both sides. Partition once, then recurse only into the side that contains index `k`. That cuts the average time to `O(n)`.

## Python's Built-in Sort &#x1F40D;

`sorted()` and `list.sort()` use **Timsort**, a merge sort hybrid that's `O(n log n)` in the worst case, stable, and very fast on partly sorted data. Use `key=` to sort by a derived value:

```python
words.sort(key=len)                              # by length
points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)  # by distance from the origin
intervals.sort(key=lambda iv: iv[0])             # by start time
```

## Tips & Gotchas &#x1F4CC;

- **Sorting first is a common trick.** It makes duplicates adjacent, enables two pointers and binary search, and puts intervals in order. Just remember it adds `O(n log n)`.
- **`sorted()` returns a new list, `.sort()` sorts in place** and returns `None`.
- **Counting sort / bucket sort** beat `O(n log n)` when values are small bounded integers, because they don't compare items at all.
