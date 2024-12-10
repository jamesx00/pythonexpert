---
lesson_name: For Loop with Data Unpacking
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 257
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 258
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

### For loop with data unpacking

When iterating over a sequence or collection in Python using a `for` loop, you can use data unpacking to assign the individual elements of each item to separate variables. This allows you to conveniently access and work with the individual components of the items within the loop.

Here's an example to illustrate data unpacking within a for loop:

```python
students = [
    ('John', 25, 'Math'),
    ('Jane', 22, 'Science'),
    ('Michael', 24, 'English')
]

for student in students:
    name, age, subject = student
    print(f"Name: {name}, Age: {age}, Subject: {subject}")
```

We can even make it shorter by unpacking the data within `for` loop statements, like so:

```python
for name, age, subject in students:
    print(f"Name: {name}, Age: {age}, Subject: {subject}")
```

---

### Exercise

Unpack the data to print the messages instead of accessing the data with the indexes.

#### Tests

<ul>
<li id="test-1">Unpack the data into variables <code>name</code>, <code>age</code>, and <code>subject</code> respectively</li>
</ul>
