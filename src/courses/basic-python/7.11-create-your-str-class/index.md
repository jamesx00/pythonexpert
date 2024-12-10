---
lesson_name: Create Your Str Class
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 357
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 356
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

### Create Your Str Class

In these next lessons, we will learn to implement our own `str` class to get a better understanding of utilizing a class and common special methods in Python.

Let's take a look at how to create a string object from the `str` class:

```python
sentence = str("Python is amazing!")
```

This is what we will try to mimic in this lesson. Let's not think too far ahead and start by implementing a very simple class here.

---

### Exercise

- Define the `__init__` method inside the class `MyStr` to mimic the behavior of the class `str` above.

#### Tests

<ul>
<li id="test-1">Create a new class named <code>MyStr</code></li>
<li id="test-2"><code>MyStr("Python is amazing!")</code> should create a new object</li>
</ul>
