---
lesson_name: Find the Duplicate Number
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Read each value as a pointer to an index: index `i` points to index `nums[i]`. Starting at index `0` and following pointers, what shape do you get if two indices point to the same place?"
  - "The repeated value is where two pointers merge, which is the entrance of a cycle. Find the meeting point with *Fast & slow pointers* from *Linked List Basics*, then find the entrance."
  - "Template: `slow = fast = nums[0]`. Loop `slow = nums[slow]`, `fast = nums[nums[fast]]` until they're equal. Then start a new pointer at `nums[0]` and move it and `slow` one step at a time until they meet. That value is the duplicate."
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

### Find the Duplicate Number

Write a function `find_duplicate(nums)` that takes a list of `n + 1` integers where every value is between `1` and `n` inclusive, and exactly one value appears more than once (though it may appear more than twice). Return that repeated value. You may not modify the input list, and you should use only constant extra space - treat the list like a linked list where each index points to the index named by its value, and detect the cycle that forms.

For example, `find_duplicate([1, 3, 4, 2, 2])` should return `2`, since every other value from `1` to `4` appears exactly once.

---

### Tests

<ul>
<li id="test-1"><code>find_duplicate([1, 3, 4, 2, 2])</code> should return <code>2</code></li>
<li id="test-2"><code>find_duplicate([3, 1, 3, 4, 2])</code> should return <code>3</code></li>
<li id="test-3"><code>find_duplicate([1, 1])</code> should return <code>1</code></li>
<li id="test-4"><code>find_duplicate([2, 2, 2, 2, 2])</code> should return <code>2</code></li>
<li id="test-5"><code>find_duplicate([5, 4, 3, 2, 1, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>find_duplicate([1, 2, 3, 4, 5, 3])</code> should return <code>3</code></li>
<li id="test-7">Performance: 100,001 values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow
```

**Brute force:** compare every pair of values, which is `O(n²)` time. A set or a sorted copy brings it down to `O(n)` or `O(n log n)`, but uses `O(n)` extra space. Sorting `nums` in place breaks the rule against changing the input.

**Bottleneck:** without extra memory, there's no quick way to tell whether you've seen a value before.

**Optimal idea:** treat `nums` as a linked list where index `i` points to index `nums[i]`. Every value is between `1` and `n`, so no pointer leads back to index `0` and the walk from `0` never ends: it must enter a cycle. Two indices hold the duplicate value, so two pointers lead to the same index, and that index is the cycle's entrance. Floyd's algorithm finds the entrance in `O(1)` space.

**Why it's correct:** let the entrance be `a` steps from the start and the meeting point `b` steps into a cycle of length `c`. When the pointers meet, `slow` has taken `a + b` steps and `fast` twice that, and the difference `a + b` is a whole number of laps. So walking `a` more steps from the meeting point lands on the entrance, and a pointer starting at the beginning also reaches it after `a` steps. They meet there.

**Complexity:** `O(n)` time: both phases take at most a few laps of a list of `n + 1` nodes. `O(1)` extra space.

**Common mistakes:** returning the meeting point of the first phase, which is somewhere in the cycle but not necessarily its entrance. Starting the second-phase pointer at index `0` when the first phase started at `nums[0]`, which puts the two pointers one step out of line.

</details>
