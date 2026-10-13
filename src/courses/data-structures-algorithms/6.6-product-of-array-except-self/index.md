---
lesson_name: Product of Array Except Self
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1) extra
hints:
  - "The product of everything except `nums[i]` splits into two parts. What are they?"
  - "`output[i]` is (product of everything to the left of `i`) × (product of everything to the right of `i`). Both can be built in one pass each, like the *Prefix sums* block in *Arrays & Hashing Basics* but with multiplication."
  - "Template: one left-to-right pass writes the running left product into `output[i]` *before* multiplying in `nums[i]`. A right-to-left pass multiplies in a running right product the same way."
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

### Product of Array Except Self

Write a function `product_except_self(nums)` that takes a list of integers and returns a new list `output` where `output[i]` is the product of every value in `nums` except `nums[i]`. You must not use division anywhere in your solution.

For example, given `nums = [2, 3, 4, 5]`, the value at index `0` should be `3 * 4 * 5 = 60`, the value at index `1` should be `2 * 4 * 5 = 40`, and so on, so `product_except_self(nums)` should return `[60, 40, 30, 24]`.

---

### Tests

<ul>
<li id="test-1"><code>product_except_self([2, 3, 4, 5])</code> should return <code>[60, 40, 30, 24]</code></li>
<li id="test-2"><code>product_except_self([1, 1, 1, 1])</code> should return <code>[1, 1, 1, 1]</code></li>
<li id="test-3"><code>product_except_self([1, 2])</code> should return <code>[2, 1]</code></li>
<li id="test-4"><code>product_except_self([-1, 2, -3])</code> should return <code>[-6, 3, -2]</code></li>
<li id="test-5"><code>product_except_self([0, 4, 5])</code> should return <code>[20, 0, 0]</code></li>
<li id="test-6"><code>product_except_self([3, 0, 0, 6])</code> should return <code>[0, 0, 0, 0]</code></li>
<li id="test-7">Performance: 100,000 elements, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output
```

**Brute force:** for each index, multiply every other element with an inner loop. That's `O(n²)` time.

**Bottleneck:** neighbouring indices share almost all of their factors, but each one recomputes its product from scratch.

**Optimal idea:** `output[i] = prefix(i) × suffix(i)`, where `prefix(i)` is the product of `nums[0..i-1]` and `suffix(i)` is the product of `nums[i+1..]`. One forward pass stores each prefix in `output`. One backward pass multiplies each suffix in, using a single running variable.

**Why it's correct:** in the forward pass, `output[i]` is set *before* `nums[i]` joins `prefix`, so it holds exactly the product to the left of `i`. The backward pass does the same for the right side. Their product is every element except `nums[i]`. No division is used, so zeros need no special case.

**Complexity:** `O(n)` time for two passes. `O(1)` extra space, because the output list doesn't count as extra.

**Common mistakes:** multiplying `nums[i]` into the running product *before* writing `output[i]`, which includes `nums[i]` in its own answer. Dividing the total product by `nums[i]` is not allowed and fails when the list contains a zero.

</details>
