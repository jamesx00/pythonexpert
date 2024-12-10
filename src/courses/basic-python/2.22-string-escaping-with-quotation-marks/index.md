---
lesson_name: String Escaping with Quotation Marks
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 132
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 133
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

### String Escaping with Quotation Marks

In Python, strings are defined using either single quotes ('...') or double quotes ("..."). If a string contains a quotation mark of the same type that is being used to define the string, the program will get confused and will assume that the string has ended. This is where the concept of "escaping" comes in.

To include a quotation mark of the same type that is being used to define the string, you can escape it by adding a backslash `\` before the quotation mark.

For example, this is okay because the quotation marks that are being used are of a different type:

```python
print('He said, "Hello!"')
```

But if you wanted to use double quotes to define the string, but the string also contains double quotes, you would escape the quotes like this:

```python
print("He said, \"Hello!\"")
```

---

### Exercise

<ul>
<li id="test-1">Fix the value of <code>sentence_1</code> to be <code>I'm going to the store.</code></li>
<li id="test-2">Fix the value of <code>sentence_2</code> to be <code>She said, "I'll be there soon."</code></li>
</ul>
