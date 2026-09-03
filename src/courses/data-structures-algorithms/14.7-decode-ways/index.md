---
lesson_name: Decode Ways
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

### Decode Ways

Write a function `num_decodings(digits)` that takes a string of digits representing an encoded message, where `"1"` maps to `'A'`, `"2"` maps to `'B'`, and so on up to `"26"` mapping to `'Z'`. Return how many distinct ways the string can be decoded back into letters. A leading zero on its own, or as the first digit of a two-digit group, is never valid on its own (a `'0'` must always be paired with the digit before it as part of `"10"` or `"20"`), so a string containing an unpairable `'0'` decodes zero ways.

For example, given `digits = "226"`, the valid decodings are `"2-2-6"` (BBF), `"22-6"` (VF), and `"2-26"` (BZ), for a total of `3` ways.

---

### Tests

<ul>
<li id="test-1"><code>num_decodings("226")</code> should return <code>3</code></li>
<li id="test-2"><code>num_decodings("12")</code> should return <code>2</code></li>
<li id="test-3"><code>num_decodings("06")</code> should return <code>0</code></li>
<li id="test-4"><code>num_decodings("10")</code> should return <code>1</code></li>
<li id="test-5"><code>num_decodings("100")</code> should return <code>0</code></li>
<li id="test-6"><code>num_decodings("11106")</code> should return <code>2</code></li>
<li id="test-7"><code>num_decodings("")</code> should return <code>1</code></li>
</ul>
