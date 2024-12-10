---
lesson_name: Looping Through Keys in a Dictionary
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 262
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 261
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

### Looping Through Keys in a Dictionary

Let's take a look at an example of looping through dictionary data:

```python
my_student = {"name": "James", "age": 10, "gender": "M"}
for i in my_student:
    print(i)
```

```bash
Output
# name
# age
# gender
```

We can see that the data printed out are the keys of the dictionary. We can use this to access the values of the dictionary:

```python
my_student = {"name": "James", "age": 10, "gender": "M"}
for key in my_student:
    print(my_student[key])
```

```bash
Output
# James
# 10
# M
```

---

### Exercise

Loop through the given dictionary `person` and append its values to the list `properties`.

#### Tests

<ul>
<li id="test-1">The list <code>properties</code> should contain <code>"George"</code>, <code>35</code>, and <code>"M"</code></li>
</ul>
