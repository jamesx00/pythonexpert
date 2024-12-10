---
lesson_name: Deleting Dictionary Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 186
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 185
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

### Deleting Dictionary Values

In Python, you can delete a value from a dictionary using the `del` keyword followed by the key of the value you want to delete. Here's an example:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict) # Output: {'a': 1, 'c': 3}
```

In the above example, we first define a dictionary `my_dict` with three key-value pairs. We then use the `del` keyword to delete the value associated with the key `b`. When we print the resulting dictionary, we could see that it contains only the key-value pairs for `a` and `c`.

---

### Exercise

Delete the key `"salary"` from the dictionary `employee`.

#### Tests

<ul>
<li id="test-1">The dictionary <code>employee</code> should not have the key <code>"salary"</code></li>
<li id="test-2">Use <code>del</code> keyword to remove the key</li>
</ul>
