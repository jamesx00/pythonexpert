---
lesson_name: Data Unpacking in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 256
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 255
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

### Data unpacking in Python

Data unpacking in Python refers to the process of extracting values from a data structure, such as a tuple or a list, and assigning them to individual variables. It allows you to conveniently access and work with the elements of a collection without explicitly indexing them.

Here's a simple example to demonstrate data unpacking:

```python
# Tuple with three elements
person = ('John', 25, 'London')

# Unpacking the tuple into separate variables
name, age, city = person

# Accessing the unpacked values
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

Output:

```bash
Name: John
Age: 25
City: London
```

In this example, the tuple `person` contains three elements: the name, age, and city of a person. By assigning these elements to the variables `name`, `age`, and `city` in a single line, we unpack the values from the tuple. Each variable is assigned the corresponding value from the tuple, allowing us to access and work with them individually.

---

### Exercise

Unpack the values from the variable `employee` into variables `name`, `age`, and `department` respectively.

#### Tests

<ul>
<li id="test-1">Variable <code>employee</code> should be <code>"Jane Smith"</code></li>
<li id="test-2">Variable <code>age</code> should be <code>28</code></li>
<li id="test-3">Variable <code>department</code> should be <code>"Marketing"</code></li>
<li id="test-4">Use data unpacking to assign all 3 variables in a single line</li>
</ul>
