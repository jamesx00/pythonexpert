---
lesson_name: Class Properties
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 352
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 353
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

### Class properties

Class properties are defined at the class level and are shared among all objects created with that class.

When you change a class property, the new value is shared among all instances of the class, including instances that were created before the attribute was changed. For example:

```python
class Car:
    wheel = 4 # <- A class property

car1 = Car()
car2 = Car()

print(Car.wheel) # Output: 4
print(car1.wheel) # Output: 4
print(car2.wheel) # Output: 4

Car.wheel = 3 # <- Change made to Car class instead of car1 or car2.

car3 = Car()

print(Car.wheel) # Output: 3
print(car1.wheel) # Output: 3
print(car2.wheel) # Output: 3
print(car3.wheel) # Output: 3
```

In the example above, we could see that when we change the class property with `Car.wheel`, the value is changed on all objects created with the `Car` class, both before and after the change.

---

### Exercise

- Create a class property named `arms` with the value `2` to the class `Person`

#### Tests

<ul>
<li id="test-1"><code>Person.arms</code> must be <code>2</code></li>
</ul>
