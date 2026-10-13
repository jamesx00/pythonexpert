---
lesson_name: Letter Combinations of a Phone Number
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(4ⁿ · n)
  space: O(n)
hints:
  - "Each digit adds one letter, chosen from 3 or 4 options. How is that like *Generate Binary Strings*, with a different set of choices per position?"
  - "Use *The Template* from *Backtracking Basics*: the recursion goes one digit deeper per level, and the loop tries each letter for that digit. When the path has one letter per digit, record `\"\".join(path)`."
  - "Template: if `digits` is empty, return `[]`. `def backtrack(index)`: if `index == len(digits)`, record `\"\".join(path)`. For each `letter` in `digit_map[digits[index]]`: append, `backtrack(index + 1)`, pop."
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

### Letter Combinations of a Phone Number

Write a function `letter_combinations(digits)` that takes a string of digits from `2` through `9` (like an old telephone keypad) and returns every possible letter string that could be typed by pressing those digits in order, one letter per digit. Use the classic keypad mapping: `2 -> "abc"`, `3 -> "def"`, `4 -> "ghi"`, `5 -> "jkl"`, `6 -> "mno"`, `7 -> "pqrs"`, `8 -> "tuv"`, `9 -> "wxyz"`. If `digits` is empty, return an empty list. The order of the returned combinations does not matter.

For example, `digits = "23"` should produce every combination of one letter from `"abc"` (for the `2`) followed by one letter from `"def"` (for the `3`): `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`, in any order.

---

### Tests

<ul>
<li id="test-1"><code>letter_combinations("23")</code> should return <code>["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]</code> (any order)</li>
<li id="test-2"><code>letter_combinations("")</code> should return <code>[]</code></li>
<li id="test-3"><code>letter_combinations("2")</code> should return <code>["a", "b", "c"]</code> (any order)</li>
<li id="test-4"><code>letter_combinations("7")</code> should return <code>["p", "q", "r", "s"]</code> (any order)</li>
<li id="test-5"><code>letter_combinations("9")</code> should return <code>["w", "x", "y", "z"]</code> (any order)</li>
<li id="test-6"><code>letter_combinations("79")</code> should return <code>["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def letter_combinations(digits):
    if not digits:
        return []
    digit_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return
        for letter in digit_map[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

Here `n` is the number of digits.

**Brute force:** there isn't a faster idea. With up to 4 letters per digit there can be `4ⁿ` combinations of length `n`, and they all have to be returned, so `O(4ⁿ · n)` is the best possible. Nested loops would work for a fixed number of digits, but not for any length.

**Bottleneck:** the number of loops depends on the input, so they can't be written out by hand.

**Optimal idea:** let recursion stand in for the nested loops. Level `index` loops over the letters of `digits[index]` and recurses into the next digit, so the recursion is as deep as the input is long.

**Why it's correct:** each combination is one letter for each digit, in order. Every level tries every letter for its digit, so each combination is built exactly once.

**Complexity:** `O(4ⁿ · n)` time: at most `4ⁿ` results, each joined in `O(n)`. `O(n)` extra space for the path and recursion, not counting the output.

**Common mistakes:** returning `[""]` for empty input instead of `[]`, which this problem asks for (unlike *Generate Binary Strings* with `n = 0`). Building strings with `path + letter` is fine too, but then there's nothing to pop.

</details>
