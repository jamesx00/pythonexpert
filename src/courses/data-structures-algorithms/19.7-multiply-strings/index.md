---
lesson_name: Multiply Strings
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(m * n)
  space: O(m + n)
hints:
  - "When you multiply two numbers on paper, where does the product of digit `i` of one and digit `j` of the other end up?"
  - "The product of `num1[i]` and `num2[j]` lands at position `i + j + 1` of a result array of length `len(num1) + len(num2)`, and its carry goes to `i + j`. See *Grade-school arithmetic on strings* in *Math & Geometry Basics*."
  - "Template: `result = [0] * (m + n)`. For `i` from the right of `num1`, for `j` from the right of `num2`: `total = d1 * d2 + result[i + j + 1]`, store `total % 10` there, and add `total // 10` to `result[i + j]`. Join the digits and strip leading zeros."
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

### Multiply Strings

You're given two non-negative integers, `num1` and `num2`, each represented as a string of digits (no leading zeros, unless the value itself is `"0"`). Write a function that returns the product of `num1` and `num2`, also as a string, computed without converting the entire strings to `int` or using a built-in big-integer multiply — the numbers may be far larger than fit comfortably in a normal integer type in other languages, so the point is to multiply digit by digit like you would on paper.

For example, `multiply("23", "45")` should return `"1035"`, since `23 * 45 = 1035`.

---

### Tests

<ul>
<li id="test-1"><code>multiply("23", "45")</code> should return <code>"1035"</code></li>
<li id="test-2"><code>multiply("2", "3")</code> should return <code>"6"</code></li>
<li id="test-3"><code>multiply("0", "52")</code> should return <code>"0"</code></li>
<li id="test-4"><code>multiply("123", "456")</code> should return <code>"56088"</code></li>
<li id="test-5"><code>multiply("999", "999")</code> should return <code>"998001"</code></li>
<li id="test-6"><code>multiply("0", "0")</code> should return <code>"0"</code></li>
<li id="test-7"><code>multiply("100", "10")</code> should return <code>"1000"</code></li>
<li id="test-8"><code>multiply("9999", "99")</code> should return <code>"989901"</code></li>
<li id="test-9">Performance: two 200-digit numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            d1 = int(num1[i])
            d2 = int(num2[j])
            pos_low = i + j + 1
            pos_high = i + j
            total = d1 * d2 + result[pos_low]
            result[pos_low] = total % 10
            result[pos_high] += total // 10
    digits = ''.join(map(str, result)).lstrip('0')
    return digits if digits else "0"
```

Here `m` and `n` are the lengths of `num1` and `num2`.

**Brute force:** multiplication is repeated addition, so add `num1` to a running total `num2` times, using digit-by-digit string addition. The number of additions is the *value* of `num2`, not its length. With 200 digits (test 9) that's about `10^200` additions, which never finishes.

**Bottleneck:** the work grows with the size of the number instead of the number of digits.

**Optimal idea:** multiply the way you do on paper, one digit pair at a time. Digit `i` of `num1` times digit `j` of `num2` belongs at position `i + j + 1` of a result array with `m + n` slots. Add it in, keep the last digit there, and push the carry one slot left.

**Why it's correct:** counting from the right, digit `i` of `num1` has place value `10^(m - 1 - i)` and digit `j` of `num2` has `10^(n - 1 - j)`. Their product has place value `10^(m + n - 2 - i - j)`, which is slot `i + j + 1` from the left in an array of length `m + n`. Every pair is added to its slot, and carries move left, so the array ends up holding the digits of the product. The product of an `m`-digit and an `n`-digit number has at most `m + n` digits, so nothing overflows the array.

**Complexity:** `O(m * n)` time, one step per digit pair. `O(m + n)` space for the result array.

**Common mistakes:** forgetting to strip leading zeros, so `"23" * "45"` gives `"01035"`. Then stripping everything from `"0" * "52"` and returning `""` instead of `"0"`. Calling `int(num1) * int(num2)`, which skips the point of the exercise.

</details>
