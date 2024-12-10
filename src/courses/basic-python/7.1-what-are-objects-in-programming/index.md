---
lesson_name: What are Objects in Programming
code_editor: True
code_execution: True
adding_file_allowed: False
section: Object-Oriented Programming
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 336
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 337
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

### What are objects in programming

In programming, objects are fundamental building blocks that represent real-life entities, concepts, or things. They encapsulate data (attributes) and behavior (methods) into a single entity.

Consider a person as a real-life example. A person can be represented as an object in programming. The person object can have attributes such as name, age, and address. These attributes describe the characteristics or state of the person. The person object can also have behaviors like walking, talking, and eating, which is implemented as methods

#### Everything in Python is an object

In Python, everything is an object. Objects are instances of classes. A class defines the blueprint for creating objects of a specific type. For example, integers, strings, lists, and functions are all objects in Python.

When we create a string in Python, we create a string object instance from a `str` class. Apart from how we created strings in previous lessons, we can instantiate a new string object with the `str` class, like so:

```python
my_string = str("Hello, World!") # <- Create a string from str class
other_string = "Hello, World!"
```

---

### Exercise

- Create a new string `my_sentence` by using the `str` class.

#### Tests

<ul>
<li id="test-1"><code>my_sentence</code> should be a string <code>"Python is awesome!"</code></li>
<li id="test-2">The string was created by calling the <code>str</code> class.</li>
</ul>
