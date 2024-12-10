---
lesson_name: Equality Comparison Between Objects
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 360
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 361
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

### Equality comparison between objects

Let's do a quick equality comparison between two `MyStr` objects.

```python
sentence1 = MyStr("Hello World!")
sentence2 = MyStr("Hello World!")
print(sentence1 == sentence2) # Output: False
```

This is not the behavior we want. We want our `MyStr` objects to return `True` the same way `str` objects are equal. For example:

```python
sentence1 = "Hello World"
sentence2 = "Hello World"
print(sentence1 == sentence2) # Output: True
```

### Special method `__eq__`

In the first example in this lesson, the only way equality comparison `==` will return `True` is when both objects are the same object.

For example:

```python
sentence1 = MyStr("Hello World!")
print(sentence1 == sentence1) # Output: True
```

To implement custom equality comparison for our objects, we need to define the special method `__eq__` in our class. For example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

dog1 = Dog("Boss")
dog2 = Dog("Boss")
dog3 = Dog("Bingo")
print(dog1 == dog2) # Output: True
print(dog1 == dog3) # Output: False
```

In the example above, the `__eq__` method takes two arguments: the object itself `self`, and the other object to compare to `other`. This function is called when `==` operator is used to compare two objects. The code `dog1 == dog2` will call the `__eq__` method with `dog1` as `self`, and `dog2` as `other`. If both dogs' names are the same, the method returns `True`, otherwise it returns `False`.

---

### Exercise

- Add the `__eq__` method to our `MyStr` class to mimick regular strings.

#### Tests

<ul>
<li id="test-1"><code>MyStr("Hello World") == MyStr("Hello World")</code> should equal to <code>True</code></li>
<li id="test-2"><code>MyStr("Hello World") == MyStr("Python is awesome")</code> should equal to <code>False</code></li>
</ul>
