---
lesson_name: Overriding Parent Class Methods
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 367
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 366
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

### Overriding parent class methods

Child classes can override methods inherited from the parent class by redefining them with the same name. This allows child classes to modify the behavior of the inherited method to suit their specific needs.

Let's take a look at an example from the previous lesson:

```python
class Animal:
    alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"The animal {self.name} is eating")

class Dog(Animal):
    def eat(self):
        print(f"The dog named {self.name} is eating")
```

In the example above, the `Dog` class has its own `eat()` method. And when we call this method from `Dog` objects, it will call the `eat()` method from the `Dog` class instead of the `Animal` class.

```python
bird = Animal("Bird")
dog = Dog("Clark")
bird.eat() # The animal Bird is eating
dog.eat() # The dog named Clark is eating
```

---

### Exercise

- Define the `__str__` method in our `MyUpperStr` class to return the text in all uppercase instead of the original text value. You can use the `upper()` method for this challenge.

#### Tests

<ul>
<li id="test-1"><code>print(MyStr("Python is awesome!"))</code> should print the message <code>"Python is awesome!"</code></li>
<li id="test-2"><code>print(MyUpperStr("Python is awesome!"))</code> should print the message <code>"PYTHON IS AWESOME!"</code></li>
</ul>
