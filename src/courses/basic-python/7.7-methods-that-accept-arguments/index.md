---
lesson_name: Methods that Accept Arguments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 349
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 348
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

### Methods that accept arguments

Just like regular functions, class methods can accept arguments. In the previous lesson, we saw that you can define a string with the class `str` with an input argument, like so:

```python
sentence = str("This is a sentence")
print(sentence) # Output: This is a sentence
```

To allow class construction to accept arguments, we can add more parameters to the `__init__` method. For example:

```python
class Car:
    def __init__(self, brand, year):
        print("A new car is created")
        print(f"The brand is {brand}")
        print(f"The year is {year}")

car = Car("Yotoya", 1990)
```

```bash
# Output:
A new car is created
The brand is Yotoya
The year is 1990
```

In the example above, we add 2 more parameters to the construction method: `brand` and `year`. When we create a new object from the `Car` class, we need to provide the arguments for those parameters, just like a regular function, with the exception that the first parameter, `self`, is automatically provided by Python.

---

### Exercise

- Update the `__init__` method in the `Person` class to accept arguments.

#### Tests

<ul>
<li id="test-1"><code>Person("Abbey", 30)</code> should print the message <code>"Abbey is 30 years old"</code></li>
<li id="test-2"><code>Person("Eric", 40)</code> should print the message <code>"Eric is 40 years old"</code></li>
</ul>
