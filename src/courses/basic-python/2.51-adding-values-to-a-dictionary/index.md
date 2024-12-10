---
lesson_name: Adding Values to a Dictionary
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 183
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 184
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

### Adding values to a dictionary

When we assign a dictionary with a key that does not exist, the value will be added to the dictionary.

For example:

```python
my_dict = {}
my_dict["country"] = "USA"
print(my_dict) # output: {'country': 'USA'}
```

In the example above, we created an empty dictionary. We then assigned the value **"USA"** to the key **"country"** with the code `my_dict["country"] = "USA"`. The value is then added to the dictionary.

---

### Exercise

We have created a dictionary `job_position`. Add a new key `"salary"` and set it to any number value.

#### Tests

<ul>
<li id="test-1"><code>job_position["salary"]</code> should be a number value</li>
</ul>
