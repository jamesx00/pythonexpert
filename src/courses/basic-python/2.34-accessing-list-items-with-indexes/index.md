---
lesson_name: Accessing List Items with Indexes
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 153
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 154
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

### Accessing an element in a list

We can access individual elements of a list using its **index** just like strings. The index starts at 0 for the first element and increases by 1 for each subsequent element. For example:

```python
my_list = ['apple', 'banana', 'cherry']
print(my_list[0]) # Output: 'apple'
print(my_list[1]) # Output: 'banana'
print(my_list[2]) # Output: 'cherry'
```

We can also access elements of a list using the negative index, which starts at -1 for the last element and decreases by 1 for each preceding element. For example:

```python
my_list = ['apple', 'banana', 'cherry']
print(my_list[-1]) # Output: 'cherry'
print(my_list[-2]) # Output: 'banana'
print(my_list[-3]) # Output: 'apple'
```

---

### Exercise

<ul>
<li id="test-1">Create a new variable named <code>fruit</code> and <strong>assign the first element</strong> of <code>my_fruits</code> to it</li>
<li id="test-2">Must use list index with <code>[]</code> to assign the value</li>
</ul>
