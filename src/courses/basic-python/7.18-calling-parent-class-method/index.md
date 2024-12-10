---
lesson_name: Calling Parent Class' Method
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 368
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 369
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

### Calling parent class' methods

The `super()` function is a built-in function that allows you to access and invoke methods and properties from a parent class within a subclass. `super()` is often used in the context of inheritance, where a child class inherits from a parent class. By calling `super()` within a method of the child class, you can refer to the parent class and utilize its methods and properties.

For example:

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I'm {self.age} years old."

child = Child("Alice", 10)
print(child.greet())  # Output: Hello, Alice! I'm 10 years old.
```

In the example above, we have a `Parent` class with an `__init__()` method and a `greet()` method. The `Child` class inherits from the `Parent` class.

Within the `__init__()` method of the `Child` class, we use `super().__init__(name)` to call the `__init__()` method of the parent class and pass the `name` argument to it. This allows us to initialize the `name` attribute inherited from the parent class.

Similarly, in the `greet()` method of the `Child` class, we use `super().greet()` to call the `greet()` method of the parent class and retrieve the parent's greeting. We then extend the greeting by appending the child's age.

---

### Exercise

- Define the `__init__` method in our `MyUpperStr` to use the `__init__` method of its parent class.

#### Tests

<ul>
<li id="test-1"><code>MyStr("It's time to code!").text</code> should be <code>"It's time to code!"</code></li>
<li id="test-2"><code>print(MyStr("It's time to code!"))</code> should print out the message <code>"It's time to code!"</code></li>
<li id="test-3"><code>MyUpperStr("It's time to code!").text</code> should be <code>"IT'S TIME TO CODE!"</code></li>
<li id="test-4"><code>print(MyUpperStr("It's time to code!"))</code> should print out the message <code>"IT'S TIME TO CODE!"</code></li>
</ul>
