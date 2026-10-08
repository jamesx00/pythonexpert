---
lesson_name: Two Sum on a Sorted Array
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Take the smallest and the largest value. If their sum is too big, can the largest value be part of *any* valid pair?"
  - "Start `left` at the smallest value and `right` at the largest (shape 1 in *Two Pointers Basics*). A sum that's too small means `left` must move right, and a sum that's too big means `right` must move left."
  - "Template: `while left < right`, compare `nums[left] + nums[right]` with `target`. Return `[left, right]` if equal, otherwise move `left` forward when the sum is too small or `right` back when it's too big."
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

### Two Sum on a Sorted Array

You're given a list of integers that is already sorted from smallest to largest, along with a `target` value. Write a function that finds two different elements in the list that add up exactly to `target`, and returns their positions as a two-item list `[i, j]` with `i < j`. You may assume exactly one valid pair exists, and each element can only be used once.

For example, given `[1, 3, 4, 7, 11]` and a target of `10`, the values at positions `1` and `3` are `3` and `7`, which sum to `10`, so the function should return `[1, 3]`.

---

### Tests

<ul>
<li id="test-1"><code>two_sum_sorted([1, 3, 4, 7, 11], 10)</code> should return <code>[1, 3]</code></li>
<li id="test-2"><code>two_sum_sorted([-4, -1, 0, 3, 8], 4)</code> should return <code>[0, 4]</code></li>
<li id="test-3"><code>two_sum_sorted([2, 5], 7)</code> should return <code>[0, 1]</code></li>
<li id="test-4"><code>two_sum_sorted([1, 2, 3, 4, 6], 10)</code> should return <code>[3, 4]</code></li>
<li id="test-5"><code>two_sum_sorted([-6, -3, -1, 2, 9], -9)</code> should return <code>[0, 1]</code></li>
<li id="test-6"><code>two_sum_sorted([0, 0, 3, 5], 0)</code> should return <code>[0, 1]</code></li>
<li id="test-7">Performance: 100,002 sorted values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None
```

**Brute force:** try every pair `i < j`. That's `O(n²)` time and ignores the fact that the list is sorted. The hash-map solution from *Two Sum* is `O(n)` time but uses `O(n)` space.

**Bottleneck:** the brute force checks pairs that the ordering already rules out.

**Optimal idea:** put `left` at the start and `right` at the end. If the sum is too small, increase it by moving `left` right. If it's too big, decrease it by moving `right` left.

**Why it's correct:** when the sum is too big, `nums[right]` plus the *smallest* remaining value is already too big, so `nums[right]` can't be in any pair with the values still in range, and it's safe to drop it. The same argument with "too small" drops `nums[left]`. Each step only drops values that can't be in the answer, so the answer is never skipped.

**Complexity:** `O(n)` time, because each step moves one pointer and they meet after at most `n` steps. `O(1)` extra space.

**Common mistakes:** using `left <= right`, which can pair an element with itself. Moving both pointers after a miss, which can skip the answer.

</details>
