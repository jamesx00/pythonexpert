---
lesson_name: Plus One
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "When you add one by hand, which digit do you start with, and when do you get to stop?"
  - "Work from the rightmost digit. A `9` becomes `0` and the carry moves left. Any other digit just goes up by one, and you're done. See *Grade-school arithmetic on strings* in *Math & Geometry Basics*."
  - "Template: copy `digits`. For `i` from the last index down to `0`: if `digits[i] < 9`, add one and return. Otherwise set it to `0`. If the loop ends, every digit was `9`, so return `[1] + digits`."
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

### Plus One

A large non-negative integer is given to you as a list of its digits, `digits`, most significant digit first, with no leading zeros (other than the number `0` itself). Write a function that adds one to the number and returns the result in the same list-of-digits format, carrying as needed.

For example, `[1, 2, 9]` represents the number `129`, so adding one gives `130`, returned as `[1, 3, 0]`. If every digit is a `9`, such as `[9, 9]`, the carry pushes a new leading digit, giving `[1, 0, 0]`.

---

### Tests

<ul>
<li id="test-1"><code>plus_one([1, 2, 9])</code> should return <code>[1, 3, 0]</code></li>
<li id="test-2"><code>plus_one([9, 9])</code> should return <code>[1, 0, 0]</code></li>
<li id="test-3"><code>plus_one([1, 2, 3])</code> should return <code>[1, 2, 4]</code></li>
<li id="test-4"><code>plus_one([0])</code> should return <code>[1]</code></li>
<li id="test-5"><code>plus_one([4, 3, 2, 9])</code> should return <code>[4, 3, 3, 0]</code></li>
<li id="test-6"><code>plus_one([9])</code> should return <code>[1, 0]</code></li>
<li id="test-7"><code>plus_one([8, 9, 9, 9])</code> should return <code>[9, 0, 0, 0]</code></li>
<li id="test-8">Performance: 300,000 digits (a 1 followed by 299,999 nines), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def plus_one(digits):
    digits = digits[:]
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

Here `n` is the number of digits.

**Brute force:** join the digits into a string, turn it into an `int`, add one, and split it back into digits. It reads well, but turning a long string into an `int` and back takes time that grows with the square of the number of digits. Test 8 has 300,000 digits, which is far too slow (and newer Python versions refuse conversions this long by default).

**Bottleneck:** the conversions touch the whole number many times over, while adding one only changes the trailing nines and one more digit.

**Optimal idea:** add one like you would on paper. Walk from the right. A `9` plus one is `0` with a carry, so set it to `0` and keep going. Any other digit takes the carry and you can return right away.

**Why it's correct:** the carry only moves left past nines. The first digit that isn't `9` absorbs it, and everything to its left stays the same. If every digit was `9`, the answer is a `1` followed by all zeros, one digit longer.

**Complexity:** `O(n)` time in the worst case (all nines), often much less. `O(n)` space for the copy, so the caller's list isn't changed.

**Common mistakes:** forgetting the all-nines case and returning `[0, 0]` for `[9, 9]`. Adding one to every digit instead of stopping at the first one that isn't `9`.

</details>
