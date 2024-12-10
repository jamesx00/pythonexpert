---
lesson_name: Class Inheritance
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 364
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 365
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

### Class Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and behaviors from another class. In Python, classes can be organized in a hierarchical structure using inheritance, creating a parent-child relationship between classes.

The class that is being inherited from is called the **"parent class"** or **"superclass,"** and the class that inherits from it is called the **"child class"** or **"subclass."** The child class inherits all the attributes and methods defined in the parent class.

A subclass can be created with the `class` keyword, followed by the subclass name, followed by parentheses of superclasses to inherit from. See the `Dog` class below as an example:

```python
class Animal
    alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"The animal {self.name} is eating")

class Dog(Animal):
    pass
```

In the example above, `Animal` is the parent class, and `Dog` is the child class that inherits from the `Animal` class. Any objects created from the `Dog` class will have the same properties and methods as those created from the `Animal` class.

```python
bird = Animal("Bird")
dog = Dog("Clark")
bird.eat() # The animal Bird is eating
dog.eat() # The animal Clark is eating
print(dog.alive) # True
```

---

### Exercise

- Create a new subclass `MyUpperStr` that inherits from our `MyStr` class.

#### Tests

<ul>
<li id="test-1"><code>MyUpperStr</code> is a subclass of the parent class <code>MyStr</code></li>
</ul>
