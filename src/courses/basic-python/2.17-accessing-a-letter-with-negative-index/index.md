---
lesson_name: Accessing a Letter with Negative Index
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 121
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 120
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

### Access a letter in a string with a negative index

In the previous lesson, we learn that an **index** is a numeric value that represents the position of an element within a sequence, such as a string or a list. The first element in a sequence has an index of 0, the second has an index of 1, and so on.

In Python, negative index refers to indexing in reverse order, starting from the end of the sequence. The last item has an index of `-1`, the second last item has an index of `-2`, and so on.

For example:

```python
my_string = "Hello, World!"
last_character = my_string[-1]
print(first_character) # Output: !
```

---

### Exercise

<ul>
<li id="test-1">Change the number <code>0</code> in the <code>[]</code> so that variable <code>comma</code> is set to the value <code>,</code></li>
<li id="test-2"><strong>Must use</strong> negative index</li>
</ul>
