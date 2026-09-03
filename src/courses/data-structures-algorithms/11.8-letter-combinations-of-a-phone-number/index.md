---
lesson_name: Letter Combinations of a Phone Number
code_editor: True
code_execution: True
adding_file_allowed: False
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
<li id="test-6"><code>letter_combinations("79")</code> should return 16 two-letter combinations from <code>"pqrs"</code> and <code>"wxyz"</code> (any order)</li>
</ul>
