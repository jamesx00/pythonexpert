---
lesson_name: Two Sum
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When you're looking at `nums[i]`, which single value would it need to pair with to reach `target`?"
  - "The partner of `n` is `target - n`. Store each value's index in a dictionary as you go, so you can check whether the partner has already appeared in `O(1)`. This is the *Complement lookup* block in *Arrays & Hashing Basics*."
  - "Template: for each `i, n`, if `target - n` is in `seen`, return `[seen[target - n], i]`. Otherwise store `seen[n] = i`."
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

### Two Sum

Write a function `two_sum(nums, target)` that takes a list of integers and a target integer, and returns the indices of the two elements that add up to `target`, as a list `[i, j]`. Assume every input has exactly one valid pair, and you cannot use the same element twice.

For example, given `nums = [3, 5, -4, 8]` and `target = 4`, the values `-4` and `8` add up to `4`, so `two_sum(nums, target)` should return `[2, 3]`. The order of the returned indices does not matter, and there is always exactly one pair of numbers that add up to the target.

---

### Tests

<ul>
<li id="test-1"><code>two_sum([3, 5, -4, 8], 4)</code> should return <code>[2, 3]</code></li>
<li id="test-2"><code>two_sum([2, 7, 11, 15], 9)</code> should return <code>[0, 1]</code></li>
<li id="test-3"><code>two_sum([3, 2, 4], 6)</code> should return <code>[1, 2]</code></li>
<li id="test-4"><code>two_sum([1, 5, 5, 2], 10)</code> should return <code>[1, 2]</code></li>
<li id="test-5"><code>two_sum([-3, 4, 3, 90], 0)</code> should return <code>[0, 2]</code></li>
<li id="test-6"><code>two_sum([0, 4, 3, 0], 0)</code> should return <code>[0, 3]</code></li>
<li id="test-7">Performance: 100,002 elements whose only valid pair is the last two, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

**Brute force:** try every pair `i < j` and return the first one that sums to `target`. That's `O(n²)` time.

**Bottleneck:** for each `nums[i]`, the inner loop searches the list for one specific value, `target - nums[i]`.

**Optimal idea:** remember every value you've passed in a dictionary from value to index. Then each "is my partner here?" question is one `O(1)` lookup.

**Why it's correct:** let the answer be `i < j`. When the loop reaches `j`, `nums[i]` is already in `seen`, so the pair is found. Checking `seen` *before* storing `n` stops an element from pairing with itself, as with `[3, 2, 4]` and target `6`.

**Complexity:** `O(n)` time for one pass with `O(1)` lookups. `O(n)` space for the dictionary.

**Common mistakes:** storing `n` before checking for its complement, which pairs an element with itself. Building the whole dictionary first and then searching, without checking `seen[complement] != i`, has the same problem.

</details>
