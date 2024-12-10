---
lesson_name: Looping Through a List with Enumerate
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 260
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 259
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

### Looping through a list with enumerate

Sometimes, when looping over a sequence or collection, such as strings, lists, or tuples in Python, you may need to access both the elements themselves and their corresponding indexes. In such cases, you can use the `enumerate()` function to obtain the index and value of each element during iteration.

Here's what happens when you call `enumerate()` with a list as the argument.

```python
names = ["John", "Jane", "Michael"]
print(list(enumerate(names)))
```

```bash
Output
[(0, 'John'), (1, 'Jane'), (2, 'Michael')]
```

In this example, the `enumerate()` function generates a sequence of index-value pairs for the list `names`.

We can use data unpacking to loop through the list, like so:

```python
selected_names = []
for index, name in enumerate(names):
    if index % 2 == 0:
        selected_names.append(name)
print(selected_names) # ['John', 'Michael']
```

In the example above, the goal is to select and store the names at even positions from the original list. The `if` statement with the modulo operator `%` helps filter out the names based on their index. The resulting names are then added to the `selected_names` list using the `append()` method.

---

### Exercise

Use the function `enumerate()` to loop through the given list `names` and append all the values except the first element to the `output` list.

#### Tests

<ul>
<li id="test-1">Use the function <code>enumerate()</code></li>
<li id="test-2"><code>output</code> should be <code>['Cassandra Sullivan', 'Brooke Stevens', 'Amanda Smith', 'Mary Smith']</code></li>
</ul>
