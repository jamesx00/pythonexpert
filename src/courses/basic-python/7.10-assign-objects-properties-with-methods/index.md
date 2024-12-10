---
lesson_name: Assign Object's Properties with Methods
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 351
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 350
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

### Setting objects' properties with methods

Instead of setting an object's property directly, it is more common and preferred to set or change the properties with an object's method.

For example, instead of setting the `brand` property of a `Car` object like this:

```python
car.brand = "Toyoto"
```

We could add a method to set the `brand` property, and call that method instead:

```python
class Car:
   def set_brand(self, brand):
        self.brand = brand

car = Car()
car.set_brand("Toyoto")
print(car.brand) # Output: Toyoto
```

When the code `self.brand = brand` is executed, since `self` is the object calling the method, it is equivalent to running the code `car.brand = brand`.

### Required properties

One very common way to set an object's properties is with the `__init__` method. Instead of allowing the `Car` object to be created without the `brand` property, we can make it required so that all cars have this property, like so:

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

toyoto = Car("Toyoto")
honde = Car("Honde")

print(toyoto.brand) # Output: Toyoto
print(honde.brand) # Output: Honde
```

---

### Exercise

- With the given class `Person`, update the `__init__` method so that the construction input is set as the object's properties.

#### Tests

<ul>
<li id="test-1"><code>Person("Abbey", 30)</code> should create an object with the below properties<ul>
<li id="test-2">Property <code>name</code> should be <code>"Abbey"</code></li>
<li id="test-3">Property <code>age</code> should be <code>30</code></li>
</ul>
</li>
<li id="test-4"><code>Person("Eric", 40)</code> should create an object with the below properties<ul>
<li id="test-5">Property <code>name</code> should be <code>"Eric"</code></li>
<li id="test-6">Property <code>age</code> should be <code>40</code></li>
</ul>
</li>
</ul>
