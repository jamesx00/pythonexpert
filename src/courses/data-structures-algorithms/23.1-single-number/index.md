---
lesson_name: Single Number
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Is there an operation that makes two equal values cancel out, whatever order they come in?"
  - "Use *XOR cancels pairs* from *Bit Manipulation Basics*: `a ^ a == 0` and `a ^ 0 == a`, in any order. XOR all the numbers together and every pair disappears."
  - "Template: `result = 0`. For each `n` in `nums`: `result ^= n`. Return `result`."
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

### Single Number

Write a function `single_number(nums)` that takes a list of integers where every value appears exactly twice except for one value that appears only once, and returns that lone value. Your solution should run in linear time while using only constant extra space, so sorting or building a frequency map with an extra structure defeats the point of the exercise.

For example, given `nums = [4, 1, 2, 1, 2]`, the values `1` and `2` each appear twice, leaving `4` as the single number, so the function should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>single_number([4, 1, 2, 1, 2])</code> should return <code>4</code></li>
<li id="test-2"><code>single_number([1])</code> should return <code>1</code></li>
<li id="test-3"><code>single_number([2, 2, 1])</code> should return <code>1</code></li>
<li id="test-4"><code>single_number([7, 3, 5, 4, 5, 3, 4])</code> should return <code>7</code></li>
<li id="test-5"><code>single_number([-1, -1, -2])</code> should return <code>-2</code></li>
<li id="test-6"><code>single_number([0, 1, 0])</code> should return <code>1</code></li>
<li id="test-7"><code>single_number([9, 5, 9])</code> should return <code>5</code></li>
<li id="test-8"><code>single_number([3, -3, 3])</code> should return <code>-3</code></li>
<li id="test-9">Performance: 50,001 numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
```

**Brute force:** for each number, count how often it appears with `nums.count(n)` and return the one that appears once. Each count scans the whole list, so this is `O(n^2)` time. Too slow for 50,001 numbers. A `Counter` or a set makes it `O(n)` time, but `O(n)` extra space, which the problem rules out.

**Bottleneck:** the counting only exists to match each value with its twin.

**Optimal idea:** XOR every number into one running value. Equal values cancel, so only the single number is left.

**Why it's correct:** XOR is commutative and associative, so you can regroup the XOR of the whole list into pairs of equal values plus the single one. Each pair gives `a ^ a == 0`, and `0 ^ x == x`, so the result is the single number. Negative numbers work too, since XOR works on their bits the same way.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** starting `result` at `nums[0]` and then looping over all of `nums`, which XORs the first value twice and cancels it. Sorting and comparing neighbours, which is `O(n log n)` and easy to get wrong at the end of the list.

</details>
