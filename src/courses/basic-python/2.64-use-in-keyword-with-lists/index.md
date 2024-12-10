---
lesson_name: Use in Keyword with Lists
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 207
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 208
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

### Use in keyword with lists

The `in` keyword can also be used to check if an item is present in a list.

For example:

```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("apple" in fruits) # output: True
print("grape" in fruits) # output: False
```

---

### Exercise

- Check if the list `programming_languages` contains the item `"English"` and assign it to the variable `has_english`.
- Check if the list `programming_languages` contains the item `"JavaScript"` and assign it to the variable `has_javascript`.

#### Tests

<ul>
<li id="test-1">Variable <code>has_english</code> should be <code>False</code></li>
<li id="test-2">Variable <code>has_javascript</code> should be <code>True</code></li>
</ul>
