---
lesson_name: "Warm-up: Merge Sort"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "If someone handed you the two halves of the list already sorted, how would you combine them into one sorted list without sorting again? Which element must come first?"
  - "Follow *Merge Sort* in *Sorting Basics*. `merge` walks two indexes `i` and `j`, appending the smaller of `left[i]` and `right[j]` each step, then appends whatever is left over. `merge_sort` returns lists of length `0` or `1` as they are, otherwise splits at `mid = len(nums) // 2`, sorts each half recursively and merges them."
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

### Warm-up: Merge Sort

Implement merge sort in two parts:

1. `merge(left, right)` takes two lists that are **already sorted** and returns one sorted list containing all of their items.
2. `merge_sort(nums)` returns a **new** sorted list with the items of `nums` in ascending order, and leaves `nums` unchanged. Split the list in half, sort each half with `merge_sort`, and combine the results with `merge`.

Don't use `sorted()` or `.sort()`. The performance test sorts 20,011 numbers, which a simple `O(n²)` sort (such as insertion sort) can't finish in time.

---

### Tests

<ul>
<li id="test-1"><code>merge([1, 4, 9], [2, 3, 10])</code> should return <code>[1, 2, 3, 4, 9, 10]</code></li>
<li id="test-2"><code>merge([], [1, 2])</code> should return <code>[1, 2]</code></li>
<li id="test-3"><code>merge([5], [])</code> should return <code>[5]</code></li>
<li id="test-4"><code>merge([1, 1, 3], [1, 2])</code> should return <code>[1, 1, 1, 2, 3]</code></li>
<li id="test-5"><code>merge([6, 7, 8], [1, 2, 3])</code> should return <code>[1, 2, 3, 6, 7, 8]</code></li>
<li id="test-6"><code>merge_sort([])</code> should return <code>[]</code></li>
<li id="test-7"><code>merge_sort([1])</code> should return <code>[1]</code></li>
<li id="test-8"><code>merge_sort([3, 1, 2])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-9"><code>merge_sort([5, -2, 9, 0, -2, 7])</code> should return <code>[-2, -2, 0, 5, 7, 9]</code></li>
<li id="test-10"><code>merge_sort([1, 2, 3, 4, 5])</code> should return <code>[1, 2, 3, 4, 5]</code></li>
<li id="test-11"><code>merge_sort([5, 4, 3, 2, 1])</code> should return <code>[1, 2, 3, 4, 5]</code></li>
<li id="test-12"><code>merge_sort([4, 4, 4, 1])</code> should return <code>[1, 4, 4, 4]</code></li>
<li id="test-13"><code>merge_sort(nums)</code> doesn't change <code>nums</code></li>
<li id="test-14"><code>main.py</code> doesn't call <code>sorted()</code> or <code>.sort()</code></li>
<li id="test-15">Performance: sorting 20,011 shuffled numbers within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return list(nums)
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))
```

**Brute force:** insertion sort. Take each item and shift it left past every bigger item already placed. Each item can move past all the items before it, so it's `O(n²)`: about 100 million shifts on average for 20,011 numbers.

**Bottleneck:** insertion sort fixes the order one item at a time and compares the same pairs of items over and over.

**Optimal idea:** divide and conquer. Sorting two halves and merging them is cheap, because merging two sorted lists only ever needs to compare their two front items. Apply that idea recursively until the pieces have one item, which is already sorted.

**Why it's correct:** `merge` keeps an index into each list. The smallest item not yet used is always `left[i]` or `right[j]`, because each list is sorted, so appending the smaller of the two keeps `result` sorted. When one list runs out, the rest of the other is already sorted and all bigger than what's in `result`. `merge_sort` trusts the recursion: if both halves come back sorted, merging them sorts the whole list. A list of length `0` or `1` is already sorted, and every split makes the pieces shorter, so the recursion always ends.

**Complexity:** the list is halved about `log n` times, and at each level of the recursion the merges handle `n` items in total. That's `O(n log n)` time. The merged lists and slices take `O(n)` extra space, and the call stack is `O(log n)` deep.

**Common mistakes:** forgetting to append the leftovers after the `while` loop, which drops items. Using `<` instead of `<=` in `merge`, which still sorts correctly but makes the sort unstable (equal items can swap order). Popping from the front of the lists with `pop(0)`, which is `O(n)` per pop. Returning `nums` itself for short lists instead of a copy, so changing the result would change the input.

</details>
