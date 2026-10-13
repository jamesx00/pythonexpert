---
lesson_name: "Warm-up: Quicksort Partition"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Walk through the range once from left to right. Each time you find an item smaller than the pivot, where should it go so that all the small items end up together at the front?"
  - "Use the Lomuto scheme in *Sorting Basics*: keep a `store` index starting at `lo`. For each `i` from `lo` to `hi - 1`, if `nums[i] < pivot`, swap `nums[i]` with `nums[store]` and move `store` forward. Finally swap the pivot (`nums[hi]`) into `nums[store]` and return `store`."
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

### Warm-up: Quicksort Partition

Write `partition(nums, lo, hi)`, the step at the heart of quicksort and Quickselect. It works **in place** on the part of `nums` from index `lo` to index `hi` (both included):

- The **pivot** is the last item in the range, `nums[hi]`.
- Rearrange the range so that every item **smaller than** the pivot comes before it, and every item **greater than or equal to** the pivot comes after it.
- Return the pivot's final index `p`. After the call, `nums[p]` is the pivot, which is now in the position it would have in the sorted list.
- Don't touch anything outside `lo..hi`, and don't create a new list: rearrange `nums` by swapping items.

For example, with `nums = [3, 8, 2, 5, 1, 4, 7, 6]`, `partition(nums, 0, 7)` uses the pivot `6`. Five items are smaller, so it returns `5`, and `nums` could become `[3, 2, 5, 1, 4, 6, 7, 8]`. The order of items within each side doesn't matter.

`main.py` also contains a finished `quicksort` that uses your `partition`. The last tests check that it sorts correctly. Don't use `sorted()` or `.sort()`.

---

### Tests

<ul>
<li id="test-1"><code>partition([3, 8, 2, 5, 1, 4, 7, 6], 0, 7)</code> should return <code>5</code> and leave indexes 0 to 7 partitioned around the pivot <code>6</code></li>
<li id="test-2"><code>partition([9, 7, 5, 3, 1], 0, 4)</code> should return <code>0</code> and leave indexes 0 to 4 partitioned around the pivot <code>1</code></li>
<li id="test-3"><code>partition([1, 2, 3, 4, 5], 0, 4)</code> should return <code>4</code> and leave indexes 0 to 4 partitioned around the pivot <code>5</code></li>
<li id="test-4"><code>partition([4, 4, 4, 4], 0, 3)</code> should return <code>0</code> and leave indexes 0 to 3 partitioned around the pivot <code>4</code></li>
<li id="test-5"><code>partition([7], 0, 0)</code> should return <code>0</code> and leave indexes 0 to 0 partitioned around the pivot <code>7</code></li>
<li id="test-6"><code>partition([10, 3, 9, 1, 8, 2, 0], 1, 5)</code> should return <code>2</code> and leave indexes 1 to 5 partitioned around the pivot <code>2</code></li>
<li id="test-7"><code>partition([5, -1, 3, -1, 0, 3], 0, 5)</code> should return <code>3</code> and leave indexes 0 to 5 partitioned around the pivot <code>3</code></li>
<li id="test-8"><code>quicksort(nums)</code> with <code>nums = [3, 6, 1, 8, 2, 9, 2]</code> should sort it to <code>[1, 2, 2, 3, 6, 8, 9]</code></li>
<li id="test-9"><code>quicksort(nums)</code> with <code>nums = [5, 4, 3, 2, 1]</code> should sort it to <code>[1, 2, 3, 4, 5]</code></li>
<li id="test-10"><code>main.py</code> doesn't call <code>sorted()</code> or <code>.sort()</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def partition(nums, lo, hi):
    pivot = nums[hi]
    store = lo
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[i], nums[store] = nums[store], nums[i]
            store += 1
    nums[store], nums[hi] = nums[hi], nums[store]
    return store
```

**Brute force:** copy the items smaller than the pivot into one new list and the rest into another, then write `smaller + [pivot] + rest` back into `nums[lo:hi + 1]`. It's `O(n)` time, but it uses `O(n)` extra memory every time quicksort partitions.

**Bottleneck:** the two temporary lists. Quicksort's advantage over merge sort is that it sorts in place, and copying throws that away.

**Optimal idea:** grow the "smaller than pivot" region at the front of the range by swapping. `store` marks where the next small item should go. One left-to-right pass is enough.

**Why it's correct:** before each step of the loop, `nums[lo:store]` holds only items smaller than the pivot, and `nums[store:i]` holds only items `>=` the pivot. If `nums[i]` is smaller, swapping it into `nums[store]` and moving `store` forward keeps both statements true; if not, it's already in the right region. After the loop, every item before `store` is smaller and every item from `store` to `hi - 1` is `>=`, so swapping the pivot into `store` puts it between the two groups. That's exactly where it belongs in sorted order, because exactly `store - lo` items in the range are smaller.

**Complexity:** one pass over `hi - lo` items with `O(1)` work each: `O(n)` time. Only a few variables: `O(1)` extra space. Quicksort then calls `partition` on smaller and smaller ranges: `O(n log n)` on average, but `O(n²)` when the pivot is always the largest or smallest item (such as an already sorted list), because each partition then only removes one item.

**Common mistakes:** looping `i` up to `hi` (inclusive), which compares the pivot with itself. Forgetting the final swap, so the pivot stays at the end and the returned index points at something else. Starting `store` at `0` instead of `lo`, which breaks partitions of a sub-range. Using `<=`, which is still a valid partition but puts items equal to the pivot on the left, so the returned index differs from the one these tests expect.

</details>
