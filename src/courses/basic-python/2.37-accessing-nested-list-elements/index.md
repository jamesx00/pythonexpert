---
lesson_name: Accessing Nested List Elements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 159
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 160
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

### Accessing Nested List Elements

To access the data of a nested list in Python, you can use the square brackets operator `[]` and specify the index of the nested list that you want to access.

For example, consider the previous nested list:

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Here's what you get when you try to access the first element of the list:

```python
print(my_list[0]) # output: [1,2,3]
```

And to access the first element within the first element, you can simply add another set of square brackets, like so:

```python
print(my_list[0][0]) # output: 1
```

---

### Exercise

<ul>
<li id="test-1">Given a list <code>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code>, get the second element of the second element and assign it to a variable <code>wanted_element</code></li>
<li id="test-2">Make sure to use <code>[]</code> to get the element</li>
<li id="test-3">Do not edit the first line of the code</li>
</ul>
