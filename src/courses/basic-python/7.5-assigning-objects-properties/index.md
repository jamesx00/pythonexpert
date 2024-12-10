---
lesson_name: Assigning Object's Properties
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 346
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 347
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

### Assigning object's properties

We can both access and assign an object's property by using the `.` (dot notation). The property is attached to each object and not shared among other objects created by the same class.

For example:

```python
class Car:
    pass

new_car = Car()
new_car.brand = "Toyota"
print(new_car.brand) # Toyota

another_car = Car()
print(another_car.brand) # AttributeError: 'Car' object has no attribute 'brand'
```

In the example above, we create a new object `new_car` from the class `Car`. We then assigned the property `brand` with the value `"Toyota"` to the `new_car` object. We can then access the `brand` property by using `new_car.brand`. But when we try to access the same property in another car object `another_car`, we then get the error `AttributeError` telling us that the object does not have the attribute `brand` yet.

---

### Exercise

- Assign a number to the property `age` to the object `person`.
- Assign another number to the property `age` to the object `another_person`.

#### Tests

<ul>
<li id="test-1"><code>person.age</code> should be a number from <code>1</code> to <code>100</code></li>
<li id="test-2"><code>another_person.age</code> should be a number from <code>1</code> to <code>100</code></li>
<li id="test-3"><code>person.age</code> and <code>another_person.age</code> should not be the same number</li>
</ul>
