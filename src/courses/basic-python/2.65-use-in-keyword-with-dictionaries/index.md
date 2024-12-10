---
lesson_name: Use in Keyword with Dictionaries
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 210
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 209
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

### Use in keyword with dictionaries

You can use the keyword `in` with dictionaries to check if a specific key exists in the dictionary or not.

For example:

```python
my_dict = {"name": "John", "age": 25, "gender": "male"}

print("name" in my_dict) # Output: True
print("country" in my_dict) # Output: False
```

In the example above, the code `"name" in my_dict` gives us `True`, because the dictionary `my_dict` has the key `"dict"`, while the key `"country"` does not exist in the dictionary.

---

### Exercise

- Find out if the key `"price"` exists in the dictionary `t_shirt` and assign the result to the variable `has_price`.
- Find out if the key `"gender"` exists in the dictionary `t_shirt` and assign the result to the variable `has_gender`.

#### Tests

<ul>
<li id="test-1">Variable <code>has_price</code> should be <code>True</code></li>
<li id="test-2">Variable <code>has_gender</code> should be <code>False</code></li>
</ul>
