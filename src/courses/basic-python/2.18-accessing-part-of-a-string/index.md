---
lesson_name: Accessing Part of a String
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 122
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 123
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

### Access part of a string

You can also extract a portion of a string by specifying a start and end index with the syntax `[start:end]`. This is called **slicing**.

For example:

```python
my_string = "Hello, World!"
substring = my_string[2:5]
print(substring) # Output: llo
```

<div class="alert-info text-sm">
Note that the end index is exclusive, so the character at the end index is not included in the substring.
</div>

We could leave out the start or the end of the index as well. By leaving out the starting index, we tell Python to include all the characters from the beginning. And if we leave out the ending index, we tell Python to include all characters until the end of the string.

For example:

```python
my_string = "Hello, World!"
print(my_string[:5]) # Hello
print(my_string[5:]) # , World!
print(my_string[:]) # Hello, World!
```

---

### Exercise

<ul>
<li id="test-1">Change the number within the <code>[]</code> brackets so that the variable <code>hello</code> has the value <code>"Hello"</code></li>
<li id="test-2">Use <strong>both</strong> starting and ending indexs.</li>
</ul>
