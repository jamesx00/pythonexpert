---
lesson_name: Variable Assignment with Mutable Objects
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 414
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 415
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

### Variable assignment with mutable objects

Mutable objects in Python, such as **dict**s and **list**s, are passed by reference, meaning that **if we assign a mutable object to multiple variables**, they all point to the same memory location. Modifying the object through one variable will affect all the other variables referencing the same object.

For example:

```python
person_a = {"name": "Coco"}
person_b = person_a # <-- Assign with existing dictionary
person_b["name"] = "Lala"
print(person_a) # {'name': 'Lala'}
print(person_b) # {'name': 'Lala'}
```

```mermaid
flowchart
    person_a --> person["{'name': 'Coco'} -> {'name': 'Lala'}"]
    person_b --> person
```

<p class="caption">
When we change the object in place, Python does not create a new object.
</p>

In this example, we modified the dict's `name` value, which affected both `person_a` and `person_b`. This is because they both point to the same object in the memory. The same happens for **list**s as well.

```python
list_a = [1, 2, 3]
list_b = list_a # <-- Assign with existing list
list_a.append(4)
print(list_a) # [1, 2, 3, 4]
print(list_b) # [1, 2, 3, 4]
```

---

### Exercise

Take a look at the code below:

```python
animal_a = {"type": "Dog"}
animal_b = animal_a
animal_a["name"] = "Fluffy"
```

1. What is the value of `animal_a`?
1. What is the value of `animal_b`?

#### Tests

<ul>
<li id="test-1">What is the value of <code>animal_a</code>?</li>
<li id="test-2">What is the value of <code>animal_b</code>?</li>
</ul>
