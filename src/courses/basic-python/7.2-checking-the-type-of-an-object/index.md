---
lesson_name: Checking the Type of an Object
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 338
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 339
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

### Checking the type of an object

The `type()` function is used to determine the class or type of an object. When you pass an object to the `type()` function, it returns the class that was used to create that object. In the example below, we could see that both `my_string` and `other_string` are created from the class `str`.

```python
my_string = str("Hello, World!")
other_string = "Hello, World!"

print(type(my_string)) # <class 'str'>
print(type(other_string)) # <class 'str'>
```

---

### Exercise

- Assign the type of `an_object` to the variable `type_of_object`

#### Tests

<ul>
<li id="test-1"><code>type_of_object</code> should be the class <code>list</code></li>
</ul>
