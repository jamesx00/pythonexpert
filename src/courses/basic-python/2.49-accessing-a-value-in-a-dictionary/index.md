---
lesson_name: Accessing a Value in a Dictionary
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 180
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 179
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

### Accessing a value in a dictionary

You can access a value in a dictionary by using sqare brackets `[]` and its key, like this `dict[key]`:

For example:

```python
my_dict = {
    "name": "John", # <--- my_dict["name"]
    "age": 25, # <--- my_dict["age"]
    "city": "New York",
}

name = my_dict["name"]
print(name) # "John"
```

In the example above, we retrieve the value of the key `"city"` of the dictionary `my_dict` and assign it to the variable `name`.

---

### Exercise

Create a new variable `city` and assign its value to be`"New York"` by accessing it from the given dictionary.

#### Tests

<ul>
<li id="test-1">Variable <code>city</code> should be <code>"New York"</code></li>
<li id="test-2">Use <code>[]</code> to access the value</li>
</ul>
