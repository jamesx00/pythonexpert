---
lesson_name: Remove Spaces from Both Ends of a String
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 149
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 148
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

### Remove space from both ends of a string

You can use the `strip()` method to remove whitespace from the beginning and end of a string.

For example, if you have a string `s = " hello world "`, you can use `strip()` to remove the whitespace like this:

```python
s = "   hello world   "
s_stripped = s.strip()
print(s_stripped) # Output: "hello world"
```

The `strip()` method removes any whitespace characters (spaces, tabs, newlines) from the beginning and end of the string. If you want to remove whitespace only from the beginning or end of the string, you can use the `lstrip()` or `rstrip()` methods, respectively.

---

### Exercise

<ul>
<li id="test-1">Use <code>strip()</code> method to remove all leading and trailing spaces before assigning the value to <code>new_sentence</code></li>
<li id="test-2">Keep the first line of code the same</li>
</ul>
