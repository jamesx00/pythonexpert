---
lesson_name: Create a Simple Class
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 341
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 340
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

### Creating a simple class

Classes serve as blueprints or templates for creating objects. To create a class in Python, use the keyword `class` followed by the class name.

For example, here's how to create a `Car` class:

```python
class Car:
    pass
```

<div class="alert-info text-sm">
In Python, the naming convention for classes is to use the <b> Pascal case</b>, where the beginning of each word is a capital letter, with the exception of many built-in types, such as <code>str</code>, <code>list</code>.
</div>

Currently, the `Car` class is very basic. The `pass` keyword is used as a placeholder to indicate an empty class body.

---

### Exercise

- Create a new `Person` class with an empty class body.

#### Tests

<ul>
<li id="test-1"><code>Person</code> should be a class.</li>
</ul>
