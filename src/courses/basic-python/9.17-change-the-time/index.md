---
lesson_name: Change The Time
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 437
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 438
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

### Change the time

Write a function that updates the time given the current time in 24-hour format as a string, e.g. `15:00`, and an integer to change the time. The integer can be positive or negative, indicating the number of minutes to add or subtract from the current time. The function should return a string representing the updated time.

---

### Tests

<ul>
<li id="test-1"><code>change_time("12:30", 45)</code> should return <code>"13:15"</code></li>
<li id="test-2"><code>change_time("23:45", -90)</code> should return <code>"22:15"</code></li>
<li id="test-3"><code>change_time("06:00", 120)</code> should return <code>"08:00"</code></li>
<li id="test-4"><code>change_time("09:15", -60)</code> should return <code>"08:15"</code></li>
<li id="test-5"><code>change_time("18:30", 0)</code> should return <code>"18:30"</code></li>
<li id="test-6"><code>change_time("23:55", 10)</code> should return <code>"00:05"</code></li>
<li id="test-7"><code>change_time("00:05", -10)</code> should return <code>"23:55"</code></li>
</ul>
