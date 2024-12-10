---
lesson_name: Combine Strings with Compound Addition
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 126
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 127
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

### Concatenating strings with compound addition

As we can increase the value of the number by using the `+=` operator, we could use the same operator to concatenate strings together, like so:

```python
full_name = ""
full_name += "Fistname" # Equivalent to full_name = full_name + "Firstname"
full_name += " "
full_name += "Lastname"
print(full_name) # Output: Firstname Lastname
```

---

### Exercise

<ul>
<li id="test-1">Create a variable <code>full_name</code> by combining your first and last name together</li>
<li id="test-2">Use the <code>+=</code> operator to combine those strings</li>
<li id="test-3">Make sure that there is a space between your first and last name</li>
</ul>
