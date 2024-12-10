---
lesson_name: Count an Item in a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 169
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 170
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

### Count an item in a list

The `list.count()` method in Python is used to count the number of occurrences of a specific item in a list. It takes a single argument, which is the item to be counted.

For example:

```python
fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'apple']
count = fruits.count('apple')
print(count)  # Output: 3
```

---

### Exercise

Use the method `count()` to count the number of `"cherry"` in the list and assign to the variable `count`

#### Tests

<ul>
<li id="test-1">Variable <code>count</code> should be the number of <code>"cherry"</code> in the list <code>fruits</code></li>
<li id="test-2">Use <code>count()</code> function</li>
<li id="test-3">Do not edit the first line of code</li>
</ul>
