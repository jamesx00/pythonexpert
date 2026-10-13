---
lesson_name: Three Sum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n²)
  space: O(1) extra
hints:
  - "Pattern: *Two Pointers*."
  - "If you fix the first number of a trio, what problem do you have left to solve for the other two?"
  - "Sort the list. For each `nums[i]`, find pairs in the rest of the list that sum to `-nums[i]` with the sorted two-pointer technique from *Two Sum on a Sorted Array*. This is shape 3 in *Two Pointers Basics*."
  - "Template: sort, then for each `i` (skipping `nums[i] == nums[i - 1]`), run `left = i + 1`, `right = n - 1` inward. After recording a trio, move `left` past every copy of the value it just used."
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

### Three Sum

Given a list of integers, write a function that finds every distinct trio of numbers in the list that adds up to zero. Return the trios as a list of 3-item lists, where each trio is sorted in ascending order, and no trio (as a set of values) appears more than once — even if the same values appear multiple times in the input at different positions. The order of the trios in your result doesn't matter.

For example, given `[-2, 0, 1, 1, -1, -4]`, the valid zero-sum trios are `(-2, 1, 1)` and `(-1, 0, 1)`, so the function should return `[[-2, 1, 1], [-1, 0, 1]]` (in any order).

---

### Tests

<ul>
<li id="test-1"><code>three_sum([-2, 0, 1, 1, -1, -4])</code> should return <code>[[-2, 1, 1], [-1, 0, 1]]</code> (any order)</li>
<li id="test-2"><code>three_sum([0, 0, 0])</code> should return <code>[[0, 0, 0]]</code></li>
<li id="test-3"><code>three_sum([0, 0, 0, 0])</code> should return <code>[[0, 0, 0]]</code></li>
<li id="test-4"><code>three_sum([1, 2, -3])</code> should return <code>[[-3, 1, 2]]</code></li>
<li id="test-5"><code>three_sum([1, 2, 3])</code> should return <code>[]</code></li>
<li id="test-6"><code>three_sum([-1, 0, 1, 2, -1, -4])</code> should return <code>[[-1, -1, 2], [-1, 0, 1]]</code> (any order)</li>
<li id="test-7">Performance: 1,000 values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def three_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    triplets = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return triplets
```

**Brute force:** try every trio with three nested loops and collect the sorted zero-sum trios in a set to remove duplicates. That's `O(n³)` time.

**Bottleneck:** once the first number is fixed, the inner two loops are a plain Two Sum, solved the slow way.

**Optimal idea:** sort the list, fix each `nums[i]`, and find the pairs that sum to `-nums[i]` with two pointers over the rest of the sorted list. Duplicates are skipped instead of collected in a set.

**Why it's correct:** for a fixed `i`, the two-pointer scan finds every pair that sums to `-nums[i]`, for the same reason as in *Two Sum on a Sorted Array*. Skipping a value of `nums[i]` equal to the previous one, and moving `left` past copies of the value just used, means each distinct trio is recorded once. Because the list is sorted, each trio comes out in ascending order.

**Complexity:** `O(n log n)` to sort, plus `O(n)` for each of the `n` scans, so `O(n²)` time. `O(1)` extra space apart from the sorted copy and the output.

**Common mistakes:** forgetting one of the two duplicate skips, which returns `[0, 0, 0]` twice for `[0, 0, 0, 0]`. Stopping the scan after the first trio for an `i`, which misses other pairs such as both `[-1, -1, 2]` and `[-1, 0, 1]`.

</details>
