---
lesson_name: Python Tuples
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 175
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 176
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

### Python Tuples

In Python, a tuple is similar to a list, but tuples have a property called **immutability**, meaning that once a tuple is defined, the data inside it cannot be changed.

We can define a tuple using parentheses `()`, which is different from creating a list with square brackets `[]`:

```python
list_of_numbers = [1, 2, 3] # Define a list
tuple_of_numbers = (1, 2, 3) # Define a tuple
print(tuple_of_numbers)
```

We can also create a tuple from a list by calling the function `tuple()`, which takes a list as an argument:

```python
my_list = ["A", "B", "C", "D"]
my_tuple = tuple(my_list)
print(my_tuple) # Output: ('A', 'B', 'C', 'D')
```

Because of immutability, we cannot modify the data inside a tuple like we can with a list. If we try to modify a tuple, we'll get a <span class="text-red-500">TypeError: 'tuple' object does not support item assignment error:</span>

```python
tuple_of_numbers = (1, 2, 3)
tuple_of_numbers[2] = 5 # TypeError: 'tuple' object does not support item assignment
```

We can use the `len()` function to get the length of a tuple, just like with a list or string:

```python
t = (1, 2, 3)
print(len(t)) # 3
```

Accessing Elements in a Tuple
We can access elements in a tuple just like with a list:

```python
fruits = ("apple", "banana", "orange", "apple")
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[-2]) # orange
```

---

### Exercise

<ul>
<li id="test-1">Change the code so that <code>numbers</code> is a tuple instead of a list.</li>
</ul>
