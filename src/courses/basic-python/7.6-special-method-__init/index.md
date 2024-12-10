---
lesson_name: Special Method __init__
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 344
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 345
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

### Special method \_\_init\_\_

We can create a method for a class by defining a function inside the class body. A method is a function defined within a class that can be called just like a regular function.

For example:

```python
class Car:
    def method_name(self):
        print("The method method_name is called")

car = Car()
car.method_name() # Output: The method method_name is called
```

<div class="alert-info text-sm">
The first parameter of a class method is always the object itself, which is conventionally named <code>self</code>. This value is automatically passed to the method whenever it is called, and we do not need to pass it ourselves.

In the example above, the <code>self</code> value will be the object <code>car</code>.

</div>

### What is the `__init__` method

The `__init__` method in Python is a special method, also known as the constructor method, which gets automatically called when an object is created from a class.

For example, if we update the `Car` class to have the `__init__` method, like so:

```python
class Car
    def __init__(self):
        print("A new car object is created")

car = Car() # Output: A new car is created
car2 = Car() # Output: A new car is created
```

Whenever we create a new car object with `Car()`, the method `__init__` is then called. In this case, the message `"A new car object is created"` is then printed in the output.

---

### Exercise

- Create an `__init__` method inside out `Person` class that prints out a message whenever an object is created from the `Person` class. Then try creating an object from the `Person` class.

#### Tests

<ul>
<li id="test-1">The message <code>"A new person is created"</code> should be printed when a new <code>Person</code> object is created</li>
<li id="test-2">Variable <code>new_person</code> should be a <code>Person</code> object</li>
</ul>
