---
lesson_name: Adding an Element to a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 165
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 166
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

### Adding a new element to a list

We can add a new element to the end of a list using the `append()` function. It takes a single argument, which is the element that needs to be added to the list.

For example:

```python
my_list = ['apple', 'banana', 'cherry']
my_list.append('orange')
print(my_list) # Output: ['apple', 'banana', 'cherry', 'orange']
```

---

### Exercise

- Use the function `append()` any value to the variable `my_list`

### Tests

<ul>
<li id="test-1">The length of <code>my_list</code> should have more than 4 elements</li>
<li id="test-2">Use the function <code>append()</code></li>
<li id="test-3">Do not change the first line of the code</li>
</ul>
