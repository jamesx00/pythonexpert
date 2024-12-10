---
lesson_name: Looping Through Dictionary Key-Value Pairs
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 265
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 266
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

### Looping through dictionary key-value pairs

The `items()` method returns a view object that contains the key-value pairs of the dictionary as tuples. By using the `for` loop and data unpacking, you can iterate over these pairs and access the individual key and value in each iteration.

Here's what happens when we call the method `items()` on a dictionary.

```python
my_dict = {'name': 'John', 'age': 30, 'country': 'USA'}
print(my_dict.items())
```

```bash
Output:
dict_items([('name', 'John'), ('age', 30), ('country', 'USA')])
```

We can see that the key-value pairs in the dictionary are now in a list of tuples. We can loop through a dictionary with the `items()` method like so:

```python
for key, value in my_dict.items():
    print(key, value)
```

```bash
Output
name John
age 30
country USA
```

---

### Exercise

Make a copy `copy_person` from the dictionary `person`.

#### Tests

<ul>
<li id="test-1"><code>copy_person</code> and <code>person</code> should have the same keys and values</li>
<li id="test-2"><code>copy_person</code> and <code>person</code> should not be the same object in memory</li>
</ul>
