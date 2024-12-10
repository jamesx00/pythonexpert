---
lesson_name: Property Specificity
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 354
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 355
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

### Property specificity

Property specificity in Python means that if a property with the same name is defined within a class and an object, the value of the object's property takes precedence over the class property.

See the code below for an example:

```python
class Car:
    wheel = 4

regular_car = Car()
different_car = Car()

different_car.wheel = 10

print(regular_car.wheel) # Output: 4
print(different_car.wheel) # Output: 10
print(Car.wheel) # Output: 4
```

In the example above, when we change the property `wheel` of the object `different_car`, only the value in that object is changed to `10`, while the same property in both the `Car` class and `regular_car` stay the same.

We could even change the `Car.wheel` property, and `different_car.wheel` will still be `10`.

```python
Car.wheel = 5
print(different_car.wheel) # Output: 10
print(regular_car.wheel) # Output: 5
```

---

### Exercise

- Change the property `arms` of an object `fake_human` to be `10`.

#### Tests

<ul>
<li id="test-1"><code>Human.arms</code> must be <code>2</code></li>
<li id="test-2"><code>regular_human.arms</code> must remain <code>2</code></li>
<li id="test-3"><code>fake_human.arms</code> must be <code>10</code></li>
</ul>
