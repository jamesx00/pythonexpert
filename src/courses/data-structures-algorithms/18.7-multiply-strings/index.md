---
lesson_name: Multiply Strings
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
</ul>
