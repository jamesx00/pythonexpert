---
lesson_name: Filter a List with Lambda Function
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 320
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 321
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

### Filter a List with Lambda Function

Write a function `filter_list(the_list, condition)` that takes a list `the_list` and a lambda function `condition` as input. The function should filter the given list based on the given condition and return a new list containing only the elements that satisfy the condition.

For example:

```python
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
condition = lambda x: x % 2 == 0  # filter even numbers
filtered_list = filter_list(the_list, condition)
print(filtered_list)  # Output: [2, 4, 6, 8, 10]
```

---

### Tests

<ul>
<li id="test-1"><code>filter_list([-2, -1, 0, 1, 2, 3, 4, 5], lambda x: x >= 0)</code> should return <code>[0, 1, 2, 3, 4, 5]</code>
<li id="test-2"><code>filter_list([10.0, 15, 2, 2.5, 9, -1, 9.9], lambda x: type(x) == int)</code> should return <code>[15, 2, 9, -1]</code>
<li id="test-3"><code>filter_list([1, "b", 3, "d", 5, "f"], lambda x: type(x) == str)</code> should return <code>["b", "d", "f"]</code>
</ul>
