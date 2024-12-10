---
lesson_name: Change Message When Object is Printed
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 358
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 359
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

### Change message when an object is printed

Now that we have our own `MyStr` class, let's see the difference between when `MyStr` and `str` objects are printed.

```python
normal_str = str("Python is awesome!")
print(normal_str) # Output: Python is awesome!

my_str = MyStr("Python is awesome!")
print(my_str) # <__main__.MyStr object at 0x7fd0908896c0>
```

When `MyStr` object is printed, the message displays the type of the object, along with the position in the memory, which isn't very useful. We want the message to be the same as `str` object.

### Special method: `__str__`

The `__str__` method is a special method that provides a string representation of an object. It is called by the built-in `str()` function and the `print()` function when attempting to convert an object to a string.

For example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is a dog named {self.name}"

max_the_dog = Dog("Max")
print(max_the_dog) # This is a dog named Max
```

In the example above, we create a new class, `Dog`, which accepts an argument when constructed. The value of `name` is then set as an object property, conveniently named `name`. We then defined the method `__str__`, which returns a string to be the message when a `Dog` object is printed.

Now that we know how to use the method `__str__`, let's implement it in our `MyStr` class.

---

### Exercise

- Update the `__init__` method to set the property `text` in our `MyStr` class and implement the `__str__` method to return the value of `text` property.

#### Tests

<ul>
<li id="test-1"><code>MyStr("Python is awesome")</code> should create an object with following attributes:<ul>
<li id="test-2">Property <code>text</code> should be <code>"Python is awesome!"</code></li>
</ul>
</li>
<li id="test-3"><code>MyStr("Programming is fun")</code> should create an object with following attributes:<ul>
<li id="test-4">Property <code>text</code> should be <code>"Programming is fun"</code></li>
</ul>
</li>
<li id="test-5"><code>print(MyStr("Python is awesome!"))</code> should print the message <code>"Python is awesome!"</code></li>
</ul>
