---
lesson_name: String Immutability in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 138
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 139
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

### String Immutability in Python

In Python, a string is an **immutable** object, which means that once a string is created, it cannot be modified.

For example, consider the following code:

```python
string = "Hello, world!"
string[0] = "h"
```

This code will result in a <span class="text-red-500 font-bold">TypeError: 'str' object does not support item assignment</span>, because we are trying to modify a character in the string, which is not allowed.

Instead of changing a character in a string, we can create a new string and reassign it to the same variable, like so:

```python
string = "Hello, world!"
string = "hello, world!"
print(string) # hello, world!
```

---

### Example

<ul>
<li id="test-1">Update the code so that the <code>string</code> variable is <code>"How are you doing?"</code></li>
<li id="test-2">Keep the first line of the code the same</li>
</ul>
