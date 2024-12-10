---
lesson_name: Method Resolution Order
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 372
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 373
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

### Method Resolution Order

In Python, Method Resolution Order (MRO) refers to the order in which methods are searched for and resolved in a class hierarchy, especially when multiple inheritance is involved. Understanding MRO is crucial for correctly determining which implementation of a method will be used when there are overlapping method names in the inheritance chain.

Here's an example to demonstrate MRO in multiple inheritance:

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # Output: "B"
```

In the example above, class `D` inherits from both class `B` and class `C`, which in turn inherit from class `A`. The MRO for class `D` is `D -> B -> C -> A`, following the order of inheritance. When the `method()` is invoked on an instance of class `D`, the MRO is consulted, and the leftmost occurrence of the method in the MRO (`B`) is used.

We can inspect the class property `__mro__` to see the MRO of the class. For example:

```python
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

You will see the order of resolution `main.D -> main.B -> main.C -> main.A` in the output.

---

### Exercise

- Switch the inheritance order in line 14 to get the desired output.

#### Tests

<ul>
<li id="test-1"><code>D().method()</code> should return <code>"C"</code></li>
<li id="test-2">Do not change the implementation of the classes <code>A</code>, <code>B</code>, <code>C</code>, and <code>D</code></li>
<li id="test-3">Class <code>D</code> must inherit from classes <code>A</code>, <code>B</code>, and <code>C</code></li>
</ul>
