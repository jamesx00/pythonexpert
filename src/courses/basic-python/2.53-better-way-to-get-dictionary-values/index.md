---
lesson_name: Better Way to Get Dictionary Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 187
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 188
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

### Better way to get dictionary values

When we try to get a dict value using a key that doesn't exist, Python raises a `KeyError` exception. This means that the key is not present in the dictionary, and the value cannot be accessed. And when an error happens, the program will stop running.

For example:

```python
employee = {"name": "John", "age": 30, "position": "developer"}
gender = employee["gender"] # KeyError: 'gender'
print("Hello World!") # This will not run
```

A better way to get a dictionary value in Python is to use the `get()` method. The `get()` method returns the value for the specified key, but if the key is not found in the dictionary, it returns a default value instead of raising a `KeyError`. This can help avoid errors in case the key is not in the dictionary.

The syntax for `get()` method is:

```python
dict.get(key, default_value)
```

where **key** is the key of the item you want to retrieve from the dictionary and **default_value** is the value that the method will return if the key is not
found in the dictionary. If default_value is not specified, it defaults to `None`.

```python
employee = {"name": "John", "age": 30, "position": "developer"}

# Accessing an existing key with get()
position = employee.get("position")
print(position) # Output: developer

# Accessing a non-existing key with get()
salary = employee.get("salary", 50000)
print(salary) # Output: 50000

# Accessing a non-existing key without default value
gender = employee.get("gender")
print(gender) # Output: None
```

In the example above, the `get()` method is used to retrieve the value for the `"position"` key from the `employee` dictionary. It returns `"developer"`, since the value exists in the dictionary.

Then, the `get()` method is used again to retrieve the value for a non-existing `"salary"` key from the employee dictionary. Since the `"salary"` key does not exist, the method returns the default value of 50000.

The last `get()` method is called to get the value for the key `"gender"`, which does not exist in the dictionary. But since we do not provide the default value, we get the value `None` as a default.

---

### Exercise

- We have created a dictionary `course_details`. Use this dictionary and `get()` method to create following variables:
  - `course_name` to be the value of the key `"name"`.
  - `course_description` to be the value of the key `"description"`, but default to `"Learn how to program in Python."`.
  - `course_stars` to be the value of the key `"stars"`. Do not provide a default value.

#### Tests

<ul>
<li id="test-1">Variable <code>course_name</code> should be <code>"Python Programming"</code></li>
<li id="test-2">Variable <code>course_description</code> should be <code>"Learn how to program in Python."</code></li>
<li id="test-3">Variable <code>course_stars</code> should be <code>None</code></li>
</ul>
