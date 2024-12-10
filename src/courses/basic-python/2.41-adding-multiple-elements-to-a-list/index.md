---
lesson_name: Adding Multiple Elements to a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 167
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 168
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

### Adding multiple elements to a list

You can only add one item at a time with the function `append()`. However, we can add multiple elements to the end of a list using the `extend()` function with a `list` as an argument.

For example:

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)   # [1, 2, 3, 4, 5]
```

### Difference between `append()` and `extend()`

- `append()` takes one argument of any type and adds it to the end of a list.
- `extend()` takes one list as an argument and adds each item to the end of a list.

For example:

```python
my_list = [1,2,3]
my_list.append([4, 5])
print(my_list) # output: [1, 2, 3, [4, 5]]

another_list = [1,2,3]
another_list.extend([4, 5])
print(another_list) # output: [1, 2, 3, 4, 5]
```

From the example above, `my_list` after append will have a length of **4** with the last element being the added list, while `another_list` will have a length of **5** from adding 2 elements to it.

---

### Exercise

Use the function `extend()` to add items `["E", "F"]` to the variable `my_list`

#### Tests

<ul>
<li id="test-1"><code>my_list</code> should become <code>["A", "B", "C", "D", "E", "F"]</code></li>
<li id="test-2">Use the function <code>extend()</code></li>
<li id="test-3">Do not change the first line of code</li>
</ul>
