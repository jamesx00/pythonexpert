---
lesson_name: Create an Object from a Class
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 342
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 343
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

### Creating an object from a class

Now that we have our own class, we can create a new object of that type by calling the class, just like calling a function:

```python
class Car:
    pass

car_object = Car()
print(type(car_object)) # <class '__main__.Car'>
```

When we call the function `type()` with the `car_object` as an argument, we can see that the type of that object is now `__main__.Car`, which tells us that the object is type `Car`, defined in the file being run (`__main__`).

---

### Exercise

- Create a new object `person` from the `Person` class.

#### Tests

<ul>
<li id="test-1">Variable <code>person</code> must be an instance of the <code>Person</code> class</li>
</ul>
