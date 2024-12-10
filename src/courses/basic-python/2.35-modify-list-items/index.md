---
lesson_name: Modify List Items
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 155
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 156
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

### Modify list elements

Because Python lists are **mutable**, this means that once we declare a list, we can change its content. We can modify elements of a list by assigning new values to them.

For example:

```python
my_list = ['apple', 'banana', 'cherry']
my_list[1] = 'orange'
print(my_list) # Output: ['apple', 'orange', 'cherry']
```

---

### Exercise

<ul>
<li id="test-1">Change the value of the last element of the list <code>my_list</code> to <code>"Four"</code></li>
<li id="test-2">Must use list index to reassign the value</li>
</ul>
