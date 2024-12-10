---
lesson_name: Convert Kilometers to Miles
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 279
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 278
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

### Convert kilometers to miles

Write a Python function that converts distance measurements in kilometers to miles. The function should take a distance value in kilometers as input and return the equivalent distance in miles.

To get an approximate result for this challenge, divide kilometers with `1.609` to get the length in miles.

---

### Tests

<ul>
<li id="test-1"><code>convert_km_to_mi(0)</code> should return a value of <code>0</code></li>
<li id="test-2"><code>convert_km_to_mi(10)</code> should return a value of <code>6.215040397762586</code></li>
<li id="test-3"><code>convert_km_to_mi(20)</code> should return a value of <code>6.215040397762586</code></li>
</ul>
