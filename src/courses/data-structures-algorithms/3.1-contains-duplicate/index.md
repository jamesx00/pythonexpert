---
lesson_name: Contains Duplicate
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "As you walk through `nums`, what would you need to remember to notice that the current value has appeared before?"
  - "Keep a `set` of the values you've already seen. Checking `x in seen` is `O(1)` on average. This is the *Seen-set* block in *Arrays & Hashing Basics*."
  - "Template: for each `x`, return `True` if `x` is already in `seen`, otherwise add it. Return `False` after the loop."
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

### Contains Duplicate

Write a function `has_duplicate(nums)` that takes a list of integers and returns `True` if any value appears more than once, or `False` if every value is unique.

For example, `has_duplicate([4, 2, 7, 2, 9])` should return `True` because `2` shows up twice, while `has_duplicate([4, 2, 7, 9])` should return `False` since all four values are distinct.

---

### Tests

<ul>
<li id="test-1"><code>has_duplicate([4, 2, 7, 2, 9])</code> should return <code>True</code></li>
<li id="test-2"><code>has_duplicate([4, 2, 7, 9])</code> should return <code>False</code></li>
<li id="test-3"><code>has_duplicate([1, 1, 1, 1])</code> should return <code>True</code></li>
<li id="test-4"><code>has_duplicate([])</code> should return <code>False</code></li>
<li id="test-5"><code>has_duplicate([5])</code> should return <code>False</code></li>
<li id="test-6"><code>has_duplicate([10, 20, 30, 40, 10])</code> should return <code>True</code></li>
<li id="test-7">Performance: 100,000 distinct values, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def has_duplicate(nums):
    return len(set(nums)) != len(nums)
```

**Brute force:** compare every pair with two nested loops. That's `O(n²)` time.

**Bottleneck:** for each value, the inner loop searches the rest of the list for a copy. Searching a list is `O(n)`.

**Optimal idea:** a `set` stores each distinct value once, and finds a value in `O(1)` on average. Building `set(nums)` drops the duplicates, so the set is shorter than the list exactly when a duplicate exists. The loop version (add values to a `seen` set, return `True` on the first repeat) works the same way and can stop early.

**Why it's correct:** `len(set(nums))` counts distinct values. It equals `len(nums)` only if no value was dropped, i.e. every value is unique.

**Complexity:** `O(n)` time to build the set, `O(n)` space to store it.

**Common mistakes:** sorting and comparing neighbours works but is `O(n log n)`. Using a list as the `seen` collection makes each `in` check `O(n)`, which brings back the `O(n²)` brute force.

</details>
