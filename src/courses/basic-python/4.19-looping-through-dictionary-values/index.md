---
lesson_name: Looping Through Dictionary Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 264
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 263
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

### Looping through dictionary values

If we only need to access the values of the dictionary, we can use the `values()` method instead.

Here is an example looping through a dictionary values with `values()` method:

```python
my_student = {"name": "James", "age": 10, "gender": "M"}
print(my_student.values()) # dict_values(['James', 10, 'M'])

for value in my_student.values():
    print(value)
```

---

### Exercise

Loop through the dictionary `person` and add its values to the list `properties`.

#### Tests

<ul>
<li id="test-1">List <code>properties</code> should contain <code>"George"</code></li>
<li id="test-2">List <code>properties</code> should contain <code>35</code></li>
<li id="test-3">List <code>properties</code> should contain <code>"M"</code></li>
</ul>
