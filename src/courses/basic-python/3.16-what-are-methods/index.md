---
lesson_name: What are Methods
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 39
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 323
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

### What are methods

<div class="alert-info text-sm">
In this lesson, we will briefly discuss methods and will not yet talk about how to create methods. Instead, we will explain the concept in the object-oriented programming section.
</div>

A method is a function defined and can be called on different types of objects. For example, in the string data type or string object, there are methods that we mentioned earlier such as `str.upper()` and `str.lower()`. Upper and lower are methods of the string objects, and calling the same method on different objects will result in different outcomes. For example,

```python
print("abc".upper()) # ABC
print("def".upper()) # DEF
```

We can see that even though we call the method or function with the same name, `upper()`, the outcomes differ depending on the object that the method is called on.

There are many methods in the built-in types that come with the Python language that we cannot explain in full detail in this lesson. We can read the details of each method and its operation in the <a href="https://docs.python.org/3/library/stdtypes.html" target="_blank" class="text-blue-500">Python language documentation</a>.

<div class="alert-info text-sm">
Moving forward in the course, we will distinguish between calling functions and methods to avoid any confusion.
</div>

---

### Tests

<ul>
<li id="test-1">Call the method <code>title()</code> on the string object so that <code>sentence</code> is equal to <code>"Python Is An Amazing Programming Language!"</code></li>
</ul>
